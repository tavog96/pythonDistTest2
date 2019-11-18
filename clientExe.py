
def wordCounting(text):  ##Funcion que ejecuta la tarea (Aca de define)
    import re
    wordList = re.sub("[^\w]", " ",  text).split()
    return (len(wordList))



if __name__ == '__main__':

    import dispy ## Se importa la herramienta
    from infrastructure.textFileController import TextFileController
    import datetime, time

    cluster = dispy.JobCluster(wordCounting) ## Se inicia la herramienta, busca nodos en LAN, define la tarea
    time.sleep(4) ## Espera a que los nodos de LAN respondan todos
    
    folderName = "files"
    jobs = []
    filesController = TextFileController( './' + folderName)
    files = filesController.filesNamesScan() ## Se detecta/obtiene el nombre de todos los archivos en la carpeta FILES, se guardan en una lista

    tiempoInicial = datetime.datetime.now() ## Inicia el conteo del tiempo de ejecucion
    print("Inicio: " + str(tiempoInicial))
    for fileName in files:
        fileContent = filesController.readFileContent(fileName) ## Se lee cada archivo
        job = cluster.submit(fileContent) ## Se envia el contenido de cada archivo, a cada nodo, para contar sus palabras
        jobs.append(job) ## Se guarda una referencia de cada nodo trabajando

    generalCounter = 0 ## Contador general de palabras

    for job in jobs:
        job() ## Se espera a que cada proceso termine
        generalCounter = job.result + generalCounter
    tiempoFinal = datetime.datetime.now() ## Se toma el tiempo final de ejecucion
    print("Final: "+str(tiempoFinal))
    print ("RESULTADO: Se han contado un total de " + str(generalCounter) + " palabras.")
    cluster.print_status() ## Se imprime el reporte de los nodos

    diferenciaTiempo = tiempoFinal - tiempoInicial ## Se calcula el total de tiempo de ejecucion
    print("La tarea total duro " + str(diferenciaTiempo.total_seconds()) + " segundos.")