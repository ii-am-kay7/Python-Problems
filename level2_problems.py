def has_33(nums):
    for i in range(0, len(nums)-1):
        if nums[i] == 3 and nums[i+1] == 3:
            return True
        
    return False

def has_33(nums):
    for i in range(0, len(nums)-1):
        if nums[i:i+2] == [3,3]:
            return True
        
    return False

def paper_doll(text):
    paper_doll = ""

    for letter in text:
        paper_doll += letter * 3

    return paper_doll

def blackjack(a,b,c):
    sumOf = sum((a,b,c))

    if sumOf <= 21:
        return sumOf
    elif sumOf > 21 and (11 in [a,b,c]):
        sumOf = sumOf - 10
        return sumOf
    elif sumOf > 21:
        return 'BUST'
    
def spy_game(nums):

    code = [0,0,7,'x']

    for num in nums:
        if num == code[0]:
            code.pop(0)

    return len(code) == 1




















