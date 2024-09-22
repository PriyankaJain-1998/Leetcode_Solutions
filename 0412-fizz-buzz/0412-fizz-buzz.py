class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        # output = [0]*n
        # for i in range(1,n+1):
        #     if i%3==0 and i%5==0: output[i-1] = "FizzBuzz"
        #     elif i%3==0: output[i-1] = "Fizz"
        #     elif i%5==0: output[i-1] = "Buzz"
        #     else: output[i-1]=str(i)
        # return output


        return ["FizzBuzz" if i%3==0 and i%5==0 else "Fizz" if i%3==0 else "Buzz" if i%5==0 else str(i) for i in range(1,n+1)]



