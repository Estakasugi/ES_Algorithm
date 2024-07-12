def numWaterBottles(numBottles, numExchange):
    #initial stage
    consumed = 0

    while numBottles >= numExchange:
        numBottles -= numExchange
        numBottles += 1
        consumed += numExchange
        #print(consumed, numBottles)

    return consumed + numBottles

ans = numWaterBottles(numBottles = 15, numExchange = 4)
print(ans)