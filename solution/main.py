from profitFunc import *
def main():
    cases = readCases('test.txt')
    #all input, in form of list:['1', '3231', '3', '3121', '212', '214', '0']
    i = 0
    caseIndex = 0
    while cases[i] != '0':
        caseIndex += 1
        #the number of case
        maxProfit = 0
        totalOrder = list()
        #new a list for storing the trunk order for each sawmills
        print('Case: {}'.format(caseIndex))
        for j in range(int(cases[i])):
            #iterate all trunk sets
            currentTrunks = list(cases[i + j + 1][1:])
            #for sample, the first currentTrunk set is ['2','3','1']
            for s in range(len(currentTrunks)):
                currentTrunks[s] = int(currentTrunks[s])
            #convert each trunk length from string to int
            bestOrder = bestProfitSets(currentTrunks)
            totalOrder.append(bestOrder)
            maxProfit += profit(bestOrder[0])
        print('MaxProfit: {}'.format(maxProfit))
        print(totalOrder)
        i += int(cases[i]) + 1
        #go to the next case's headline
    print('END')
    return

if __name__ == '__main__':
    main() 