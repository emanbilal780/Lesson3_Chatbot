import re, random
from colorama import Fore, init

init(autoreset=True)

destinations = {

    "beaches": ["Bali", "Maldives", "Phuket"],
    "mountains": ["Swiss Alps", "Rocky Mountains", "Himalayas"],
    "cities": ["Tokyo", "Paris", "New York"]

}

jokes = [
    "Why don't programmers like nature? Too many bugs!",
    "Why did the computer go to the doctor? Because it had a virus!",
    "Why do travelers always feel warm? Because of all their hot spots!"

]

def normalize_input(text):

    return re.sub(r"\s+", " ", text.strip().lower())

def recommend():

    print(Fore.CYAN + "TravelBot: Beaches, mountains, or cities?")
    preference = input(Fore.YELLOW + "You: ")
    preference = normalize_input(preference)
    

    if preference in destinations:

        suggestion = random.choice(destinations[preference])

        print(Fore.GREEN + f"TravelBot: How about {suggestion}?")

        print(Fore.CYAN + "TravelBot: Do you like it? (yes/no)")

        answer = input(Fore.YELLOW + "You: ").lower()

        if answer == "yes":
            print(Fore.GREEN + f"TravelBot: Awesome! Enjoy {suggestion}!")

        elif answer == "no":
            print(Fore.RED + "TravelBot: Let's try another.")
            recommend()  # Recursive call if the user rejects the suggestion
        
        elif "time" in user_input or "clock" in user_input:

            local_time()

        else:
            print(Fore.RED + "TravelBot: I'll suggest again.")
            recommend()  # Recursive call on unrecognized answer

    else:
        print(Fore.RED + "TravelBot: Sorry, I don't have that type of destination.")

    show_help()
    
def packing_tips():

    print(Fore.CYAN + "TravelBot: Where to?")

    location = normalize_input(input(Fore.YELLOW + "You: "))

    print(Fore.CYAN + "TravelBot: How many days?")

    days = input(Fore.YELLOW + "You: ")

    

    print(Fore.GREEN + f"TravelBot: Packing tips for {days} days in {location}:")

    print(Fore.GREEN + "- Pack versatile clothes.")

    print(Fore.GREEN + "- Bring chargers/adapters.")

    print(Fore.GREEN + "- Check the weather forecast.")

def tell_joke():

    print(Fore.YELLOW + f"TravelBot: {random.choice(jokes)}")

def show_help():

    print(Fore.MAGENTA + "\nI can:")

    print(Fore.GREEN + "- Suggest travel spots (say 'recommendation')")

    print(Fore.GREEN + "- Offer packing tips (say 'packing')")

    print(Fore.GREEN + "- Tell a joke (say 'joke')")

    print(Fore.GREEN + "- Give budget tips (say 'budget')")

    print(Fore.CYAN + "Type 'exit' or 'bye' to end.\n")

    print(Fore.GREEN + "- Tell local time in a city (say 'time')")


def chat():

    print(Fore.CYAN + "Hello! I'm TravelBot.")

    name = input(Fore.YELLOW + "Your name? ")

    print(Fore.GREEN + f"Nice to meet you, {name}!")

    

    show_help()

    

    while True:

        user_input = input(Fore.YELLOW + f"{name}: ")

        user_input = normalize_input(user_input)

        

        if "recommend" in user_input or "suggest" in user_input:

            recommend()

        elif "pack" in user_input or "packing" in user_input:

            packing_tips()

        elif "joke" in user_input or "funny" in user_input:

            tell_joke()

        elif "help" in user_input:

            show_help()
        elif "budget" in user_input or "money" in user_input:

            budget_tip()

        elif "exit" in user_input or "bye" in user_input:

            print(Fore.CYAN + "TravelBot: Safe travels! Goodbye!")

            break

        else:

            print(Fore.RED + "TravelBot: Could you rephrase?")

def budget_tip():

    print(Fore.CYAN + "TravelBot: What's your budget in dollars?")

    budget = input(Fore.YELLOW + "You: ")

    if budget.isdigit():

        budget = int(budget)

        if budget < 500:
            print(Fore.GREEN + "TravelBot: Try a budget trip! Hostels and local food save a lot.")

        elif budget < 2000:
            print(Fore.GREEN + "TravelBot: A mid-range trip! Maybe a nice hotel and some tours.")

        else:
            print(Fore.GREEN + "TravelBot: Luxury trip time! Resorts, fine dining, the works!")

    else:
        print(Fore.RED + "TravelBot: Please enter numbers only, like 500.")

from datetime import datetime, timedelta

# Offset from UTC in hours for a few cities
city_offsets = {

    "tokyo": 9,
    "paris": 1,
    "new york": -4,
    "london": 1,
    "dubai": 4,
    "sydney": 10

}

def local_time():

    print(Fore.CYAN + "TravelBot: Which city? (Tokyo, Paris, New York, London, Dubai, Sydney)")

    city = normalize_input(input(Fore.YELLOW + "You: "))

    if city in city_offsets:

        offset = city_offsets[city]

        utc_now = datetime.utcnow()

        city_time = utc_now + timedelta(hours=offset)

        print(Fore.GREEN + f"TravelBot: It's currently {city_time.strftime('%I:%M %p')} in {city.title()}.")

    else:
        print(Fore.RED + "TravelBot: Sorry, I don't have that city yet.")

if __name__ == "__main__":

    chat()