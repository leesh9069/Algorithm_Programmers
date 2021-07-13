class Programmers1:

    def __init__(self, progresses, speeds):
        self.progresses = progresses
        self.speeds = speeds

    def solution(self):
        residue = []
        for i in range(len(self.progresses)):
            if (100 - self.progresses[i]) % self.speeds[i] == 0:
                r = (100 - self.progresses[i]) / self.speeds[i]
                residue.append(r)
            else:
                r = ((100 - self.progresses[i]) // self.speeds[i]) + 1
                residue.append(r)

        return residue

    def solution2(self):
        residue = self.solution()
        first = 0
        answer = []
        for i in range(len(residue)):
            if residue[i] > residue[first]:
                answer.append(i - first)
                first = i
        answer.append(len(residue) - first)

        return answer

rlt = Programmers1([95,90,99,99,80,99],[1,1,1,1,1,1])
print(rlt.solution2())