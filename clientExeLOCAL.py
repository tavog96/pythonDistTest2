# function 'compute' is distributed and executed with arguments
# supplied with 'cluster.submit' below
def wordCounting(text):
    import re
    wordList = re.sub("[^\w]", " ",  text).split()
    return (len(wordList))

if __name__ == '__main__':
    # executed on client only; variables created below, including modules imported,
    # are not available in job computations
    import dispy
    from infrastructure.textFileController import TextFileController
    import datetime

    tiempoInicial = datetime.datetime.now()
    print(str(tiempoInicial))
    # distribute 'compute' to nodes; in this case, 'compute' does not have
    # any dependencies to run on nodes
    # run 'compute' with 20 random numbers on available CPUs
    folderName = "files"
    filesController = TextFileController( './' + folderName)
    files = filesController.filesNamesScan()
    generalCounter = 0
    for fileName in files:
        fileContent = filesController.readFileContent(fileName)
        generalCounter = generalCounter + wordCounting(fileContent)

    print ("RESULTADO: Se han contado un total de " + str(generalCounter) + " palabras.")
    tiempoFinal = datetime.datetime.now()
    print(str(tiempoFinal))
    diferenciaTiempo = tiempoFinal - tiempoInicial
    print("La tarea total duro " + str(diferenciaTiempo.total_seconds()) + " segundos.")