user_no = int(input('Enter a number, to find if its prime or not: '))

if user_no<=1:
    print('not prime')
    for i in range(2,user_no):
        user_no%i==0
        print("not prime")
else:
    print('it is prime')
