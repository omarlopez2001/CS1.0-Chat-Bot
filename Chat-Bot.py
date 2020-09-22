def get_bot_response(user_response)

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

if user_response == ["hawks", "Hawks", "Atlanta Hawks", "atlanta hawks"]:
    return choice(bot_response_hawks)
elif user_response == ["celtics", "Celtics", "Boston Celtics", "boston celtics"]:
    return choice(bot_response_celtics)
elif user_response == ["nets", "Nets", "Brooklyn Nets", "brooklyn nets"]:
    return choice(bot_response_nets)
elif user_response == ["hornets", "Hornets", "Charlotte Hornets", "charlotte hornets"]:
    return choice(bot_response_hornets)
elif user_response == ["bulls", "Bulls", "Chicago Bulls", "chicago bulls"]:
    return choice(bot_response_bulls)
elif user_response == ["cavs", "Cavs", "Cleveland Cavaliers", "cleveland cavaliers"]:
    return choice(bot_response_cavs)
elif user_response == ["mavs", "Mavs", "Dallas Mavericks", "dallas mavericks"]:
    return choice(bot_response_mavs)
elif user_response == ["nuggets", "Nuggets", "Denver Nuggets", "denver nuggets"]:
    return choice(bot_response_nuggets)
elif user_response == ["pistons", "Pistons", "Detroit Pistons", "detroit pistons"]:
    return choice(bot_response_pistons)
elif user_response == ["warriors", "Warriors", "Golden State Warriors", "golden state warriors"]:
    return choice(bot_response_warriorrs)
elif user_response == ["rockets", "Rockets", "Houston Rockets", "houston rockets"]:
    return choice(bot_response_rockets)
elif user_response == ["pacers", "Pacers", "Indiana Pacers", "indiana pacers"]:
    return choice(bot_response_pacers)
elif user_response == ["clippers", "Clippers" "LA Clippers", "la clippers"]:
    return choice(bot_response_clippers)
elif user_response == ["lakers", "Lakers", "LA Lakers", "la lakers"]:
    return choice(bot_response_lakers)
elif user_response == ["grizzlies", "Grizzlies", "Memphis Grizzlies", "memphis grizzlies"]:
    return choice(bot_response_grizzlies)
elif user_response == ["heat", "Heat", "Miami Heat", "miami heat"]:
    return choice(bot_response_heat)
elif user_response == ["bucks", "Bucks", "Milwaukee Bucks", "milwaukee bucks"]:
    return choice(bot_response_bucks)
elif user_response == ["timberwolves", "Timberwolves", "Minnesota Timberwolves", "minnesota timberwolves"]:
    return choice(bot_response_timberwolves)
elif user_response == ["pelicans", "Pelicans", "New Orleans Pelicans", "new orleans pelicans"]:
    return choice(bot_response_pelicans)
elif user_response == ["knicks", "Knicks", "New York Knicks", "new york knicks"]:
    return choice(bot_response_knicks)
elif user_response == ["thunder", "Thunder", "Oklahoma City Thunder", "oklahoma city thunder"]:
    return choice(bot_response_thunder)
elif user_response == ["magic", "Magic", "Orlando Magic", "orlando magic"]:
    return choice(bot_response_magic)
elif user_response == ["76ers", "Philadelphia 76ers", "philadelphia 76ers"]:
    return choice(bot_response_76ers)
elif user_response == ["suns", "Suns", "Phoenix Suns", "phoenix suns"]:
    return choice(bot_response_suns)
elif user_response == ["blazers", "Blazers", "Portland Trail Blazers", "portland trail blazers"]:
    return choice(bot_response_blazers)
elif user_response == ["kings", "Kings", "Sacramento Kings", "sacramento kings"]:
    return choice(bot_response_kings)
elif user_response == ["spurs", "Spurs", "San Antonio Spurs", "san antonio spurs"]:
    return choice(bot_response_spurs)
elif user_response == ["raptors", "Raptors", "Toronto Raptors", "toronto raptors"]:
    return choice(bot_response_raptors)
elif user_response == ["jazz", "Jazz", "Utah Jazz", "utah jazz"]:
    return choice(bot_response_jazz)
elif user_response == ["wizards", "Wizards", "Washington Wizards", "washington wizards"]:
    return choice(bot_response_wizards)
else:
    return "I do not recognize that team :("