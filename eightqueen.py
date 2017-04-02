def confict(state, pos):
    nextY = len(state)
    if pos in state:
        return True
    for i in range(nextY):
        if nextY - pos == i - state[i] :
            return True
        if nextY + pos == i + state[i] :
            return True
    return False

def queens(num, state=()):
    if num-1 == len(state):
        for i in range(num):
            if not confict(state, i):
                yield (i,)
    else:
        for pos in range(num):
            if not confict(state, pos):
                for result in queens(num, state+(pos,)):
                    yield (pos,) + result
 
a = list(queens(6))    
for i in a:
    print(i)
