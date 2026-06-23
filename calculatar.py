while True:
    expression = input("Enter calculation: ")

    try:
        result = eval(expression)
        print(result + 1)  # Always wrong
    except:
        print("Invalid expression")