
# Task 1: try, except, else, finally usage
# 



# Valid: try + except
try:
    print(10 / 0)
except ZeroDivisionError:
    print("Handled ZeroDivisionError")

# Valid: try + finally
try:
    print("Inside try + finally example")
finally:
    print("finally block executed")

# Valid: try + except + else
try:
    x = 5 + 5
except:
    print("Error occurred")
else:
    print("Else executed (no error)")

# Valid: try + except + else + finally
try:
    x = int("100")
except ValueError:
    print("ValueError occurred")
else:
    print("Value converted successfully")
finally:
    print("Finally executed always")



# Task 2: Nested try-except blocks




try:
    print("Outer try block")

    # Inner try 1
    try:
        a = int("abc")
    except ValueError:
        print("Inner except: ValueError handled")

    # Inner try 2
    try:
        b = 10 / 0
    except ZeroDivisionError:
        print("Inner except: ZeroDivisionError handled")

except Exception as e:
    print("Outer except caught:", e)

finally:
    print("Outer finally executed")
