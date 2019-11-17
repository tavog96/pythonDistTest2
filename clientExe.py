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
    cluster = dispy.JobCluster(wordCounting)
    # run 'compute' with 20 random numbers on available CPUs
    folderName = "files"
    jobs = []
    filesController = TextFileController( './' + folderName)
    files = filesController.filesNamesScan()
    for fileName in files:
        fileContent = filesController.readFileContent(fileName)
        job = cluster.submit(fileContent)
        jobs.append(job)
    # cluster.wait() # waits until all jobs finish
    generalCounter = 0
    for job in jobs:
        count = job() # waits for job to finish and returns results
        generalCounter = count + generalCounter
        # other fields of 'job' that may be useful:
        # job.stdout, job.stderr, job.exception, job.ip_addr, job.end_time
    print ("RESULTADO: Se han contado un total de " + str(generalCounter) + " palabras.")
    cluster.print_status()  # shows which nodes executed how many jobs etc.
    tiempoFinal = datetime.datetime.now()
    print(str(tiempoFinal))
    diferenciaTiempo = tiempoFinal - tiempoInicial
    print("La tarea total duro " + str(diferenciaTiempo.total_seconds()) + " segundos.")