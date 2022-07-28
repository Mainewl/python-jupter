import time



# x = 0
# while True:
#     print(x)
#     x += 1


counter = 0
while counter < 11:
    print(counter)
    counter = counter + 1
    if counter == 11:
        break
    time.sleep(1)
print('now its okay')



rows = 5
for i in range(1, rows+1, 1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print('')

n= 5
k= 5
for i in range(0,n+1):
    for j in range(k-i,0,-1):
        print(j, end=" ")
    print()


numbers = [12, 75, 150, 180, 145, 525, 50]

for item in numbers:
    if item > 500:
        break
    elif item > 150:
        continue 
    elif item % 5 == 0:
        print(item)


num = 758699
count = 0

while num != 0:
    num = num //10
    count = count + 1
print(count)    



for i, v in enumerate(['tic', 'tac', 'toe']):
    print (i, v)


frutas = ['banana', 'maçã', 'laranja']
for u in frutas:
    print(u)
    if u == 'maçã':
        print('a maçã ta podre')

for l in range(2, 6):
    print(l)
