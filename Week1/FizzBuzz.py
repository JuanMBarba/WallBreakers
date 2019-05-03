class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result= []
        for number in range(1,n+1):
            strNumber=''
            if number%3 == 0:
                strNumber+="Fizz"
            if number%5 == 0:
                strNumber+="Buzz"
            if strNumber == '':
                strNumber+=str(number)
            result.append(strNumber)
            
        return result
        
