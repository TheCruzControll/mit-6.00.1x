x = 100
low = 0
high = x
ans = int(round((high+low)/2))
print('Please think of a number between 0 and 100!')
while True:
  try:  
    print('Is your secret number ' + str(ans) + '?')
    response = (input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly."))
    if response == 'c':
        break
    elif response == 'h':
      high = ans
    elif response == 'l':
      low = ans
    else:
        print('Sorry, I did not understand your input.')
    ans = int((high+low)/2)
  except:
      print('Sorry, I did not understand your input')
print('Game over. Your secret number was: ' + str(ans))