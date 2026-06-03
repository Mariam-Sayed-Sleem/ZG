import random
from Lists import home_events, roof_events, out_events, legend_events, ultra_legend_events

def rando_event(event_dictionary):
    events = list(event_dictionary.keys())
    weights = list(event_dictionary.values())
    return random.choices(events, weights=weights, k=1)[0]

def home_EV():
    return rando_event(home_events)

def roof_EV():
    return rando_event(roof_events)

def out_EV():
    return rando_event(out_events)

def LEGENDARY_EV():
    return rando_event(legend_events)

def ULTRA_EV():
    return rando_event(ultra_legend_events)