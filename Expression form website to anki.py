"""
Note:
In the 1545 expressions, one has a different page presentation :
http://www.expressio.fr/expressions/dans-les-vapes.php

And another one has this : « белые ночи »
http://www.expressio.fr/expressions/une-nuit-blanche.php

So I can't do what I want on them
You must delete it manualy from the "websites.txt"


You can add them manually in AnkiFile with this line :
Quel est l'origine et le sens de : Une nuit blanche ?@ Signification : <br>Une nuit sans sommeil<br><br>Origine : <br>Autant vous l'avouer tout de suite : il n'existe aucune certitude quant à l'origine de cette expression qui date du XVIIIe siècle. Et pourtant, vu la taille du texte ci-dessous, il y a quand même des choses à en dire.<br><br> On en trouve une attestation en date du 30 octobre 1771 dans une lettre de la marquise du Deffand, Marie de Vichy-Chamrond alors âgée de 74 ans, à l'homme politique et écrivain anglais Horace Walpole. Elle y écrit ceci : « Vous saurez que j'ai passé une nuit blanche, mais si blanche, que depuis deux heures après minuit que je me suis couchée, jusqu'à trois heures après-midi que je vous écris, je n'ai pas exactement fermé la paupière ; c'est la plus forte insomnie que j'ai jamais eue. » <br>Comme il ne semble pas exister de traces antérieures dans la littérature française, certains auteurs émettent l'hypothèse que c'est elle qui a inventé ce terme. Mais comme on le trouve dans d'autres ouvrages postérieurs moins d'un an et demi après (voir l'exemple), il n'est pas certain que cela soit le cas.<br><br>L'idée la moins originale mais peut-être la plus véridique est la simple opposition avec la nuit noire, celle où, en temps normal, on dort d'un sommeil généralement bien mérité, une nuit passée en restant éveillé étant alors une nuit blanche, soit par constraste, soit parce qu'on la passe avec une lumière allumée.<br>Pour le confirmer, il suffit de se souvenir qu'en français, le qualificatif blanc désigne souvent un manque. Ainsi, un mariage blanc, un examen blanc, un tir à blanc ou encore une voix blanche, par exemple.<br>Bien entendu, on peut trouver quelques autres explications, en particulier sur Internet où la plus répandue, et certainement la plus fausse, évoque les chevaliers qui, la nuit précédant leur adoubement, devaient la passer éveillés dans une tenue entièrement blanche. Mais si cette explication était la bonne, il faudrait expliquer pourquoi il a alors fallu attendre la deuxième moitié du XVIIIe siècle pour trouver la première trace écrite de cette expression, plusieurs siècles après cette coutume de chevalerie.<br><br>Toutefois, une autre hypothèse, nettement plus vraisemblable, cette fois, car elle respecte la chronologie, nous vient de Saint-Pétersbourg, en Russie. À l'époque du règne d'Élisabeth, puis de Catherine II, la cour royale dans cette ville - qui je le rappelle, était alors la capitale du pays - était fréquentée par de nombreux Français, en été principalement. Or, à cette époque de l'année et à cette latitude, les nuits sont loin d'être vraiment noires, le soleil ne se couchant jamais complètement.<br>Et dans ces années-là, tradition perpétuée actuellement par le festival des Nuits Blanches de Saint-Pétersbourg, la vie « nocturne » battait son plein. Autant dire que ceux qui participaient aux bals et autres fêtes tardives, passaient des nuits doublement blanches à la fois, par l'absence de sommeil et par la luminosité de la nuit.<br>Il se peut donc tout-à-fait que le terme russe « белые ночи » (nuits blanches) ait été ramené et popularisé chez nous par les Français qui passaient du bon temps là-bas.
"""

import codecs

###Initialization
def GetPageWithExpression():
    """
    Get the html of the main page which list all the expressions
    """
    link = "http://www.expressio.fr/toutes_les_expressions.php"

    myfile = OpenUrl(link)

    return myfile


def SaveUrls(wblist):
    """
    Save the urls
    """
    writingFile = open("websites.txt", "r")
    for wb in wblist:
        writingFile.write(wb + "\n")
    writingFile.close()


def GetUrls():
    """
    Get urls from the html code of the main page which have been a little bit
    modified to make things easier (I have deleted the head part of the html code)
    """
    firstWebSite = OpenFile("Expression Website.txt")

    i = 0
    wblist = []
    while i < len(firstWebSite):
        wb = ""

        if firstWebSite[i] == "\"":
            i+=1
            while firstWebSite[i] != "\"":
                wb += firstWebSite[i]
                i+=1
            wblist.append("http://www.expressio.fr/" + wb)

        i +=1

    SaveUrls(wblist)


###Recuperation of the content of an url
def GetUrlsFromFile(file):
    """
    Get the list of urls save in file
    """
    wblist = OpenFile(file).split("\n")
    wblist.pop()

    return wblist


def OpenFile(file):
    """
    Open a file...
    """
    tempo = open(file, "r")
    text = str(tempo.read())
    tempo.close()

    return text


def OpenUrl(url):
    """
    Get the Html code of the url
    """
    from urllib.request import urlopen
    f = urlopen(url)
    htmlPage = str(f.read())
    f.close()

    return htmlPage


def GetTextFromHtml(htmlPage, index, start, end):
    """
    Get the text between the start and the end
    """
    text = ""
    while start != htmlPage[index : index + len(start)]:
        index += 1

    index += len(start)

    while end != htmlPage[index : index + len(end)]:
        text += htmlPage[index]
        index += 1

    return text


