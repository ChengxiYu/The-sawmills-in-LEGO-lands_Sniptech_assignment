from itertools import permutations

def singleProfit_below4(truck: int) -> int:
    if truck == 0:
        return 0
    if truck == 1:
        return -1
    if truck == 2:
        return 3
    if truck == 3:
        return 1

def profit(order: tuple[int]) -> int:
    res = 0
    remain = 0
    #remain is the rest part of sawmill can be used after cutting previous truck
    #for example, if we cut 1 + 3 + 2 from previous truck, 
    #the remain part now is 3 - 2 = 1, the first part of this truck must be 1
    for truck in order:
        while truck > 4:
            truck -= 3
            res += 1
        #if truck length more than 4, we can take the middle 3 out because it will not influence final result
        if truck < remain:
            res += singleProfit_below4(truck)
            remain -= truck
            continue

        if truck == remain:
            res += singleProfit_below4(truck)
            remain = 0
            continue
        if truck == 4:
            if remain == 2:
                res += singleProfit_below4(2) * 2
                remain = 1
                continue
            if remain == 0:
                remain = 2
                continue
            if remain == 1:
                remain = 0
                continue
        if truck > remain:
            res += singleProfit_below4(remain) + singleProfit_below4(truck - remain)
            remain = 3 - (truck - remain)
    return res 
    
def bestProfitSets(trucks: list[int]) -> list[list[int]]:
    res = set()
    #res -> all the rebuild truck order with best profit
    maxProfit = len(trucks) * (-1)
    for order in permutations(trucks, len(trucks)):
        #check all orders of this truck list
        profit_ = profit(order)
        if profit_ == maxProfit:
            res.add(order)
            continue
        if profit_ > maxProfit:
            res = set()
            res.add(order)
            maxProfit = profit_
    return list(res)

def readCases(filename :str) -> list[str]:
    fin = open(filename)
    text = fin.readlines()
    for i in range(len(text)):
        text[i] = text[i].replace(' ', '')
        text[i] = text[i].strip('\n')
    fin.close()
    return text
