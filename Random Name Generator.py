import random

# Random methods: Choice() Choices() sample() using the k= extension to set the occurence
# Random name generator
while True:
    print()
    random_name = input("Would you like a random name? (yes or no): ")
    print()
    Variables = ('Juan', 'Bob', 'Carly', 'Kalil', 'Marcus', 'Leon', 'Jose', 'Drew', 'Jared', 'Isabelle', 'Jasmine', 'Lauren', 'Kayjah', 'Keytor','Kirstin', 'Kiana', 'Kaleb')
    if random_name == 'y' or random_name == 'yes' or random_name == 'Yes' or random_name == 'YES' or random_name == 'Y':
        print()
        print('Your name is: ',random.sample(Variables, k= 2))
        continue
    else:
        if random_name == 'no' or random_name == 'n':
            leaving_so_soon = input("Are you sure you want to leave the program? yes or no: ")
            print()
            if leaving_so_soon == 'yes' or leaving_so_soon == 'y':
                print()
                print("Now leaving random name generator")
                quit()


    


