def checkOnesSegment(self, s):
        t = i  = 0  
        while i < len(s):
            if s[i] == '1':          
                t += 1               
            if i+1 > t:              
                if '1' in s[i:]:     
                    return False     
                return True          
            i += 1
        return True                  