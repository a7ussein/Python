def recipe():
    recipePrompt = input("Have a receipe: ")
    if(recipePrompt == "yes" or recipePrompt == "Yes" or recipePrompt == 'y' or recipePrompt == 'y'):
        ingredients()
    else:
        print("Find a recipe online")
        recipe()
    
def ingredients():
    ingredientsPrompt = input("Have the ingredients: ")
    if(ingredientsPrompt == "yes" or ingredientsPrompt == "Yes" or ingredientsPrompt == 'y' or ingredientsPrompt == 'Y'):
        followRecipe()
    else:
        print("Buy them")
        ingredients()

def followRecipe():
    followRecipePrompt = input("Did you follow the receipe exactly: ")
    if(followRecipePrompt == "yes" or followRecipePrompt == "Yes" or followRecipePrompt == 'y' or followRecipePrompt == 'Y'):
        cookiesBaked()
    else:
        print("Start over. Cookies demand percision")
        ingredients()

def cookiesBaked():
    cookiesBakedPrompt = input("are the cookies backed: ")
    if(cookiesBakedPrompt == "yes" or cookiesBakedPrompt == "Yes" or cookiesBakedPrompt == 'y' or cookiesBakedPrompt == 'Y'):
        delicious()
    else:
        print("Bake them")
        cookiesBaked()

def delicious():
    deliciousPrompt = input("Are they delicious: ")
    if(deliciousPrompt == "yes" or deliciousPrompt == "Yes" or deliciousPrompt == 'y' or deliciousPrompt == 'Y'):
        print("Good Job!")
    else:
        print("Get some milk")
        deliciousWithMilk()

def deliciousWithMilk():
    deliciousWithMilkPrompt = input("Are they delicious with Milk: ")
    if(deliciousWithMilkPrompt == "yes" or deliciousWithMilkPrompt == "Yes" or deliciousWithMilkPrompt == 'y' or deliciousWithMilkPrompt == 'Y'):
        print("Good Job!")
    else:
        print("Find a recipe online")
        recipe()

recipe()

