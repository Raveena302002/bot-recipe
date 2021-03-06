"""
recipe chatbot
1. Greeting the user
2. Menu
3. Respond to users input
4. Show the menu until the user prompts the exit option
"""

import random
from datetime import datetime
def greet():
    print("Hii! Welcome to our restaurant i am recipe bot I can help you to choose various options and details of food items in our restaurant")
                

def time():
    present_time=datetime.now()
    Greeting="Good Morning"
    if present_time.hour>12 and present_time.hour<=17:
        Greeting="Good Afternoon"
    elif present_time.hour>17 and present_time.hour<=22:
        Greeting="Good Evening"
    elif present_time.hour>22:
        Greeting="Hey thats too late, its time to sleep"
    return Greeting
def welcome():
    r="Nice to meet you"
    print(f"{time()}, {r}")

def menu():
    print(" Choose which option do you want")
    print("1. recipes and costs")
    print("2. best recipes")
    print("3. ratings of the food")
    print("4. covid-19 precautions")
    print("5. quit")
    print()
    try:
        return int(input("enter your choice: "))
        print()
    except:
        print("only choose from [1-5] ")
def show_items():
    print("1 : chicken tandoori, 2 : Biryani, 3 : veg manchuria, 4 : Fried chicken, 5 : Burgers,  6 : Chicken soup, 7 : Rotis , 8 : French fries, 9 : salads ,10 : Bread omlet")


def items_costs(food_items):
    items={
        1 : "chicken tandoori - cost: Rs 250",
        2 : "Biryani - cost: Rs 200",
        3 : "veg manchuria - cost: Rs 150",
        4 : "Fried chicken - cost: Rs 300",
        5 : "Burgers - cost: Rs 200",
        6 : "Chicken soup - cost: Rs 125",
        7 : "Rotis - cost: Rs 50",
        8 : "French fries - cost: Rs 199",
        9 : "salads - cost: Rs 100",
       10 : "Bread omlet - cost: Rs 75",
    }
    print(items.get(food_items, "you pick invalid choice"))

    

def best_items():
    print("1. Chicken tandoori")
    print("2. Biryani")
    print("3. salads")
    print("4. French fries")
    print("5. Chicken soup")
    print("6. Burgers")
    print()

def ratings_of_food():
    print("*. 4 stars for chicken tandoori")
    print("*. 5 stars for biryani")
    print("*. 3.8 stars for salads")
    print("*. 4.5 stars for French fries")
    print("*. 4.3 stars for Chicken soup")
    print("*. 4.1 stars for Burgers")
    print()

def covid_precautions():
    print("1. Maintain Social distance")
    print("2. Use sanitizer")
    print("3. Use mask")
    print("4. Wash your hands properly")
    print()    

def bot():
    greet()
    welcome()
    choice=menu()
    while choice!=5:
        if choice==1:
            show_items()
            food_items=int(input("Enter the choice of food item"))
            items_costs(food_items)
        elif choice==2:
            best_items()
        elif choice==3:
            ratings_of_food()
        elif choice==4:
            covid_precautions()
        else:
            print("I dont understand that")
        choice=menu()
bot()