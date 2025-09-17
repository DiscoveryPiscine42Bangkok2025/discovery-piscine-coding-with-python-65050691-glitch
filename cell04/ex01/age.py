age = int(input("Pls tell me your age:"))
print("You are currently",age,"years old.")
i = 0
year=10
for i in range(1,4):
        print("In",year*i,"years, you'll be",age+(i*year),"years old.")
        year+10