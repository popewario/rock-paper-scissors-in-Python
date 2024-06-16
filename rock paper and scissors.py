import random

def paly():
    user = input('r == rock, p == paper or s == scissors ').lower()
    comp = random.choice(['r', 'p', 's'])

    if user == comp:
        return 'it\'s a tie'
#" \ " ==   Used to include special characters in strings,
#  such as a single quote within a string 
    if is_win(user, comp):
        return 'you won'
    
    return 'you lose'
    
def is_win(player,cpu):
    if (player == 'r' and cpu == 's') or (player == 's' and cpu == 'p') \
    or (player == 'p' and cpu == 'r'):
        return True  
    
#" \ " == Used to continue a statement on the next line.
print(paly())