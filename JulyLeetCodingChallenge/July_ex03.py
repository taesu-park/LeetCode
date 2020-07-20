#(3) Add Binary

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        end = max(len(a),len(b))
        a = '0'*(end-len(a))+a
        b = '0'*(end-len(b))+b
        result = ''
        idx = 0
        for i in range(end-1,-1,-1):
            tmp = 0
            if int(a[i]) + int(b[i]) + idx ==2:
                idx = 1
                result = '0'+result
            elif int(a[i]) + int(b[i]) + idx == 3:
                idx = 1
                result = '1'+result
            else:
                result = str(int(a[i])+int(b[i])+idx) + result
                idx = 0
        if idx:
            result = '1'+result
        return result