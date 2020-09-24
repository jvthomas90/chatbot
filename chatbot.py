#Library imports
from random import choice #for pseudo-random selection from lists in order to respond more "organically"
import webbrowser #for opening online resource materials related to certain responses

#Function definition
def get_bot_response(user_response): #Checks user-input for certain keywords and returns a response for output
    if "quot" in user_response: #This partial ensures recognition of variations in "quote" like quotes, quoted, quoting, quotation, quotatable, quotability, quoth, etc... 
                                #unfortunately, it also triggers with unrellated words like "quotient" so 🤷🏼‍♂️ sortof a plethora-of-pros/edge-case-con situation #featureORbug?
        pearls_of_wisdom=["Live long and prosper 🖖🏼\n", "2 plus 2 is 4, minus 1 that's 3 - quick maths!\n", "Never run with scissors!!! ε=ε=ε=(╯°□°)╯✂️\n"]
        return choice(pearls_of_wisdom)
    elif "productiv" in user_response: #catches conversational use of "productive" such as "productively," "productivity," etc 
        prodivity_topics = ["gtd","priority","autofocus","pomodoro"]
        chosen_topic = choice(prodivity_topics)
        if chosen_topic == "gtd": #Getting Things Done methodology, i.e. "Collect+Organize, Defer+Delegate, Engage+Review"
            webbrowser.open("https://gettingthingsdone.com/")
            return "Read 'GTD: The Art of Stress Free Productivity' by David Allen to improve your project-planning methodology 🗂📈\n"
        elif chosen_topic == "priority": #Importance vs Urgency in decision making. Also check out I.C.E. matrices for prioritization!
            webbrowser.open("https://www.developgoodhabits.com/eisenhower-matrix/")
            return "Learn about Eisenhower's 'priority-matrix' method for decision-making! ◳🤔\n"
        elif chosen_topic == "autofocus": #Simple, straightforward, and suuuuuper-effective list... it's just a list. But still! 🤯
            webbrowser.open("http://markforster.squarespace.com/autofocus-system/")
            return "Single-task effectively with Mark Forster's 'AutoFocus' list technique ✅📝\n"
        elif chosen_topic == "pomodoro": #Time and energy management for maintaining high efficacy and quality throughput throughout
            webbrowser.open("https://www.forbes.com/sites/bryancollinseurope/2020/03/03/the-pomodoro-technique/")
            return "For peak-performance, your brain needs to relax in 5-15 minute diffuse-mode time-blocks in between 30 minute focused-work sessions ⏳🧠\n"
    elif "music" in user_response: #The proper spelling of "music" can also cover "musical",  "musically",  "musician" etc as well
        tunes = ["classically classy classic","modernized classic","scatt","djent","edm"]
        chosen_tune = choice(tunes)
        if chosen_tune == "classically classy classic": #Confutatis! Maledictis!! Flamis acribus addictis!!! #WolfGang🐺
            webbrowser.open("https://www.youtube.com/watch?v=USe-wZ0AOQQ")
            return "The 'Confutatis' movement of Mozart's 'Requiem in D minor' is a classic that I thoroughly enjoy!\n"
        elif chosen_tune == "modernized classic": #Courtesy of Tina S
            webbrowser.open("https://www.youtube.com/watch?v=o6rBK0BqL2w")
            return "Check out this cool cover of Ludwig Van Beethoven's 'Moonlight Sonata' (3rd Movement)\n"
        elif chosen_tune == "scatt": #Scattman John scatting the opening lyrics of "Scattman"
            webbrowser.open("https://www.youtube.com/watch?v=Hy8kmNEo1i8")
            return "Ska-badabadabadoo-belidabbelydabbladabbladabblabab-belibabbelibabbelibabbelabbelo-doobelidoo\n"
        elif chosen_tune == "djent": #Excerpt from the Oxford Dictionary definition of djent, by a true djentleman!
            webbrowser.open("https://www.youtube.com/watch?v=YTkuJ4vRQZM")
            return "Pika paka. Pika paka! I pick up a pancake. Ah, pick uppa pan-cake! uh-pi-pa-ka-ka pika-paka-pop-pup-pa-PwWhaAAah!!! a-chigga-chugga BA-NA-NAAA!!!!!!\n"
        elif chosen_tune == "edm": #Best intro to electronic-dance-music (and specifically dubstep) that there ever was, period.
            webbrowser.open("https://www.youtube.com/watch?v=JkYhneTczXo")
            return "Here is 'A Brief Intro to Dubstep' by Dubba Johnny to get you started ;)\n"
    else: #Non-sequitor nonsense, just for the giggles
        default_responses = ["The cake is a lie! 🍰\n", "There is no spoon! 🥄\n", "Yer a wizard, Harry! 🧙🏼‍♂️\n","To exit chat, type 'done'\n"]
        return choice(default_responses)

#Program starts here
print("Greetings and salutations, human! I am chatbot 🤝\n") #Hello World! 👋🏼

#Prompt outlines optional topics of interest to discuss with the chatbot
print('''- I can tell you some curious quotes to mull and muse over, 
- or we can talk about musical melodies I think you might like, 
- or perhaps even insightful and informative productivity advice!\n''')

while True: #indefinite loop 
    user_response = input("What topic would you like to explore further? ") #prompt and save input
    if user_response == "done": #escape clause
        break #break out of while-loop on keyword
    else:
        print(get_bot_response(user_response)) #get bot response to user input and print to screen
        continue #restart while-loop... gotta keep that convo alive!
exit #End of program
