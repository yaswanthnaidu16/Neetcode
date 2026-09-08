class Solution:
    def calPoints(self, ops: List[str]) -> int:
        ans = []
        for i in ops:
            if i == "D":
                temp = ans[-1]
                temp2 = int(ans[-1])*2
                ans.append(temp2)
            elif i == "C":
                ans.pop()
            elif i == "+":
                temp3 = int(ans[-1]) + int(ans[-2])
                ans.append(temp3)
            else:
                ans.append(int(i))
        return sum(ans)


        