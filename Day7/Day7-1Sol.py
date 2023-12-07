import pandas as pd

data = pd.read_csv('Day7/day7mat.txt', sep= ' ', names= ['cards', 'bid'])
print(data)

def CardsValue(s) -> str:
    s = str(s)
    hands = [[1, 1, 1, 1, 1], [2, 1, 1, 1], [2, 2, 1], [3, 1, 1], [3, 2], [4, 1], [5]]
    cunts = []
    for c in set(s):
        cunts.append(s.count(c))
    cunts.sort(reverse= True)

    tops = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10}
    answ = chr(122 - hands.index(cunts))
    for A in s:
        B = tops[A] if A in tops else int(A)
        answ += chr(122 - B)
    return answ

data['values'] = data['cards'].map(CardsValue)
data.sort_values(['values'], inplace= True, ascending= False, ignore_index= True)

winnings = 0
for i, val in enumerate(data['bid']):
    winnings += (i+1)*val
print(winnings)