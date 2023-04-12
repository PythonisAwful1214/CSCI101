#   Nicolas Callier
#   CSCI 101 - D
#   Python Lab 3
#   Time: 45 minutes

def check_error(TIC):
    valid = 0
    for i in range(0, len(TIC)):
        if len(TIC[i]) != 3:
            return 'ERROR'
        for j in range(0, len(TIC[i])):
            if TIC[i][j] == "O" or TIC[i][j] == "X" or TIC[i][j] == "E":
                valid += 1
    if valid != 9:
        return 'ERROR'
    else:
        return ''
        
def ZOOWEEMAMA(TIC):
    for i in range (0, 3):
        if TIC[0][i] == TIC[1][i] and TIC[0][i] == TIC[2][i] and TIC[0][i] != 'E':
            return TIC[0][i]
    return ''

def ZOOWEEPAPA(TIC):
    for i in range (0, 3):
        if TIC[i][0] == TIC[i][1] and TIC[i][0] == TIC[i][2] and TIC[i][0] != 'E':
            return TIC[i][0]
    return ''

def ZOOWEENB(TIC):
        if TIC[0][0] == TIC[1][1] and TIC[0][0] == TIC[2][2] and TIC[0][0] != 'E':
            return TIC[0][0]
        elif TIC[0][2] == TIC[1][1] and TIC[1][1] == TIC[2][0] and TIC[0][2] != 'E':
            return TIC[0][2]
        return ''
nlist = [input('ROW0> '), input('ROW1> '), input('ROW2> ')]

yippe = check_error(nlist)

if len(yippe) != 0:
    outP = yippe
else:
    outP = '' + ZOOWEEMAMA(nlist) + ZOOWEEPAPA(nlist) + ZOOWEENB(nlist)
    if len(outP) == 0:
        outP += 'T'
print('OUTPUT ' + outP)
