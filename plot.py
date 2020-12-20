import os
import matplotlib.pyplot as plt
import numpy
import time

results = {}

def runInputDeck():
    global results
    ministatPaths = ["/home/aidrisy/1_thread","/home/aidrisy/2_thread","/home/aidrisy/4_thread",
                    "/home/aidrisy/6_thread","/home/aidrisy/8_thread","/home/aidrisy/12_thread",
                    "/home/aidrisy/16_thread","/home/aidrisy/ministat","/home/aidrisy/microOpt"]
    inputFilesPath = "~/ccny59866/inputFiles"

    #"/home/aidrisy/microOpt"
        
    files = os.listdir("inputFiles")
    for path in ministatPaths:
        os.chdir(path)
        print(f"CWD Changed to :: {os.getcwd()}")
        results[path] = {}
        for x in files:
            iFile = os.path.join(inputFilesPath,x)
            start = time.time()
            os.system(f"./ministat -q {iFile}")
            end = time.time()
            elapsed = end - start
            print(f"Time elapsed for {iFile} = {elapsed}")
            results[path][int(x)] = elapsed
    
    print(results)

def sortAndPlot():
    global results
    plotTimes = []
    labels = []
    for d in results:
        subDict = results[d]
        print(d)
        labels.append(d)
        keys = list(subDict.keys())
        keys.sort()
       # print(f"Keys = {keys}")
        row = []
        for k in keys:
            row.append(subDict[k])
        print(f"Row = {row}")
        plotTimes.append(row)

    print("---")

    diffs = []
    for i in range(0,len(plotTimes[0])):
        # Custom - stock
        delta = plotTimes[0][i] - plotTimes[1][i]
        diffs.append(delta)

    print(f"Difs = {diffs}")

    plt.figure(figsize=(15,10))
    plt.title("||-Ministat vs µ-Opt-Ministat vsStock-Ministat")
    plt.xlabel("Size of file in ints")
    plt.ylabel("Running Time (Secs)")
    for i in range(0,len(plotTimes)):
        plt.plot(keys,plotTimes[i],'x--',label=labels[i])
    plt.legend(loc="upper left")
    plt.savefig("parallel_vs_micro_vs_stock.png")


def main():
    runInputDeck()
    os.chdir("/home/aidrisy/ccny59866")
    print(f"CWD Changed to :: {os.getcwd()}")
    sortAndPlot()
main()