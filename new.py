x = input("What is your name: ")
y = input("What is your age: ")

def yomoSucks(name, age):
    if(name == "Mohammed" or name == "mohammed" or name == "Mohammed Ahmed" or name == "mohammed ahmed" and int(age) == 18):
        print("YoMo, You Suck!")
    else:
        print("You are not yomo, you are a good person")

yomoSucks(x, y)
