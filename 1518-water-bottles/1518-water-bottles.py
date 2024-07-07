class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        empty = numBottles
        drink = numBottles
        while (empty >= numExchange):
            drink += empty // numExchange
            empty = empty % numExchange + empty // numExchange
        return drink



        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        