import argparse
import random


parser = argparse.ArgumentParser()

parser.add_argument("-s", "--seed", action="store", default=10)
parser.add_argument("-n", "--numQueues", action="store", default=3)
parser.add_argument("-q", "--quantum", action="store", default=10)
parser.add_argument("-a", "--allotment", action="store", default=1)
parser.add_argument("-j", "--numJobs", action="store", default=3)
parser.add_argument("-m", "--maxLen", action="store", default=100)
parser.add_argument("-M", "--maxIO", action="store", default=10)
parser.add_argument("-B", "--boost", action="store_true", default=False)
parser.add_argument("-i", "--ioTime", action="store", default=5)
parser.add_argument("-c", "--compute", action="store_true", default=False)
parser.add_argument("-S", "--stay", action="store_true", default=False)
parser.add_argument("-I", "--iobump", action="store_true", default=False)
# parser.add_argument("-l", "--jlist", action="store_true", default=False)
args = parser.parse_args()

random.seed(args.seed, version=2)

print("\n")

print("Here is the list of inputs:\n")
print("OPTIONS jobs: ", args.numJobs)
print("OPTIONS queues 3: ", args.numQueues)
print("OPTIONS jobs: ", args.numJobs)
for queue in range(0, int(args.numQueues)):
    print("OPTIONS allotments for queue ", queue, " is: ", args.allotment)
    print("OPTIONS quantum length for ", queue, "is: ", args.quantum)
print("OPTIONS boost: ", args.boost)
print("OPTIONS ioTime ", args.ioTime)
print("OPTIONS stayAfterIO ", args.stay)
print("OPTIONS iobump ", args.iobump)

print("\n")

joblist = []
iotime = int(args.ioTime)

for jobnum in range(0, int(args.numJobs)):
    runtime = int(args.maxLen * random.random() + 1)
    IOfreq = int(args.maxIO * random.random() + 1)
    joblist.append([jobnum, runtime, IOfreq])
    print("Job: ", jobnum, " Runtime: ", runtime, " IO Freq: ", IOfreq)

print("\n")

if(args.compute):
    queues = []
    for queue in range(0, int(args.numQueues)):
        queues.append([])
    
    hiqueue = len(queues)-1

    for job in range(0, int(args.numJobs)):
        queues[hiqueue].append(joblist[job])
    
    jobcount = int(args.numJobs)

    checkIO = [0] * jobcount
    trackAllotSlices = [int(args.allotment)] * jobcount
    trackIO = []
    trackRT = []

    for job in range(0, jobcount):
        trackRT.append(joblist[job][1])
    
    time = 0
    quantum = int(args.quantum)
    while(jobcount):
        for q in range(len(queues)-1, -1, -1):
            if(len(queues[q]) > 0):
                hiqueue = q
                break
        
        currjob = queues[hiqueue][0][0]
        runtime = trackRT[currjob]
        IOfreq = queues[hiqueue][0][2]

        # hiqueue.pop(0)

        if(runtime <= 0):
            jobcount -= 1
            continue

        time += 1
        trackRT[currjob] -= 1
        checkIO[currjob] += 1
        quantum -= 1

        if quantum == 0:
            quantum = int(args.quantum)
            queues[hiqueue].pop(0)
            

        print("TIME ", time, " Job ", currjob, " runtime: ", trackRT[currjob], " IO in: ", checkIO[currjob])

        if(checkIO[currjob] == IOfreq):
            if(hiqueue > 0):
                trackIO.append([currjob, hiqueue-1, iotime])
            else:
                trackIO.append([currjob, hiqueue, iotime])
            queues[hiqueue].pop(0)
            checkIO[currjob] = -1
            print("Job ", job, " gets IO")
        
        for i in range(0, len(trackIO)):
            if(i >= len(trackIO)):
                break
            iojob = trackIO[i][0]
            trackIO[i][2] -= 1 #remaining IO time
            if(trackIO[i][2] == 0):
                nextqueue = trackIO[i][1]
                queues[nextqueue].append(joblist[iojob])
                trackIO.pop(i)
                checkIO[iojob] = 0
                print("Job ", iojob, " IO done")
            
        if((len(queues[hiqueue]) > 0 and queues[hiqueue][0][1] - trackRT[currjob])/int(args.quantum) >= int(args.allotment)):
            if(hiqueue > 0):
                queues[hiqueue-1].append([currjob, runtime, IOfreq])
            else:
                queues[hiqueue-1].append([currjob, runtime, IOfreq])
            queues[hiqueue].pop(0)
            if(hiqueue > 0):
                finalpriority = hiqueue-1
            else:
                finalpriority = hiqueue
            print("Job: ", currjob, " priority decreased from ", hiqueue, " to ", finalpriority)

