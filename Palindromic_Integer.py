try:
    x = int(input("Enter the number to check for palindromic: "))
    
    str1 = str(x)
    str2 = str1[::-1]
    
    if str1 == str2:
        print("The given number is palindromic.")
    else:
        print("The number is not palindromic.")
except ValueError:
    print("Invalid input! Please enter a valid integer.")
