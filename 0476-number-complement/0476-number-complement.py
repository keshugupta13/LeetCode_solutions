class Solution(object):
    def findComplement(self, num):
        def decimal_to_binary(num):
            if num == 0:
                return "0"
            if num == 1:
                return "1"
            binary = ""
            while num > 0:
                rem = num % 2
                binary = str(rem) + binary
                num = num // 2 
            return binary
        
        def binary_to_decimal(binary):
            decimal = 0
            binary_str = binary[::-1]
            for i in range(len(binary_str)):
                decimal += int(binary_str[i]) * (2 ** i)
            return decimal

        binary = decimal_to_binary(num)
        n = len(binary)

        complement = ''
        for i in range(n):
            if binary[i] == '0':
                complement += '1'
            else:
                complement += '0'

        return binary_to_decimal(complement)

        


                  
