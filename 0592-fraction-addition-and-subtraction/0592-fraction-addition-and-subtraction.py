class Solution(object):
    def fractionAddition(self, expression):
        numerator = 0
        denominator = 1
        n = len(expression)
        i = 0
        while i < n:
            curr_numerator = 0
            curr_denominator = 0
            isNeg = False
            ch = expression[i]
            
            if ch == '+' or ch == '-':
                if ch == '-':
                    isNeg = True
                i += 1

            # Extract the numerator
            start = i
            while i < n and '0' <= expression[i] <= '9':
                i += 1
            curr_numerator = int(expression[start:i])

            if isNeg:
                curr_numerator *= -1

            i += 1  # Skip the '/' sign

            # Extract the denominator
            start = i
            while i < n and '0' <= expression[i] <= '9':
                i += 1
            curr_denominator = int(expression[start:i])
            
            # Update the numerator and denominator for the sum
            numerator = numerator * curr_denominator + curr_numerator * denominator
            denominator = denominator * curr_denominator

        # Find the greatest common divisor (gcd) to simplify the fraction
        gcd_value = abs(self.gcd(numerator, denominator))
        numerator //= gcd_value
        denominator //= gcd_value

        return str(numerator) + "/" + str(denominator)

    def gcd(self, a, b):
        if b == 0:
            return a
        else:
            return self.gcd(b, a % b)


