username = "admin"
password = "1234"
system = True
for i in range(3):
    username_input = input("username: ")
    password_input = input("password: ")
    if username == username_input and password == password_input:
        break
    else:
        system = False
        if i == 2:
            print ("account locked")
        else:
            print ("wrong username or password")
            print("------------------------------------------")
if system:
    N = int(input("Enter a number: "))
    for num in range(2, N + 1):
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)