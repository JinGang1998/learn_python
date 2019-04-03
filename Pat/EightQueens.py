def conflict(state , nextX):
    nextY = len(state)
    for i in range(nextY):
        if abs(state[i] - nextX) in (0 , nextY - i ):
            return True
    return False
def queens(num = 8 , state = ()):
    for pos in range(num):
        if not conflict(state , pos):
            if len(state) == num -1:
                yield (pos,)
                #print((pos,))
            else:
                for result in queens(num , state + (pos,)):
                    yield (pos, ) + result
                    print(result)
                    print((pos,))
                    print("###"+str((pos, )) + str(result))
print(list(queens(8)))
#print((123,)+(2))

