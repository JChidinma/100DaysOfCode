def divide_numbers(a, b):
    try:
        result = a/b
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed")
    except TypeError:
        print("Error: Check the data type in your calculation.")
    else:
        print("The result is: ", result)

    finally:
        print("Execution completed")


divide_numbers(6, 2)
divide_numbers(6, 0)
divide_numbers(10, "a")
