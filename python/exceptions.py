
import sys

try:
    x = int(input('x: '))
    y = int(input('y: '))
except ValueError:
        print('error: need integers only please !')
        sys.exit(1) # sort du programme avec une erreur specifique
    

try: 

    result = x / y 
except ZeroDivisionError:
    print('error: cannot divide by 0!')
    sys.exit(1)

except ValueError:
    print('error: need integers only please !')

print(f'{x} / {y} = {result}')