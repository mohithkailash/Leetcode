class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digits = []
        letters = []
        for log in logs:
            if log[-1].isdigit():
                digits.append(log)
            else:
                letters.append(log)
        letters = sorted(letters, key=lambda letter: (letter.split()[1:],letter.split()[0]))
        result = letters+digits
        
        return result