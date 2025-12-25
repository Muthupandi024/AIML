secret_number = 24
guess = 0
while guess != secret_number :
    guess = int(input("Enter the guess number : "))
    if secret_number<guess:
        print(f'{guess} is a long')
    elif secret_number>guess:
        print(f'{guess}is low ')
    else:
        print(f'{guess} is corrrect guess number ')

