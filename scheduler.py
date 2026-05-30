import argparse
import random
from operator import itemgetter

parser = argparse.ArgumentParser()

parser.add_argument("-c", "--compute", action="store_true", default=False)
parser.add_argument("-s", "--seed", action="store")
parser.add_argument("-p", "--policy", action="store")
parser.add_argument("-j", "--jobs", action="store")
parser.add_argument("-m", "--maxlen", default=10, action="store")
parser.add_argument("-q", "--quantum", default=1, action="store")

args = parser.parse_args()
print("\n")
print("Policy:", args.policy)
print("Seed: ", args.seed)
print("Maxlen: ", args.maxlen)
print("Total Jobs", args.jobs)
print("\n")

random.seed(args.seed, version=2)

joblist = []
for jobnum in range(0, int(args.jobs)):
    runtime = int(args.maxlen * random.random() + 1)
    joblist.append([jobnum, runtime])
    print("Job: ", jobnum, " Runtime: ", runtime)

print("\n")

if(args.compute):
    if(args.policy == "SJF"):
        joblist = sorted(joblist, key=itemgetter(1))


        temp = 0.0
        waitsum = 0.0
        responsesum = 0.0
        turnaroundsum = 0.0
        for job in range(0, len(joblist)):
            jobno = joblist[job][0]
            runtime = joblist[job][1]
            print("Job ", joblist[job][0], " running for ", joblist[job][1], " from ", temp, " to ", temp + runtime)
            turnaround = temp + runtime
            response = temp 
            wait = temp

            waitsum += wait
            responsesum += response
            turnaroundsum += turnaround
            temp += runtime
        print("average responce : ", responsesum/len(joblist), " average turnaround: ", turnaroundsum/len(joblist), " average wait: ", waitsum/len(joblist))

    if(args.policy == "FIFO"):
        temp = 0.0
        waitsum = 0.0
        responsesum = 0.0
        turnaroundsum = 0.0
        for job in range(0, len(joblist)):
            jobno = joblist[job][0]
            runtime = joblist[job][1]
            print("Job ", joblist[job][0], " running for ", joblist[job][1], " from ", temp, " to ", temp + runtime)
            turnaround = temp + runtime
            response = temp 
            wait = temp

            waitsum += wait
            responsesum += response
            turnaroundsum += turnaround
            temp += runtime
        print("average responce : ", responsesum/len(joblist), " average turnaround: ", turnaroundsum/len(joblist), " average wait: ", waitsum/len(joblist))
        print("\n")

    if(args.policy == "RR"):
        turnaround = [0] * len(joblist)
        response = [-1] * len(joblist)
        wait = [0] * len(joblist)
        lastran = [0] * len(joblist)
        quantum = float(args.quantum)
        jobcount = len(joblist)
        thetime = 0.0
        count = len(joblist)
        while jobcount > 0:
            job = joblist.pop(0)
            jobnum  = job[0]
            runtime = float(job[1])
            if response[jobnum] == -1:
                response[jobnum] = thetime
            currwait = thetime - lastran[jobnum]
            wait[jobnum] += currwait
            if runtime > quantum:
                runtime -= quantum
                ranfor = quantum
                print('  [ time %3d ] Run job %3d for %.2f secs' % (thetime, jobnum, ranfor))
                joblist.append([jobnum, runtime])
            else:
                ranfor = runtime;
                print('  [ time %3d ] Run job %3d for %.2f secs ( DONE at %.2f )' % (thetime, jobnum, ranfor, thetime + ranfor))
                turnaround[jobnum] = thetime + ranfor
                jobcount -= 1
            thetime += ranfor
            lastran[jobnum] = thetime

        print('\nFinal statistics:')
        turnaroundSum = 0.0
        waitSum       = 0.0
        responseSum   = 0.0
        for i in range(0,count):
            turnaroundSum += turnaround[i]
            responseSum += response[i]
            waitSum += wait[i]
            print('  Job %3d -- Response: %3.2f  Turnaround %3.2f  Wait %3.2f' % (i, response[i], turnaround[i], wait[i]))

        
        print('\n  Average -- Response: %3.2f  Turnaround %3.2f  Wait %3.2f\n' % (responseSum/count, turnaroundSum/count, waitSum/count))






