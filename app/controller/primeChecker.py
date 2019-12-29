class PrimeChecker():

    def isTwoSidedPrime(self, number):
        isPrime=True
        number=str(number)
        #left trimming
        while(len(number)):
            if self.checkPrime(number):
                number=self.truncateLeftDigits(number)
            else:
                isPrime=False
                break
        #right trimming
        while(len(number)):
            if self.checkPrime(number):
                number=self.truncateRightDigits(number)
            else:
                isPrime=False
                break
        return isPrime

    @staticmethod
    def truncateLeftDigits(number):
        number=str(number)
        number=number[1:]
        return number

    @staticmethod
    def truncateRightDigits(number):
        number=str(number)
        number=number[:-1]
        return number

    @staticmethod
    def checkPrime(number):
        number=int(number)
        result = True
        if number<=1:
            result = False
        else :
            if number<=3:
                result = True
            else :
                if ((number % 2 ==0) or (number % 3 ==0)):
                    result = False
                else:
                    i = 5
                    while(i * i <= number) : 
                        if (number % i == 0 or number % (i + 2) == 0):
                            result= False
                            break
                        i = i + 6
        
        return result
