username = "masum"
password = "5678"
for i in range(3):
    user = input("username")
    pas = input("password")
    if username == user and password == pas:
        print("wellcome")
        break
    elif username != user and password == pas:
        print("the username is incorect")
    elif username == user and password != pas:
        print("the password is incorect")
    else:print("username and password are wrong")
    if i == 2:
     print("you blocked")