

# Having the try-except will let the file continue after the error
# in below example, divide by 0 will error AND time() is not a real function, but script still continues and Completes

x=0

try:
  print(x)
  print(5/x)
  time()

except NameError:
  print("Variable x is not defined")

except ValueError:
  print("Number problem")

except:
  print("ERROR: Something else went wrong")


print("Complete")