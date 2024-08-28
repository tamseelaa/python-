c_username= 'python'
c_password='rules'
a=0
max_a=5
while a<max_a:
    username = input("Enter username: ").lower()
    password = input("Enter password: ").lower()
    if c_username==username and c_password==password:
        print ("welcome")
        break
    else:
        a += 1
        remaining_attempts = max_a-a
        if remaining_attempts > 0:
            print(f"Incorrect username or password. You have {remaining_attempts} attempt(s) left.\n")
        else:
            print("Access denied.")