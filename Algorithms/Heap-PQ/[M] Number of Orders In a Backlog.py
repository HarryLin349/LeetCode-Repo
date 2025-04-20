from heapq import heapify, heappush, heappop
class Solution:
    '''
    if buy:
        find smallest sell in backlog (minsell)
        if minsell <= buy, execute and remove sell
        else, add buy to backlog

    if sell:
        find largest buy in backlog (maxbuy)
        if maxbuy >= sell, execute and buy removed
        else, add sell to backlog
    
    return total amount of orders in the backlog

    idea: use minheap -> sells and maxheap ->buys
    use a tuple to track the amount
    at each operation, subtract amount from tuple until complete
    '''
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        MOD = 10**9 + 7
        sells = []
        buys = []
        for order in orders:
            price, amount, ordertype = order[0], order[1], order[2]
            if (ordertype == 0):
                while (amount > 0):
                    if (sells and sells[0][0] <= price):
                        # we can execute, rm amount equal to min(sells[0][1] and amount)
                        executed = min(sells[0][1], amount)
                        amount -= executed
                        newsell = (sells[0][0], sells[0][1] - executed)
                        heappop(sells)
                        if newsell[1] > 0:
                            heappush(sells, newsell)
                            print()
                    else:
                        heappush(buys, (-price, amount))
                        amount = 0
            else:
                while (amount > 0):
                    if (buys and -buys[0][0] >= price):
                        # we can execute, rm amount equal to min(buys[0][1] and amount)
                        executed = min(buys[0][1], amount)
                        amount -= executed
                        newbuy = (buys[0][0], buys[0][1] - executed)
                        heappop(buys)
                        if newbuy[1] > 0:
                            heappush(buys, newbuy)
                    else:
                        heappush(sells, (price, amount))
                        amount = 0
        res = 0
        for price, amount in sells:
            res += amount
            res %= MOD
        for price, amount in buys:
            res += amount
            res %= MOD
        return res