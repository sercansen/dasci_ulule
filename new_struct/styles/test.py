
import pdfkit
string_to_print = """
                        <h1>Titre</h1>
                        <p>Retest</p>
                        <div class="test">
                            b
                            <p>Test</p>
                        </div>
                        <test>
                            testtesttest
                        </test>
                    """
pdfkit.from_string(string_to_print, './out.pdf',
                   css="./new_struct/styles/styles.css")
