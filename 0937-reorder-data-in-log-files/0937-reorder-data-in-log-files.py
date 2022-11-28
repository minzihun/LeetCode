class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        
        letter_logs = []
        digit_logs = []
        
        # split digit and letter-logs
        for log in logs:
                if log[-1].isdigit():
                    digit_logs.append(log)
                else:
                    letter_logs.append(log)
        
        # need a process to order letter-logs
        letter_logs.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        
        return letter_logs + digit_logs