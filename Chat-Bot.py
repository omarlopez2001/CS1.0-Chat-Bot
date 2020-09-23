from random import choice

def get_bot_response(user_response):

    bot_response_hawks = ["I love Atl!", "Go Hawks!", "Trae Young's the best!"]
    bot_response_celtics = ["Go Celtics!", "One of the best!", "Great young team!"]
    bot_response_nets = ["KD and Kyrie!", "Go Nets!", "Nets > Knicks!"]
    bot_response_hornets = ["I love the Jordan jerseys!", "Go Hornets!", "All Fly!"]
    bot_response_bulls = ["Go Bulls!", "Bull eyes!", "I love Chicago"]
    bot_response_cavs = ["The Land!", "Cleveland, this is for you!", "Go Cavs!"]
    bot_response_mavs = ["Luka Doncic is my favorite!", "Go Mavs!", "Dallas In!"]
    bot_response_nuggets = ["Go Nuggets!", "Let the Denver Madness Begin!", "Yes We Can!"]
    bot_response_pistons = ["Go Pistons!", "We're the best five alive!", "Deeetroit vs Everybody!"]
    bot_response_warriorrs = ["Splash Bros!", "Dub Nation!", "Go Warriors!"]
    bot_response_rockets = ["H-Town!", "The Beard", "Go Rockets!"]
    bot_response_pacers = ["Go Pacers!", "Great fight in the bubble!", "We Grow Basketball Here!"]
    bot_response_clippers = ["Battle for LA!", "The Claw!", "Go Clippers!"]
    bot_response_lakers = ["LAbron James!", "Mamba!", "Love the Mamba jerseys!"]
    bot_response_grizzlies = ["Ja Morant, Rookie of the Year!", "I love Memphis!", "Go Grizzlies!"]
    bot_response_heat = ["Go Heat!", "United in Black!", "Miami is FUN!"]
    bot_response_bucks = ["The Greek Freak!", "Go Bucks!", "Fear the Deer!"]
    bot_response_timberwolves = ["Who are you drafting?!", "Go Timberwolves!", "Minnesota is cold!"]
    bot_response_pelicans = ["Go Pelicans!", "ZION!", "Won't Bow Down!"]
    bot_response_knicks = ["Bad luck in the lottery :(", "Go Knicks!", "Once a Knick, Always a Knick!"]
    bot_response_thunder = ["Go Thunder!", "Roar Like Thunder!", "I love OKC!"]
    bot_response_magic = ["Go Magic!", "Love the Disney jerseys!", "I love Orlando!"]
    bot_response_76ers = ["Go 76ers!", "Trust the Process!", "Go Philly!"]
    bot_response_suns = ["We Are PHX!", "Go Suns!", "Devin Booker is the best!"]
    bot_response_blazers = ["RIP City!", "Go Blazers!", "Have you heard Dame's new track?"]
    bot_response_kings = ["Sacramento Proud!", "Go Kings!", "I love Sacramento!"]
    bot_response_spurs = ["Go Spurs Go!", "Spurs Basketball!", "Legendary franchise!"]
    bot_response_raptors = ["We The North!", "I love Canada!", "Go Raptors!"]
    bot_response_jazz = ["Go Jazz!", "Keep the Jazz Bumpin'", "Donovan Mitchell is the best!"]
    bot_response_wizards = ["Go Wizards", "DC Family!", "Rep the District!"]

    if user_response == "atlanta hawks":
        return choice(bot_response_hawks)
    elif user_response == "boston celtics":
        return choice(bot_response_celtics)
    elif user_response == "brooklyn nets":
        return choice(bot_response_nets)
    elif user_response == "charlotte hornets":
        return choice(bot_response_hornets)
    elif user_response == "chicago bulls":
        return choice(bot_response_bulls)
    elif user_response == "cleveland cavaliers":
        return choice(bot_response_cavs)
    elif user_response == "dallas mavericks":
        return choice(bot_response_mavs)
    elif user_response == "denver nuggets":
        return choice(bot_response_nuggets)
    elif user_response == "detroit pistons":
        return choice(bot_response_pistons)
    elif user_response == "golden state warriors":
        return choice(bot_response_warriorrs)
    elif user_response == "houston rockets":
        return choice(bot_response_rockets)
    elif user_response == "indiana pacers":
        return choice(bot_response_pacers)
    elif user_response == "la clippers":
        return choice(bot_response_clippers)
    elif user_response == "la lakers":
        return choice(bot_response_lakers)
    elif user_response == "memphis grizzlies":
        return choice(bot_response_grizzlies)
    elif user_response == "miami heat":
        return choice(bot_response_heat)
    elif user_response == "milwaukee bucks":
        return choice(bot_response_bucks)
    elif user_response == "minnesota timberwolves":
        return choice(bot_response_timberwolves)
    elif user_response == "new orleans pelicans":
        return choice(bot_response_pelicans)
    elif user_response == "new york knicks":
        return choice(bot_response_knicks)
    elif user_response == "oklahoma city thunder":
        return choice(bot_response_thunder)
    elif user_response == "orlando magic":
        return choice(bot_response_magic)
    elif user_response == "philadelphia 76ers":
        return choice(bot_response_76ers)
    elif user_response == "phoenix suns":
        return choice(bot_response_suns)
    elif user_response == "portland trail blazers":
        return choice(bot_response_blazers)
    elif user_response == "sacramento kings":
        return choice(bot_response_kings)
    elif user_response == "san antonio spurs":
        return choice(bot_response_spurs)
    elif user_response == "toronto raptors":
        return choice(bot_response_raptors)
    elif user_response == "utah jazz":
        return choice(bot_response_jazz)
    elif user_response == "washington wizards":
        return choice(bot_response_wizards)
    else:
        return "I do not recognize that team :("

print("Welcome to NBA Basketball Bot!")
print("Please enter your favorite NBA basketball team")

user_response = ""

while True:
    user_response = input("Which is your favorite basketball team?: ")
    if user_response == "done":
        break

    bot_response = get_bot_response(user_response)
    print(bot_response)