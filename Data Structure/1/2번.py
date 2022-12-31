def isPalindrome(string):
    lenStr = len(string)
    for i in range(lenStr/2):
    	if string[i] != string[lenStr-1-i]:
    		return False
    return True

def isPalindrome(string):
    if len(string) == 1:
        return True
        
    if string[0] == string[-1]:
        return isPalindrome(string[1:-1])
    else:
        return False