import math

print('\n')
print('===================')
print('Area Calculator 📐')
print('===================')
print('\n')
print('1) Triangle')
print('2) Rectangle')
print('3) Square')
print('4) Circle')
print('5) Quit')
print('\n')



figure = input('Which shape would you like to calculate? ')
print('\n')

if figure == '1':
    base = int(input('Enter base length: '))
    height = int(input('Enter height: '))
    area = (base * height) / 2
    print('\n')
    print(f'The area of the triangle is: {area}')
    print('\n')

elif figure == '2':
    length = int(input('Enter length: '))
    width = int(input('Enter width: '))
    area = length * width
    print('\n')
    print(f'The area of the rectangle is: {area}')
    print('\n')

elif figure == '3':
    side = int(input('Enter side length: '))
    area = side ** 2
    print('\n')
    print(f'The area of the square is: {area}')
    print('\n')

elif figure == '4':
    radius = int(input('Enter radius: '))
    area = math.pi *(radius ** 2)
    print('\n')
    print(f'The area of the circle is: {area: .2f}')
    print('\n')

elif figure == '5':
    print('Exiting program. Bye!')

else:
    print('Invalid input. Please enter a number between 1 and 5')

print('\n')
