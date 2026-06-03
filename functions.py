from music import background, zombie, typer, typer2, suspense
import time
# Defining per Letter Delay (LD)
def type(text, delay=0.05):
    for char in text:
        print(char, end="", flush=True)
        if char != " ":
            typer.play()
        time.sleep(delay)
    print()
def longtype(text, delay=0.5):
    for char in text:
        print(char, end="", flush=True)
        if char != " ":
            typer2.play()
        time.sleep(delay)
    print()
# ---------------------------------------#
# Defining per Sentence Delay (SD)
def scene(*scenes, pause_time=1.5, use_type=True, delay=0.05):
    for message in scenes:
        if use_type:
            type(message, delay=delay)
        else:
            print(message)
        time.sleep(pause_time)