#perform based on age

age = eval(input("Please enter your age: "))
if (age >= 1) and (age <= 18):
    print("Important Birthday!\n")
elif (age == 21) or (age == 50):
    print("Important Birthday\n")
elif not(age < 60):
    print("Important higher than 60 Birthday\n")
else:
    print("Not important Birthday\n")