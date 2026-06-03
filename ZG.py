# adding Libraries
import random
import time
from functions import longtype, scene, type
from Lists import event_pool
from music import background, suspense, zombie
from Randomizer import LEGENDARY_EV, home_EV, roof_EV, out_EV
import Settings as s
from Settings import Days, Max_Days

# ---------------------------------------#
# Settings
day = Days
# ---------------------------------------#
# Defining Events for Intro
def intro():
    scene("One day, while you were watching TV at home, enjoying your favourite TV show.")
    scene("It was almost peaceful...")
    longtype("Almost..")
    scene("that was before the broadcast was interrupted by breaking news—")
    scene("'Zombies broke out, as mindless corpses are spreading around the city at a global rate'")
    scene("'Beware and Stay at your Homes—', before the screen cuts to static as a zombie attacks.")
    zombie.play()
    scene("You stare at the screen in disbelief, but a chilling sound from outside confirms your worst fears to be true.")
    scene("before the lights in your home flicker and go dull as the generator dies off")
# ---------------------------------------#
# --->> Game Code starts here <<---#
scene("This is Game Assistance for ZG (‾◡◝)")
scene("Insert your character name:")
name = input("> ").strip()
# Character name recheck
if len(name) < 3:
    scene("Is that a shortcut or a typo? (￣yv￣)╭")
    scene("Wanna like...")
    scene("redo your.... name?")
    scene("last Chance..")
    scene("Press 1 for Yes / Press 2 for No")
    choice = input("> ").strip()
    if choice == "1":
        scene("Insert your character name")
        scene("again")
        longtype("...")
        name = input("> ").strip()
    elif choice == "2":
        scene("uhmmm...")
        scene("Okay!")
        scene("I can get along with " + name + " as a name!")
# ---------------------------------------#
scene("Hello " + name + "! (•̀ ω •́ )")
scene("In this game, you'd have to survive zombies invading the city for 30 days to win this game! (((o(*ﾟ▽ﾟ*)o)))")
# ----------------------------------------#
# Resume game condition
scene("Would you like to start the journey? ( •_•)>⌐■-■")
scene("Press 1 for Yes / Press 2 for No")
cont = input("> ").strip()
while cont not in ["1", "2"]:
    scene("Excuse me! ＞﹏＜")
    scene("I said 1 or 2!")
    cont = input("> ").strip()
if cont == "1":
    scene("Starting game in")
    try:
        background.play(loops=-1)
    except:
        pass
    scene("3")
    scene("2")
    scene("1")
    longtype("..........")
    intro()
    try:
        suspense.play()
    except:
        pass
    scene(f"DAY {day}")
else:
    scene("Game Closed. See you next time. ¯\\_(ツ)_/¯")
    exit()
# ---------------------------------------#
# Main Game Loop
while day <= Max_Days:
    scene(f"\n=== DAY {day} ===")
    print(
    f"\nHunger: {s.hunger_tier()} ({s.HPg:.1f}/100) | "
    f"Sanity: {s.sanity_tier()} ({s.SP:.1f}/100) | "
    f"Health: {s.health_tier()} ({s.HP:.1f}/100)"
    )
    if s.HP <= 0:
        break
    scene("Where do you want to spend today?")
    scene("1. Stay Home")
    scene("2. Go to the Rooftop")
    scene("3. Go Outside")
    location_choice = input("> ").strip()
    if location_choice == "1":
        event_key = home_EV()
    elif location_choice == "2":
        event_key = roof_EV()
    elif location_choice == "3":
        event_key = out_EV()
    else:
        scene("Nuh uh!")
        scene("Wrong Typo, Try again!")
        continue
    if event_key in event_pool:
        event_func = event_pool[event_key]
        event_func()
    else:
        scene("Event error occurred...")
    if random.random() < 0.08: # Legendary Event Chance
        try:
            legend_key = LEGENDARY_EV()
            if legend_key in event_pool:
                event_pool[legend_key]()
        except Exception:
            pass
    day += 1
# ---------------------------------------#
# End Game
if day > Max_Days:
    scene(f"\n🎉 CONGRATULATIONS {name.upper()}! YOU SURVIVED 30 DAYS! 🎉")
    scene("You Win!")
else:
    scene("\nYour journey has ended...")