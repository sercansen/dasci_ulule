import torch.nn as nn
import torch
import torchvision.transforms as transforms
import torch.utils.data as Data
import numpy as np
import matplotlib.pyplot as plt
from torch.utils.data.sampler import SubsetRandomSampler
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from utils.utils import get_html_from_fig

def dataframe_to_dataloaders(dataframe):

    y = dataframe['goal_raised'].copy(deep=True)
    dataframe.drop(columns = ['amount_raised', 'comments_count', 'fans_count', 'goal_raised', 'id', 'percent', 'supporters_count'], axis = 1, inplace=True)
    shape = dataframe.shape[1]
    X_train, X_test, y_train, y_test = train_test_split(dataframe, y)
    X_train = StandardScaler().fit_transform(X_train.values)
    X_test = StandardScaler().fit_transform(X_test.values)

    y_train.replace(True, 1)
    y_train.replace(False, 0)
    y_test.replace(True, 1)
    y_test.replace(False, 0)
        
    ###creating tensors, datasets and dataloaders
    #creating our tensors
    X_train_tensor = torch.tensor(X_train)
    X_test_tensor = torch.tensor(X_test)

    y_train_tensor = torch.tensor(y_train.to_numpy().reshape(-1,1))
    y_test_tensor = torch.tensor(y_test.to_numpy().reshape(-1,1))

    #creating datasets from tensors

    train_dataset = Data.TensorDataset(X_train_tensor, y_train_tensor)
    test_dataset = Data.TensorDataset(X_test_tensor, y_test_tensor)

    #creating dataloaders

    batch_size = 64 # how many samples per batch to load
    num_train = len(train_dataset)

    test_loader = Data.DataLoader(test_dataset, batch_size = batch_size)

    valid_size = 0.2 # percentage of training set to use as validation

    # obtaining training indices that will be used for validation
    indices = list(range(num_train))
    np.random.shuffle(indices)
    split = int(np.floor(valid_size * num_train))
    train_index, valid_index = indices[split:], indices[:split]

    # defining samplers for obtaining training and validation batches
    train_sampler = SubsetRandomSampler(train_index)
    valid_sampler = SubsetRandomSampler(valid_index)

    # preparing data loaders
    train_loader = torch.utils.data.DataLoader(train_dataset, batch_size = batch_size, sampler = train_sampler)
    valid_loader = torch.utils.data.DataLoader(train_dataset, batch_size = batch_size, sampler = valid_sampler)

    return train_loader, valid_loader, test_loader, shape

class MLP(nn.Module):
    def __init__(self, n_features, n_hidden_1, n_hidden_2 , n_output):
        super(MLP, self).__init__()
        self.fc0 = nn.Linear(n_features, n_hidden_1)
        self.fc1 = nn.Linear(n_hidden_1, n_hidden_2)
        self.fc2 = nn.Linear(n_hidden_2, n_output)
        self.rel0 = nn.ReLU()
        self.rel1 = nn.ReLU()
        self.drop = nn.Dropout(0.3)
        self.sig = nn.Sigmoid()
    
    def forward(self, x):
        x = self.fc0(x)
        x = self.rel0(x)
        x = self.fc1(x)
        x = self.rel1(x)
        x = self.drop(x)
        x = self.fc2(x)
        x = self.sig(x)
        
        return x

