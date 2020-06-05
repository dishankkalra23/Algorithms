import pandas as pd

arrivalTime = list(map(int, input('Enter the Arrival time of processes: ').split()))
burstTime = list(map(int, input('Enter the Burst time of processes: ').split()))

duplicateBurstTime = burstTime.copy()  # .copy so that duplicateBT is not changed

actualAT = [-1] * len(arrivalTime)

actualCT = [0] * len(arrivalTime)

currentArrival = 0

ganttChartTime = []
ganntChartProcess = []

while sum(burstTime) != 0:
    # print("currentTime: ", currentArrival)
    burstList = []  # Removing existing burst time
    arrivalList = []

    for i in range(len(arrivalTime)):
        if arrivalTime[i] <= currentArrival and burstTime[i] > 0:
            arrivalList.append(arrivalTime[i])
            # print(arrivalList)
            burstList.append(burstTime[i])
        # print("burstList: ", burstList)

    currentBurst = 0  # To get maximum current Burst Time
    if len(burstList) != 0:
        currentBurst = max(burstList)
        burstIndex = burstTime.index(currentBurst)
        # print("BurstIndex: ", burstIndex)

        if burstTime[burstIndex] > 0:
            burstTime[burstIndex] -= 1
        # print("BurstTime: ", burstTime)

        if actualAT[burstIndex] == -1:
            actualAT[burstIndex] = currentArrival
        # print("AT: ", actualAT)

        completionTime = currentArrival + 1

        if burstTime[burstIndex] == 0:  # None of the process can end at 0 sec
            actualCT[burstIndex] = completionTime

        ganttChartTime.append(currentArrival)
        ganntChartProcess.append("Process " + str(burstIndex + 1))

    elif len(burstList) == 0:
        ganttChartTime.append(currentArrival)
        ganntChartProcess.append('CPU is Idle')
    currentArrival += 1

TAT = []
WaitingTime = []
ResponseTime = []
RelativeDelay = []
process = []

for j in range(len(arrivalTime)):
    TAT.append(actualCT[j] - arrivalTime[j])
    ResponseTime.append(actualAT[j] - arrivalTime[j])

for k in range(len(arrivalTime)):
    WaitingTime.append(TAT[k] - duplicateBurstTime[k])

for i in range(len(arrivalTime)):
    RelativeDelay.append(TAT[i] / duplicateBurstTime[i])

for i in range(1, len(arrivalTime) + 1):
    process.append("P" + str(i))

ghanttchartResult = {'Process Executing': ganntChartProcess, 'Time': ganttChartTime}
print(pd.DataFrame(data=ghanttchartResult))

result = {'Process': process, 'Arrival Time': arrivalTime, 'Burst Time': duplicateBurstTime, 'TAT': TAT,
          'Waiting Time': WaitingTime, 'Response Time': ResponseTime, 'Relative Delay': RelativeDelay}
print(pd.DataFrame(data=result))

print("Average Turn Around Time: ", sum(TAT) / len(arrivalTime), " units")
print("Average Waiting Time: ", sum(WaitingTime) / len(arrivalTime), " units")
print("Average Response Time: ", sum(ResponseTime) / len(arrivalTime), " units")
print("Average Relative Delay: ", sum(RelativeDelay) / len(arrivalTime), " units")
