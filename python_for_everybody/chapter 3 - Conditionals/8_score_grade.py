score = input("Enter Score: ")
score = float(score)
if score < 0.6:
    print('F')
elif 0.6 <= score < 0.7:
    print('D')
elif 0.7 <= score < 0.8:
    print('C')
elif 0.8 <= score < 0.9:
    print('B')
elif 0.9 <= score < 1.0:
    print('A')
else:
    print('Value out of range')


astr = 'Hello Bob'
istr = int(astr)