#training our neural network
def training(device, train_loader, valid_loader, model, criterion, optimizer, n_epochs = 75):

    train_losses, valid_losses = [], []
      # initialize tracker for minimum validation loss
    valid_loss_min = np.Inf  # set initial "min" to infinity

    for epoch in range(n_epochs):
        train_loss, valid_loss = 0, 0 # monitor losses

          # train the model
        model.train() # prepare model for training
        for data, label in train_loader:
            data = data.to(device=device, dtype=torch.float32)
            label = label.to(device=device, dtype=torch.float32)
            optimizer.zero_grad() # clear the gradients of all optimized variables
            output = model(data)
            loss = criterion(output, label.reshape(-1,1))# calculate the loss
            loss.backward() # backward pass: compute gradient of the loss with respect to model parameters
            optimizer.step() # perform a single optimization step (parameter update)
            train_loss += loss.item() * data.size(0) # update running training loss

          # validate the model
        model.eval()
        for data, label in valid_loader:
            data = data.to(device=device, dtype=torch.float32)
            label = label.to(device=device, dtype=torch.float32)
            ones = torch.ones(label.shape).to(device=device)
            zeros = torch.zeros(label.shape).to(device=device)
            with torch.no_grad():
                output = model(data)
                output = torch.where(output>0.5, ones, zeros)
            loss = criterion(output,label.reshape(-1,1))
            valid_loss += loss.item() * data.size(0)

          # calculate average loss over an epoch
        train_loss /= len(train_loader.sampler)
        valid_loss /= len(valid_loader.sampler)
        train_losses.append(train_loss)
        valid_losses.append(valid_loss)

        # save model if validation loss has decreased
        if valid_loss <= valid_loss_min:
            torch.save(model.state_dict(), 'model.pt')
            valid_loss_min = valid_loss

    return train_losses, valid_losses      

def evaluation(device, model, test_loader, criterion) -> str:

    eval_string = """"""
  # initialize lists to monitor test loss and accuracy
    test_loss = 0.0
    class_correct = list(0. for i in range(2))
    class_total = list(0. for i in range(2))

    model.eval() # prepare model for evaluation
    for data, label in test_loader:
        data = data.to(device=device, dtype=torch.float32)
        label = label.to(device=device, dtype=torch.float32)
        ones = torch.ones(label.shape).to(device=device)
        zeros = torch.zeros(label.shape).to(device=device)
        with torch.no_grad():
            output = model(data)
            output = torch.where(output>0.5, ones, zeros)# forward pass: compute predicted outputs by passing inputs to the model
        loss = criterion(output, label.reshape(-1,1))
        test_loss += loss.item()*data.size(0)
        _, pred = torch.max(output, 1) # convert output probabilities to predicted class
        correct = (np.squeeze(output.eq(label.data.view_as(output)))).cpu().numpy()# compare predictions to true label
        # calculate test accuracy for each object class
        for i in range(len(label)):
            digit = int(label[i].cpu().detach().numpy())
            class_correct[digit] += (1 if correct[i] else 0)
            class_total[digit] += 1

    # calculate and print avg test loss
    test_loss = test_loss/len(test_loader.sampler)
    eval_string += 'test Loss: {:.6f}\n'.format(test_loss)
    for i in range(2):
        eval_string += '\ntest accuracy of %1s: %2d%% (%2d/%2d)' % (str(i), 100 * class_correct[i] / class_total[i], np.sum(class_correct[i]), np.sum(class_total[i]))
    eval_string += '\ntest accuracy (overall): %2.2f%% (%2d/%2d)' % (100. * np.sum(class_correct) / np.sum(class_total), np.sum(class_correct), np.sum(class_total))
    return eval_string

def mlp(dataframe) -> str:
    
    to_print = """"""

    n_epochs = 75
    train_loader, valid_loader, test_loader, shape = dataframe_to_dataloaders(dataframe)
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    model_MLP = MLP(shape, 100, 100, 1)
    model_MLP.to(device=device)

    criterion = nn.BCELoss() # specify loss function 
    optimizer = torch.optim.Adam(model_MLP.parameters(), lr = 0.01)

    train_losses, valid_losses = training(device, train_loader, valid_loader, model_MLP, criterion, optimizer, n_epochs)

    fig, ax = plt.subplots()
    ax.plot(range(n_epochs), train_losses)
    ax.plot(range(n_epochs), valid_losses)
    ax.legend(['train', 'validation'], prop={'size': 10})
    plt.title('loss function', size=10)
    plt.xlabel('epoch', size=10)
    plt.ylabel('loss value', size=10)

    to_print += get_html_from_fig(fig)
    plt.close(fig)

    model_MLP.load_state_dict(torch.load('model.pt', map_location=device))

    to_print += evaluation(device, model_MLP, test_loader, criterion)

    return to_print