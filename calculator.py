# Calculator Python Simple Program
def welcome():
    print('''
   Welcome to Calculator
   ''')
   
# Don’t forget to call the function
welcome()

def calculate(): 
   operation = input('''
   Please type in the match operation you would like to complete: 
   + for addition
   - for subtraction
   * for multiplication
   / for division
   ** for power
   % for modulo

   ''')

   prev = int(input('Enter your first Number: '))
   current = int(input('Enter your second Number: '))

   # Addition
   if operation == '+':
      print('{} + {} = '.format(prev, current), prev + current)

   # Subtraction
   elif operation == '-':
      print('{} - {} = '.format(prev, current), prev - current)

   # Multiplication
   elif operation == '*':
      print('{} * {} = '.format(prev, current), prev * current)

   # Division
   elif operation == '/':
      print('{} / {} = '.format(prev, current), prev / current)

   # Power
   elif operation == '**': 
      print('{} / {} = '.format(prev, current), prev ** current)

   # Modulo
   elif operation == '%': 
      print('{} / {} = '.format(prev, current), prev % current)

   else: 
      print('You have not typed a valid operator, please run the program again.')

   # Add again() function to calculate() function
   again()

def again():
   calc_again = input('''
Do you want to calculate again? 
Please type Y for YES or N for NO.

   ''')

   if calc_again.upper() == 'Y':
      calculate()
   elif calc_again.upper() == 'N':
      print('See you later.')
   else: 
      again()

# Call calculate() outside of the function
calculate()