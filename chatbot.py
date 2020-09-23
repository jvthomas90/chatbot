from random import choice
import webbrowser

def get_bot_response(user_response):
    if "quote" in user_response:
        pearls_of_wisdom=["Live long and prosper 🖖🏼", "2 plus 2 is 4, minus 1 that's 3 - quick maths!", "Never run with scissors!!! ε=ε=ε=(╯°□°)╯✂️"]
        return choice(pearls_of_wisdom)
    elif "productiv" in user_response:
        prodivity_topics = ["gtd","priority","autofocus","pomodoro"]
        chosen_topic = choice(prodivity_topics)
        if chosen_topic == "gtd":
            webbrowser.open("https://gettingthingsdone.com/")
            return "Read 'GTD: The Art of Stress Free Productivity' by David Allen to improve your project-planning methodology 🗂📈"
        elif chosen_topic == "priority":
            webbrowser.open("https://www.developgoodhabits.com/eisenhower-matrix/")
            return "Learn about Eisenhower's 'priority-matrix' method for decision-making! ◳🤔"
        elif chosen_topic == "autofocus":
            webbrowser.open("http://markforster.squarespace.com/autofocus-system/")
            return "Single-task effectively with Mark Forster's 'AutoFocus' list technique ✅📝"
        elif chosen_topic == "pomodoro":
            webbrowser.open("https://www.forbes.com/sites/bryancollinseurope/2020/03/03/the-pomodoro-technique/")
            return "For peak-performance, your brain needs to relax in 5-15 minute diffuse mode time-blocks in between 30 minute focused-work sessions ⏳🧠"
    elif "music" in user_response:
        tunes = ["classically classy classic","modernized classic","scatt","djent","edm"]
        chosen_tune = choice(tunes)
        if chosen_tune == "classically classy classic":
            webbrowser.open("https://www.youtube.com/watch?v=USe-wZ0AOQQ")
            return "The 'Confutatis' movement of Mozart's 'Requiem in D minor' is a classic that I thoroughly enjoy!"
        elif chosen_tune == "modernized classic":
            webbrowser.open("https://www.youtube.com/watch?v=o6rBK0BqL2w")
            return "Check out this cool cover of Ludwig Van Beethoven's 'Moonlight Sonata' (3rd Movement)"
        elif chosen_tune == "scatt":
            webbrowser.open("https://www.youtube.com/watch?v=Hy8kmNEo1i8")
            return "Ska-badabadabadoo-belidabbelydabbladabbladabblabab-belibabbelibabbelibabbelabbelo-doobelidoo"
        elif chosen_tune == "djent":
            webbrowser.open("https://www.youtube.com/watch?v=YTkuJ4vRQZM")
            return "Pika paka. Pika paka! I pick up a pancake. Ah, pick uppa pan-cake! uh-pi-pa-ka-ka pika-paka-pop-pup-pa-PwWhaAAah!!! a-chigga-chugga BA-NA-NAAA!!!!!!"
        elif chosen_tune == "edm":
            webbrowser.open("https://www.youtube.com/watch?v=JkYhneTczXo")
            return "Here is 'A Brief Intro to Dubstep' by Dubba Johnny to get you started ;)"
    else:
        default_responses = ["The cake is a lie! 🍰", "There is no spoon! 🥄", "Yer a wizard, Harry! 🧙🏼‍♂️","To exit chat, type 'done'"]
        return choice(default_responses)

print("Greetings and salutations, human! I am chatbot 🤝\n")
print("I can tell you some curious quotes to mull and muse over, or we can talk about musical melodies I think you might like, or perhaps even insightful and informative productivity advice!\n")
user_response = ""

while True:
    user_response = input("What topic would you like to explore further? ")
    
    if user_response == "done":
        break
    else:
        print(get_bot_response(user_response))
        continue
