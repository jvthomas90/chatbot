from random import choice

def get_bot_response(user_response):
	if "quote" in user_response:
		return choice["Live long and prosper 🖖🏼", "2 plus 2 is 4, minus 1 that's 3 - quick maths!", "Never run with scissors!!! ε=ε=ε=(╯°□°)╯✂️"]
	elif "produvtiv" in user_response:
		prod_topic = random.choice("gtd","priority","autofocus","pomodoro")
		if prod_topic == "gtd":
			return "Read 'Getting Things Done' by David Allen to improve your project-planning methodology 🗂📈"
        elif prod_topic == "priority":
            return "Learn about Eisenhower's 'priority-matrix' method for decision-making! ◳🤔"
        elif prod_topic == "autofocus":
            return "Single-task effectively with Mark Forster's 'AutoFocus' list technique ✅📝"
        elif prod_topic == "pomodoro":
            return "For peak-performance, your brain needs to relax in 5-15 minute diffuse mode time-blocks in between 30 minute focused-work sessions ⏳🧠"
	elif "music" in user_response:
		tunes = random["classical","scatt","edm"]
		if tunes == "classical"
			print("Confutatis movement of Mozart's 'Requiem in D minor'"")
			choice = input("Wanna listen? Y/N")
				if choice.upper() == "Y"
					web.open()
				else:
					pass/break/continue?
		elif tunes == "scatt"
			web.open(scattman)
			return "gibberish lorem ipsum here"
		else:
			???
	else
		return random.choice[default,responses,here]

user_response = ""

while True:
	user_response = input(prompt)

	if user_response = "done"
		break
	else
		get_bot_Response(user_response)
		continue
