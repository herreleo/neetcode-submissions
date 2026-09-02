class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        profit = 0

        min_price = prices[0]
        

        L = 0
        R = 0
        for i in range(len(prices)):
            current_profit = prices[i] - min_price
            if profit < 0:
                profit = 0
            
            elif current_profit > profit:
                profit = current_profit

            if prices[i] < min_price:
                min_price = prices[i]

        return profit
         
        


            



