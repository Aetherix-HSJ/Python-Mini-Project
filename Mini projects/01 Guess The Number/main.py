# 🎯 Guess the Number

# I have selected a number between 1 and 100.

# Enter your guess: 50
# Too high!

# Enter your guess: 25
# Too low!

# Enter your guess: 37
# Too high!

# Enter your guess: 32
# 🎉 Correct!

# You guessed it in 4 attempts.

import random

num = random.randint(1, 100)
guess = int(input("Enter your guess: "))
count = 1
while(guess!=num):
   count +=1
   if(guess>num):
      print("lower!")
   elif(guess<num):
      print("higher")
   guess = int(input("Enter your guess: "))
   
print(f"Wohooo! you have guessed it right in {count} attempts")