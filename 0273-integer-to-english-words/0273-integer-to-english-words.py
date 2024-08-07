class Solution(object):
    belowTen = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    belowTwenty = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    belowHundred = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

    def numberToWords(self, num):
        if num == 0:
            return "Zero"

        if num < 10:
            return self.belowTen[num]
        
        if num < 20:
            return self.belowTwenty[num - 10]

        if num < 100:
            return self.belowHundred[num // 10] + ("" if num % 10 == 0 else " " + self.belowTen[num % 10])

        if num < 1000:
            return self.belowTen[num // 100] + " Hundred" + ("" if num % 100 == 0 else " " + self.numberToWords(num % 100))
        
        if num < 1000000:
            return self.numberToWords(num // 1000) + " Thousand" + ("" if num % 1000 == 0 else " " + self.numberToWords(num % 1000))

        if num < 1000000000:
            return self.numberToWords(num // 1000000) + " Million" + ("" if num % 1000000 == 0 else " " + self.numberToWords(num % 1000000))

        return self.numberToWords(num // 1000000000) + " Billion" + ("" if num % 1000000000 == 0 else " " + self.numberToWords(num % 1000000000))