def GetExpression(htmlPage, index):
    """
    Get the expression in the Html page
    """
    ExpressionStart = "<h1 id=\"expression\">"
    ExpressionEnd = "</h1>"

    expression = GetTextFromHtml(htmlPage, index, ExpressionStart, ExpressionEnd)

    return expression


def GetTraduction(htmlPage, index):
    """
    Get the traduction of the expression in the html page
    """
    TraductionStart = "<h2 id=\"signification\">"
    TraductionEnd = "</h2>"

    traduction = GetTextFromHtml(htmlPage, index, TraductionStart, TraductionEnd)

    return traduction


def GetOrigine(htmlPage, index):
    """
    Get the origine of the expression in the html page
    """
    OrigineStart = "<p id=\"origine\">"
    OrigineEnd = "</p>"

    origine = GetTextFromHtml(htmlPage, index, OrigineStart, OrigineEnd)

    return origine


def GetText(url):
    """
    Get the expression and its origin from a url
    """
    htmlPage = OpenUrl(url)
    index = 0

    expression = Clean(GetExpression(htmlPage, index))
    traduction = Clean(GetTraduction(htmlPage, index))
    origine = Clean(GetOrigine(htmlPage, index))

    return expression, traduction, origine


def DeleteShit(text):
    """
    Removes HTML tags
    """
    newText =""

    length = len(text)
    i = 0
    while i < length:
        while i < length and text[i] == "<":
            i += 1
            while text[i] != ">":
                i+=1
            i += 1

        if i < length:
            newText += text[i]
        i+= 1

    return newText


def Clean(text):
    """
    Clean the text from any html residue
    """
    import html

    return DeleteShit(html.unescape(text.replace('\n', '').replace('\\', '')))


###Testing
def CopyUrlContent(url):
    """
    analyzing a typic expression page
    """
    text = openUrl(url)
    expressionSite = open("Expression Site.txt", "a")
    expressionSite.write(text)
    expressionSite.close()


###Main
"""Création de AnkiFile"""
import time
time.sleep(2)
print("starting")
with codecs.open("AnkiFile.txt", "a", "utf-8") as AnkiFile:
    wblist = GetUrlsFromFile("websites.txt")

    i = 0
    for wb in wblist:
        expression, traduction, origine = GetText(wb)
        AnkiFile.write("Quel est l'origine et le sens de : " + expression + " ?@ Signification : <br>" + traduction + "<br><br>Origine : <br>" + origine + "\n")

        #Stats
        i+=1
        print(str(i) + " websites done")
        print(wb)
        print("This is : " + str("%.3f" % (i/len(wblist) * 100)) + "%")


print(f"{len(wblist)} cartes Anki ont du etre ajoutees" )
# print(Clean("""Quel est l'origine et le sens de : X au jus / C\'est du peu au jus ?@ Signification : <br>Plus que x jours avant la fin / Il n\'y en a plus que pour quelques jours avant la fin<br><br>Origine : <br>Ceux qui ont eu l\'immense plaisir de faire leur service militaire (je vous parle l&agrave; d\'un temps... <a href="http://www.paroles.net/charles-aznavour/paroles-la-boheme" target="_blank"><img src="lien.gif" border="no" alt="Lien externe" title="Lien externe"></a>) connaissent bien le fameux &laquo; z&eacute;ro ! &raquo; abr&eacute;viation de &laquo; z&eacute;ro au jus ! &raquo;, le joyeux cri qu\'ils poussaient au dernier jour de leur service enfin termin&eacute;.<br />Mais ce &laquo; z&eacute;ro &raquo; avait bien souvent &eacute;t&eacute; pr&eacute;c&eacute;d&eacute; d\'autres annonces au nombre d&eacute;croissant (comme &laquo; soixante au jus &raquo; ou &laquo; huit au jus &raquo;) au fur et &agrave; mesure que <a href="http://www.expressio.fr/expressions/la-quille.php" target="_blank">la quille</a> se rapprochait.<br />Alors pourquoi ce <i>jus</i> pour d&eacute;signer un nombre jours ?<br /><br />Eh bien c\'est pour une raison simple : en argot, le mot <i>jus</i> d&eacute;signe le caf&eacute;. Et dans le cas qui nous int&eacute;resse, c\'est plus pr&eacute;cis&eacute;ment celui du petit d&eacute;jeuner, ce caf&eacute; qui rythme le d&eacute;but de chaque journ&eacute;e. Autrement dit, symboliquement, le nombre de jus d&eacute;signe le nombre de jours.<br />D\'ailleurs, il &eacute;tait fr&eacute;quent que le r&eacute;veil d\'une chambr&eacute;e par un grad&eacute; se fasse par un &laquo; au jus l&agrave; d\'dans ! &raquo; pour indiquer qu\'il &eacute;tait temps d\'aller fissa prendre son petit-d&eacute;jeuner avant de passer aux r&eacute;elles et sympathiques activit&eacute;s militaires.<br /><br />Sortie du service militaire, cette expression peut aussi s\'employer dans d\'autres situations o&ugrave; l\'on d&eacute;compte un nombre de jours restants comme, par exemple, lorsqu\'un employ&eacute; va quitter sa soci&eacute;t&eacute; et qu\'il lui reste quelques jours avant son d&eacute;part ou lorsqu\'un prisonnier n\'est plus tr&egrave;s loin de sa lib&eacute;ration.<br /><br />Pour les curieux, car je sais qu\'il y en a quelques-uns dans la salle, le terme <i>jus</i> est une abr&eacute;viation de &laquo; jus de chique (le tabac noir &agrave; m&acirc;cher) &raquo; ou &laquo; jus de chaussette &raquo;, ces liquides tr&egrave;s peu app&eacute;tissants auxquels le mauvais caf&eacute; pouvait &ecirc;tre compar&eacute;."""))
