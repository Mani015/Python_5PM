
count = 0
limit = 4
while count< limit:
    give = int(input('Enter your password:'))
    if give == 10:
        print('screen open')
        break
    count+=1
else:
    print('soory ! your completed')
