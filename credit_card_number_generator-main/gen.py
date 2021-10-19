import random

# Author: EH
# Educational Purposes Only 
# i am not responsible for you're actions
#-------------------------------------------------

class GenerateCardNumber:
    def __init__(self):
        self.t = {"m":[5], "v":[4]}
        self.pos = {"m":[0], "v":[0]}


    def luhn(self, num):
        if type(num) != str:
            num = str(num)
        else:
            num = num.strip()
        
        res = 0
        sec = False
        for i in range(len(num)-1, -1, -1):
            a = int(num[i])
            if sec:
                a = a*2
                if a > 9:
                    res += a-9
                    sec = False
                    continue
                res += a
                sec = False
            else:
                res += a
                sec = True
        
        return res%10

    def gen_digits(self, length):
        out = []
        for i in range(length):
            out.append(str(random.randint(0, 9)))
        return out

    def gen_val(self, t):
        digits = self.gen_digits(16)
        digits[self.pos[t][0]] = str(self.t[t][0])
        rem = self.luhn("".join(digits))
        p = self.pos[t]
        pos = 0
        temp = 0 

        while rem > 0:
            pos = random.randint(0, len(digits)-1) 
            if digits[pos] == "0" or pos%2 == 0 or pos in p:
                continue

            temp = int(digits[pos])
            if temp >= rem:
                digits[pos] = str(temp-rem)
                rem = 0
            else:
                rem -= 1
                temp -= 1
                digits[pos] = str(temp)
        
        return "".join(digits)
