# -*- coding: utf8 -*-


import random
import time


NUM_LIST = list(range(1, 46))


def shuffled(lst):

    random.shuffle(lst)
    return lst


def getLottoNumList():

    numList = NUM_LIST[:]
    random.shuffle(numList)

    return sorted(numList[:6]) + [numList[-1]]


def showLottoNumList(lottoNumList):

    for num in lottoNumList[:6]:
        print num,
    print "/", lottoNumList[6:]


def getSameCount(list1, list2):

    return len(set(list1) & set(list2))


def checkLotto(winLottoNumList, lottoNumList):

    sameCount = getSameCount(winLottoNumList[:6], lottoNumList[:6])

    if sameCount == 6:
        return 1

    elif sameCount == 5:
        if winLottoNumList[-1] in lottoNumList:
            return 2
        else:
            return 3

    elif sameCount == 4:
        return 4
    
    elif sameCount == 3:
        return 5
    
    return None


def lottoSimulation(lottoNumList = None, differentOpt = False):

    if lottoNumList == None and not differentOpt:
        lottoNumList = getLottoNumList()

    if not differentOpt:
        print "your lotto numbers"
        showLottoNumList(lottoNumList)
        print

    winCountList = [0] * 5
    drawCount = 0
    
    while winCountList[0] == 0:

        if differentOpt:
            lottoNumList = getLottoNumList()

        winLottoNumList = getLottoNumList()

        rank = checkLotto(winLottoNumList, lottoNumList)

        if rank != None:
            winCountList[rank - 1] += 1

        drawCount += 1

    
    print "win  lotto numbers"
    showLottoNumList(winLottoNumList)
    print
    print "draw count"
    print drawCount
    print
    print "result"

    for i in range(5):
        print i + 1, ":", "%10d %20f" % (winCountList[i], winCountList[i] / float(drawCount))
    print


def test():

    assert len(getLottoNumList()) == 7

    lottoNumList = getLottoNumList()
    assert all(lottoNumList.count(num) == 1 for num in lottoNumList)

    winLottoNumList = [1, 2, 3, 4, 5, 6, 7]

    assert checkLotto(winLottoNumList, [1, 2, 3, 4, 5, 6]) == 1
    assert checkLotto(winLottoNumList, [1, 2, 3, 4, 5, 7]) == 2
    assert checkLotto(winLottoNumList, [2, 3, 4, 5, 6, 7]) == 2
    assert checkLotto(winLottoNumList, [1, 2, 3, 4, 5, 8]) == 3
    assert checkLotto(winLottoNumList, [3, 4, 5, 6, 7, 8]) == 4
    assert checkLotto(winLottoNumList, [1, 5, 6, 7, 8, 9]) == 5

    #lottoSimulation(sorted([45, 37, 21, 11, 17, 7]))
    lottoSimulation(None, True)

    print "Success"


def main():

    start = time.time()

    #lottoSimulation(sorted([10, 11, 23, 40, 44, 37]))
    lottoSimulation(None, True)

    print time.time() - start


if __name__ == "__main__":
    #test()
    main()
