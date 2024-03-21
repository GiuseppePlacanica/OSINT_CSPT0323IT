import xml.etree.ElementTree as ET
import sys, getopt, csv, os, re, datetime
from bs4 import BeautifulSoup


def parsInput(argv): #funzione che stabilisce il parsing della linea di comando

    target = str(sys.argv[1]) #ip target
    filename = ''
    flagexists = 1
    delay = 0
    dpath = os.getcwd()

    try:
        opts, args = getopt.getopt(sys.argv[2:], "o:vrpd:h", ["output", "verbose", "refresh", "proxy", "delay", "help"]) #definiamo i comandi possibili. Quelli con : richiedono un argomento
        for opt, arg, in opts: #loop per l'intero input utente

            if opt == '-o': #selezionata opzione output
                print("Output selection " + arg)
                filename = arg
                filename = re.sub("<*|>*|:*|,*|\\*|/*|!*|", "", filename)  # bonifichiamo l'input da caratteri che gli OS snobbano. Missing '?' because of some metacharacter bs
                try:
                    f = open(dpath + "\\" + filename, 'w')  # join path with filename

                except FileExistsError:  # if file exists, add a counter to the filename until it's unique
                    while flagexists > 0:
                        print("It looks like a file of the same name already exists. Autorenaming...")
                        try:
                            filename.replace(".", str(flagexists) + ".")
                            f = open(dpath + "\\" + filename, 'w')
                            break
                        except FileExistsError:
                            flagexists += 1

                except FileNotFoundError:  # if data path validation is wrong we default the option
                    print("You must produce a valid path and filename to continue. Defaulting...")
                    datanow = str(datetime.datetime.now())
                    datanow = datanow.replace(":", "_").replace(" ", "___")
                    datanow = datanow.split('.', 1)[0]
                    filename = "RA" + datanow
                    f = open(dpath + "\\" + filename, 'w')

                if "txt" in filename:
                    print("famo un txt, alziamo flag per le scritture ma probabilmente nulla di strano da fare")
                elif "csv" in filename:
                    print("famo un csv ma bisogna definire la struttura prima")
                elif "html" in filename:
                    print("famo un html ma bisogna definire la struttura prima")
                else:
                    print("default at standard text")
            elif opt == '-v':
                print("verbose selection, ma non so che c'è da mettere qui per ora ")
            elif opt == '-r':
                print("refresh, non so che vuol dire")
            elif opt == '-p':
                print("proxy, non so che vuol dire")

            elif opt == '-d':
                print("delay")
                try:
                    delay = float(arg)
                except ValueError:
                    print("Looks like you inserted an invalid delay, defaulting to 2 seconds...")
                    delay = 2

    except getopt.GetoptError as optionErrors:
        print("Selezione errata o errore input " + optionErrors)
        sys.exit()

    print("The address is " + target)
    print(len(sys.argv))
    return target #???



def parsXML(): #TODO Parsing dell'xml. Replicare o cambiare struttura.
    tree = ET.parse('tekdefense.xml')
    root = tree.getroot()
    for x in root.findall('site'):
        domain = x.find('domainurl').text
        print(domain)






parsInput(sys.argv)
parsXML()




