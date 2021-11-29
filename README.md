# dasci_ulule

## Utilisation du programme

Pour lancer le programme il suffit d'exécuter le fichier main.py. Si l'on souhaite ne pas avoir d'affichage pour augmenter la vitesse d'exécution, il suffit de changer `main(display_explanations=True)` en `main(display_explanations=False)`, toujours dans le fichier main.py. Le fichier principal se charge d'appeler les différentes fonction de lecture de CSV, de nettoyage des données etc.

Les résultats sont affichés dans le fichier `out.pdf`. Les styles des éléments affichés dans ce pdf sont contrôlés dans le fichier `styles.css`.

## Modification du programme

Pour rajouter un paragraphe de texte, penser à utiliser les balises `<p>` et `</p>` autour dudit paragraphe. Pour un titre principal, ce sont les balises `<h1>` et `</h1>`. Pour un sous-titre, les balises `<h2>` et `</h2>`, etc. Pour ajouter un graphe, la fonction `get_html_from_fig` dans le fichier `/utils/utils.py` se charge de l'affichage, il faut juste l'ajouter à une chaîne de caractère.

## Pistes d'évolution

Il pourrait être intéressant d'envisager un approche plus "objet". Par exemple une classe pour chaque feature, qui contiendrait différentes méthodes, utilisant l'héritage.
