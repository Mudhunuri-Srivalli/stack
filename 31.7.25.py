password = "valli@14"
attempts = 3
while attempts > 0:
    user_input = input("Enter password: ")
    if user_input == password:
        print("Login successful")
        break
    else:
        attempts -= 1
        print(f"Incorrect. {attempts} attempts left.")
else:
    print("Account locked")
