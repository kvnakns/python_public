
import random



# print out numbers up to x
# Generator example
def count_up_to(max):
    count = 1
    while count <= max:
        yield count
        count += 1

for num in count_up_to(22):
    print(num)




# Decorator example
import time
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Function took {end - start} seconds")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(1)
    print("Function completed")

slow_function()



 
# text generating

nouns = ["dog", "car", "computer", "city", "tree"]
verbs = ["runs", "drives", "types", "jumps", "sings"]

noun = random.choice(nouns)
verb = random.choice(verbs)

print ("The" ,noun, verb)