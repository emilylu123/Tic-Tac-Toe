# Analyze the game state and print the result. Possible states:
# Game not finished when neither side has three in a row but the grid still has empty cells.
# Draw when no side has a three in a row and the grid has no empty cells.
# X wins when the grid has three X’s in a row.
# O wins when the grid has three O’s in a row.
# Impossible when the grid has three X’s in a row as well as three O’s in a row, or there are a lot more X's than O's or vice versa (the difference should be 1 or 0; if the difference is 2 or more, then the game state is impossible).

state = input('Enter cells:')
out = list(state)

print('---------')
print('| ' + out[0] + ' ' + out[1] + ' ' + out[2] + ' |')
print('| ' + out[3] + ' ' + out[4] + ' ' + out[5] + ' |')
print('| ' + out[6] + ' ' + out[7] + ' ' + out[8] + ' |')
print('---------')

result = ''
winner = ''
count_x = 0
count_y = 0
count_winner = 0
for sign in out:
    if sign == 'X':
        count_x += 1
    elif sign == 'O':
        count_y += 1

if out[0] == out[1] == out[2] or out[0] == out[4] == out[8] or out[0] == out[3] == out[6]:
    count_winner += 1
    winner = out[0]

if out[3] == out[4] == out[5] or out[2] == out[4] == out[6] or out[1] == out[4] == out[7]:
    count_winner += 1
    winner = out[4]

if out[6] == out[7] == out[8] or out[2] == out[5] == out[8]:
    count_winner += 1
    winner = out[8]

if count_winner == 1:
    result = winner + ' wins'
elif count_winner > 1 or abs(count_x - count_y) > 1:
    result = 'Impossible'
elif count_winner == 0 and count_x + count_y < 9:
    result = 'Game not finished'
else:
    result = 'Draw'

print(result)


