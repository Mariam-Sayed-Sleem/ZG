import time
import random

Days = 1
Max_Days = 30
HPg = 100.00      # Hunger Points (0 to 100)
SP = 100.00       # Sanity Points (-1 to 100)
HP = 100.00       # Health Points (0 to 100)
TP = 0.00         # Trust Points (-100 to 100) (((BTW, I know it can also be refering to Tuberculosis of some sorts, but dw, it's TP, not TB!)))

    
def hunger_tier():
    if HPg >= 75: return "Well Fed"
    if HPg >= 50: return "Hungry"
    if HPg >= 25: return "Starving"
    return "Dying"

def sanity_tier():
    if SP >= 75: return "Stable"
    if SP >= 50: return "Anxious"
    if SP >= 25: return "Paranoid"
    return "Breaking"

def health_tier():
    if HP >= 75: return "Healthy"
    if HP >= 50: return "Hurt"
    if HP >= 25: return "Wounded"
    return "Critical"