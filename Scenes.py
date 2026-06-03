from functions import scene
import Settings as s
from music import TeleportIN, TeleportOUT, rickrolled, seagull

def BrokenWindow():
    scene("While you were searching for supplies, you heard the sound of breaking glass.")
    scene("A storm has broken one of your home's windows.")
    scene("What would you do?")
    scene("1. Fix it with wood")
    scene("2. Block it with blankets")
    scene("3. Ignore it")
    while True:
        choice = input("> ").strip()

        if choice == "1":
            scene("You board up the window with scrap wood. It won't hold forever, but it'll do.")
            s.SP += 3
            s.HP += 2
            s.HPg -= 3
            break
        elif choice == "2":
            scene("You stuff blankets into the gap. Cold air still seeps in, but it's better than nothing.")
            s.HP -= 3
            s.SP -= 2
            s.HPg -= 2
            break
        elif choice == "3":
            scene("You leave it. The wind howls through all night, and you wake up exhausted and cold.")
            s.HP -= 8
            s.SP -= 5
            s.HPg -= 3
            break
        else:
            scene("Invalid choice.")

def FoodsSPoilage():
    scene("You check your food supplies… something smells off.")
    scene("1. Eat it anyway")
    scene("2. Throw it away")
    scene("3. Risk cooking it")

    while True:
        choice = input("> ").strip()

        if choice == "1":
            scene("You eat it… your stomach regrets it.")
            s.HP -= 10
            s.HPg += 10
            s.SP -= 3
            break
        elif choice == "2":
            scene("You discard the spoiled food. Better safe than sorry.")
            s.HPg -= 8
            s.SP += 3
            s.HP += 1
            break
        elif choice == "3":
            scene("You try to salvage it by cooking… it mostly works.")
            s.HPg += 5
            s.SP -= 5
            s.HP -= 5
            break
        else:
            scene("Invalid choice.")

def StrangeNoiseUpstairs():
    scene("You hear slow footsteps upstairs…")
    scene("1. Investigate")
    scene("2. Hide and wait")
    scene("3. Shout at it")

    while True:
        choice = input("> ").strip()

        if choice == "1":
            scene("You slowly go upstairs… nothing is there. A loose shutter. You breathe again.")
            s.SP -= 5
            s.HP -= 2
            s.HPg += 3
            s.encounters_count += 1
            break
        elif choice == "2":
            scene("You stay hidden, waiting. The noise fades. You relax, but hunger sets in.")
            s.SP += 3
            s.HP -= 2
            s.HPg -= 3
            break
        elif choice == "3":
            scene("Your voice echoes… something hears you. Bad move.")
            s.SP -= 10
            s.HP -= 5
            s.HPg -= 5
            break
        else:
            scene("Invalid choice.")

def BarricadeWeakening():
    scene("Your barricade is cracking under pressure.")
    scene("1. Repair it properly")
    scene("2. Reinforce with furniture")
    scene("3. Ignore it")

    while True:
        choice = input("> ").strip()

        if choice == "1":
            scene("You patch the barricade carefully. It holds. You feel safer.")
            s.HPg -= 5
            s.SP += 5
            s.HP += 2
            break
        elif choice == "2":
            scene("You shove heavy furniture into place. Exhausting, but it works.")
            s.HPg -= 8
            s.HP -= 3
            s.SP += 2
            break
        elif choice == "3":
            scene("You ignore it… it worsens overnight. A draft and fear keep you up.")
            s.HP -= 10
            s.SP -= 5
            s.HPg -= 3
            break
        else:
            scene("Invalid choice.")

def RatInfestation():
    scene("Rats have invaded your supplies.")
    scene("1. Hunt them down")
    scene("2. Ignore them")
    scene("3. Set a trap")

    while True:
        choice = input("> ").strip()

        if choice == "1":
            scene("You drive them away. Tiring work, but your supplies are safe.")
            s.HPg += 8
            s.SP -= 5
            s.HP -= 2
            break
        elif choice == "2":
            scene("They slowly consume your food. You wake up to real damage.")
            s.HPg -= 10
            s.SP -= 3
            s.HP -= 2
            break
        elif choice == "3":
            scene("You set traps and recover supplies. Clean, smart, effective.")
            s.HPg += 12
            s.SP += 5
            s.HP += 2
            break
        else:
            scene("Invalid choice.")

def MysteriousKnock():
    scene("Someone is knocking on your door… slowly.")
    scene("1. Open it")
    scene("2. Ignore it")
    scene("3. Prepare a weapon and answer")

    while True:
        choice = input("> ").strip()

        if choice == "1":
            scene("A survivor appears, desperate but alive. You let them in cautiously.")
            s.TP += 5
            s.SP -= 3
            s.HP -= 2
            s.HPg -= 3
            break
        elif choice == "2":
            scene("The knocking continues for an hour… then stops. You feel the weight of that.")
            s.SP -= 8
            s.HP -= 2
            s.HPg -= 2
            break
        elif choice == "3":
            scene("You open it armed. Nothing there. You feel on edge the rest of the day.")
            s.SP -= 3
            s.HP += 1
            s.HPg -= 2
            break
        else:
            scene("Invalid choice.")

def HiddenSupplies():
    scene("While moving furniture, you discover a hidden panel in the floor.")
    scene("Inside, someone stashed supplies long ago. But opening it makes noise.")
    scene("1. Open it carefully and take everything")
    scene("2. Take only what you need and seal it back")
    scene("3. Leave it untouched — it could be a trap")
    while True:
        choice = input("> ").strip()

        if choice == "1":
            scene("You pry it open. Inside: canned food, a flashlight, and a first aid kit. Jackpot.")
            s.HPg += 15
            s.SP += 8
            s.HP += 5
            break
        elif choice == "2":
            scene("You take a few cans and a bandage, then carefully reseal the hatch. Smart.")
            s.HPg += 8
            s.HP += 5
            s.SP += 3
            break
        elif choice == "3":
            scene("You back away slowly. Maybe it was nothing. Maybe not. The paranoia costs you sleep.")
            s.SP -= 5
            s.HP -= 2
            s.HPg -= 2
            break
        else:
            scene("Invalid choice.")

def RadioBroadcast():
    scene("A broken radio crackles to life.")
    scene("1. Listen carefully")
    scene("2. Ignore it")
    scene("3. Try to repair it")

    while True:
        choice = input("> ").strip()

        if choice == "1":
            scene("You hear survivors talking… coordinates mentioned. Hope, faint but real.")
            s.SP += 5
            s.HP += 2
            s.HPg += 2
            break
        elif choice == "2":
            scene("You turn it off. Silence again. You missed something, you can feel it.")
            s.SP -= 3
            s.HP -= 1
            s.HPg -= 2
            break
        elif choice == "3":
            scene("You fix the signal. Clear voices come through. A huge morale lift.")
            s.SP += 8
            s.HP += 3
            s.HPg += 3
            break
        else:
            scene("Invalid choice.")

def SupplyDrop():
    scene("A military helicopter roars overhead and drops a crate nearby.")
    scene("It lands two blocks away. You saw it. Others might have too.")
    scene("1. Rush to it immediately")
    scene("2. Wait and watch before approaching")
    scene("3. Ignore it — could be bait")
    while True:
        choice = input("> ").strip()

        if choice == "1":
            scene("You sprint to the crate. Rations, medicine, ammo. You grab it all before anyone arrives.")
            s.HPg += 20
            s.SP += 5
            s.HP -= 5
            break
        elif choice == "2":
            scene("You wait. A zombie wanders past the crate, then moves on. You retrieve it safely.")
            s.HPg += 15
            s.SP += 5
            s.HP += 3
            break
        elif choice == "3":
            scene("You stay put. Gunshots echo from that direction ten minutes later. Good call.")
            s.SP += 5
            s.HP += 2
            s.HPg -= 3
            break
        else:
            scene("Invalid choice.")

def FriendlySurvivor():
    scene("A person waves at you from across the street. They look exhausted but unthreatening.")
    scene("They're calling out: 'Please — I just need water.'")
    scene("1. Invite them in")
    scene("2. Toss supplies from a distance")
    scene("3. Turn them away")
    while True:
        choice = input("> ").strip()

        if choice == "1":
            scene("You let them in. They're grateful and share information about a nearby safe house.")
            s.TP += 10
            s.HPg -= 8
            s.SP += 5
            s.HP += 3
            break
        elif choice == "2":
            scene("You slide a bottle of water across the street. They nod thankfully and move on.")
            s.TP += 5
            s.HPg -= 3
            s.SP += 3
            s.HP += 1
            break
        elif choice == "3":
            scene("You shake your head. They stare for a long moment, then disappear into the ruins.")
            s.TP -= 8
            s.SP -= 5
            s.HP -= 2
            s.HPg += 2
            break
        else:
            scene("Invalid choice.")

def InjuredSurvivor():
    scene("A wounded survivor collapses near your door. They're bleeding badly.")
    scene("1. Treat their wounds fully")
    scene("2. Give basic supplies and send them off")
    scene("3. Ignore them")
    while True:
        choice = input("> ").strip()

        if choice == "1":
            scene("You bandage them through the night. They recover and offer to help defend your shelter.")
            s.TP += 12
            s.HPg -= 10
            s.SP += 5
            s.HP += 5
            break
        elif choice == "2":
            scene("You hand over a bandage and a tin of food. They manage to walk away.")
            s.TP += 6
            s.HPg -= 5
            s.SP += 2
            s.HP += 1
            break
        elif choice == "3":
            scene("You watch from the window. They don't make it through the night. The guilt is heavy.")
            s.TP -= 10
            s.SP -= 5
            s.HP -= 3
            s.HPg += 2
            break
        else:
            scene("Invalid choice.")

def PetReturns():
    scene("Scratching at the back door. You open it — it's your dog. Thin, scared, but alive.")
    scene("1. Let them in and feed them properly")
    scene("2. Let them in but ration their food carefully")
    scene("3. Keep them outside — too risky")
    while True:
        choice = input("> ").strip()

        if choice == "1":
            scene("You let them in and feed them properly. Their tail wags. You feel almost human again.")
            s.HPg -= 8
            s.SP += 12
            s.HP += 5
            break
        elif choice == "2":
            scene("You let them in and share small portions. They curl up beside you. It helps.")
            s.HPg -= 4
            s.SP += 8
            s.HP += 3
            break
        elif choice == "3":
            scene("You close the door. Their whimpering fades. You stare at the wall for a long time.")
            s.SP -= 10
            s.HP -= 3
            s.HPg += 1
            break
        else:
            scene("Invalid choice.")

def FamilyPhotoFound():
    scene("While clearing debris, you find a family photo album, undamaged.")
    scene("It's not yours — but the smiling faces feel real.")
    scene("1. Keep it — a reminder of what you're surviving for")
    scene("2. Leave it where it belongs")
    scene("3. Use the pages as kindling")
    while True:
        choice = input("> ").strip()

        if choice == "1":
            scene("You tuck it into your bag. On dark nights, you'll look at it.")
            s.SP += 8
            s.HP += 3
            s.HPg += 1
            break
        elif choice == "2":
            scene("You set it back carefully on the rubble. Some things shouldn't be moved.")
            s.SP -= 2
            s.HP += 3
            s.HPg += 1
            break
        elif choice == "3":
            scene("You tear out the pages and feed the fire. You don't think about it too hard.")
            s.SP -= 8
            s.HP += 2
            s.HPg += 3
            break
        else:
            scene("Invalid choice.")

def ZombieHordesSPotted():
    scene("From your window you see a massive horde moving slowly down your street.")
    scene("1. Hide completely and go silent")
    scene("2. Create a distraction to redirect them")
    scene("3. Reinforce your barricades right now")
    while True:
        choice = input("> ").strip()

        if choice == "1":
            scene("You kill every light and hold your breath. Three hours later, the horde passes.")
            s.SP += 5
            s.HP -= 5
            s.HPg -= 5
            break
        elif choice == "2":
            scene("You throw a noise-maker down the alley. The horde turns. It works — barely.")
            s.HPg -= 8
            s.SP -= 5
            s.HP -= 3
            break
        elif choice == "3":
            scene("You spend the horde's approach reinforcing every entry point. They pass without breaching.")
            s.HPg -= 10
            s.SP += 8
            s.HP += 2
            break
        else:
            scene("Invalid choice.")

def DistantSmoke():
    scene("A dark column of smoke rises from a few blocks away.")
    scene("1. Investigate")
    scene("2. Stay put and monitor from a distance")
    scene("3. Use the distraction to scavenge elsewhere")
    while True:
        choice = input("> ").strip()

        if choice == "1":
            scene("You find a burnt-out pharmacy. Scorched shelves, but some medicine survived in the back.")
            s.HPg += 10
            s.HP -= 5
            s.SP -= 3
            break
        elif choice == "2":
            scene("You watch the smoke thin and disappear. Nothing comes your way. Quiet day.")
            s.SP += 3
            s.HP += 2
            s.HPg += 1
            break
        elif choice == "3":
            scene("While everyone else is drawn toward the smoke, you slip into an unguarded shop. Good haul.")
            s.HPg += 15
            s.SP += 3
            s.HP += 2
            break
        else:
            scene("Invalid choice.")

def RoofLeak():
    scene("Water drips steadily through your ceiling. A section of roof has given way.")
    scene("1. Patch it with tarp and rope")
    scene("2. Move supplies away from the wet area")
    scene("3. Ignore it")
    while True:
        choice = input("> ").strip()

        if choice == "1":
            scene("You climb up and stretch the tarp across the gap. It holds. Dry shelter restored.")
            s.SP -= 5
            s.HP += 5
            s.HPg += 3
            break
        elif choice == "2":
            scene("You relocate your supplies to a dry corner. Not ideal, but everything stays usable.")
            s.HPg -= 3
            s.SP += 2
            s.HP += 1
            break
        elif choice == "3":
            scene("The dripping keeps you up all night. By morning, a box of food is ruined with mold.")
            s.HP -= 8
            s.HPg -= 5
            s.SP -= 3
            break
        else:
            scene("Invalid choice.")

def BirdFlockExplosion():
    scene("Hundreds of birds suddenly burst from the rooftops around you, screeching into the sky.")
    scene("Something scared them. Something nearby.")
    scene("1. Take cover immediately")
    scene("2. Climb to high ground to see what's coming")
    scene("3. Keep moving and hope it passes")
    while True:
        choice = input("> ").strip()

        if choice == "1":
            scene("You duck into a doorway. A small zombie pack shambles past. They don't notice you.")
            s.SP += 5
            s.HP += 2
            s.HPg += 1
            break
        elif choice == "2":
            scene("You scramble onto a fire escape. You spot the horde before it reaches you — valuable intel.")
            s.SP += 8
            s.HP -= 3
            s.HPg += 2
            break
        elif choice == "3":
            scene("You keep walking. The horde clips you at the edge. You escape but take a hit.")
            s.SP -= 8
            s.HP -= 10
            s.HPg -= 3
            break
        else:
            scene("Invalid choice.")

def StrayCatAppears():
    scene("A skinny tabby cat slips through a gap in your wall and stares at you.")
    scene("1. Feed it and keep it")
    scene("2. Shoo it back out")
    scene("3. It's protein. You're desperate.")
    while True:
        choice = input("> ").strip()

        if choice == "1":
            scene("You share a bit of food. The cat curls up near the door. It's nice to not be alone.")
            s.HPg -= 4
            s.SP += 10
            s.HP += 3
            break
        elif choice == "2":
            scene("You wave it back out. It vanishes without a sound. Probably for the best.")
            s.HPg += 2
            s.SP -= 2
            s.HP += 1
            break
        elif choice == "3":
            scene("You do what you have to. You don't feel great about it, but your stomach stops hurting.")
            s.SP -= 12
            s.HP += 8
            s.HPg += 5
            break
        else:
            scene("Invalid choice.")

def SolarPanelMalfunction():
    scene("Your solar panel setup has shorted out. No power for lighting or your radio.")
    scene("1. Attempt repairs yourself")
    scene("2. Cannibalize it for parts to use elsewhere")
    scene("3. Leave it and conserve battery reserves")
    while True:
        choice = input("> ").strip()

        if choice == "1":
            scene("After hours of fiddling, you get it working again. Dim light flickers on. Victory.")
            s.SP -= 5
            s.HP += 5
            s.HPg += 3
            break
        elif choice == "2":
            scene("You strip the wiring and rig a hand crank lamp. Resourceful.")
            s.SP += 5
            s.HP += 2
            s.HPg += 2
            break
        elif choice == "3":
            scene("You ration your batteries carefully. They last three more days. Plan B needed.")
            s.SP -= 5
            s.HP -= 2
            s.HPg -= 2
            break
        else:
            scene("Invalid choice.")

def ZombieClimber():
    scene("Something is scraping up the outside of your wall. A zombie has learned to climb.")
    scene("1. Push it off from above")
    scene("2. Barricade the upper floor access")
    scene("3. Flee to the lower floor and seal the stairs")
    while True:
        choice = input("> ").strip()

        if choice == "1":
            scene("You lean out and shove it off with a plank. It doesn't get back up.")
            s.HP -= 8
            s.SP += 5
            s.HPg -= 3
            break
        elif choice == "2":
            scene("You pile furniture against the upper hatch. It claws at it all night but can't get through.")
            s.HPg -= 8
            s.SP += 3
            s.HP += 2
            break
        elif choice == "3":
            scene("You seal the stairs and wait. It eventually loses interest and drops off.")
            s.SP -= 5
            s.HPg -= 5
            s.HP -= 2
            break
        else:
            scene("Invalid choice.")

def RooftopGarden():
    scene("You find a rooftop with old planter boxes — some still have soil. You have seeds.")
    scene("1. Plant everything now")
    scene("2. Plant a small test batch first")
    scene("3. Ignore it — too exposed")
    while True:
        choice = input("> ").strip()

        if choice == "1":
            scene("You spend the day planting. In two weeks, green shoots appear. Food security, finally.")
            s.HPg += 20
            s.SP -= 8
            s.HP -= 3
            break
        elif choice == "2":
            scene("You plant a few rows cautiously. They grow. You'll expand next week.")
            s.HPg += 10
            s.SP -= 3
            s.HP += 1
            break
        elif choice == "3":
            scene("You leave it. The planters dry out and die. A missed opportunity haunts you.")
            s.HPg -= 5
            s.SP -= 3
            s.HP -= 2
            break
        else:
            scene("Invalid choice.")

def SupplyCrateFalls():
    scene("You were hauling a supply crate up a rope when it slips — crashing into the alley below.")
    scene("The noise was loud.")
    scene("1. Retrieve it fast before anything arrives")
    scene("2. Leave it and stay hidden")
    scene("3. Drop a distraction and then recover it")
    while True:
        choice = input("> ").strip()

        if choice == "1":
            scene("You sprint down. You grab the crate and get back inside just as shadows round the corner.")
            s.HP -= 8
            s.HPg += 15
            s.SP -= 3
            break
        elif choice == "2":
            scene("You pull back from the window. The crate is looted by the time you check. At least you're safe.")
            s.SP += 5
            s.HPg -= 12
            s.HP += 1
            break
        elif choice == "3":
            scene("You roll a bottle down the opposite alley. The distraction works. You recover the crate clean.")
            s.HPg += 12
            s.SP += 2
            s.HP += 2
            break
        else:
            scene("Invalid choice.")

def SniperSurvivorWaves():
    scene("A survivor on a distant rooftop is waving at you with a piece of cloth.")
    scene("They appear to be signaling, not threatening.")
    scene("1. Wave back and approach cautiously")
    scene("2. Signal back but stay put")
    scene("3. Ignore them")
    while True:
        choice = input("> ").strip()

        if choice == "1":
            scene("You make your way over. They're a medic with antibiotics. A valuable ally found.")
            s.TP += 12
            s.HP += 8
            s.SP -= 5
            s.HPg += 5
            break
        elif choice == "2":
            scene("You wave back. They nod and disappear. A small mutual acknowledgment. Not alone.")
            s.TP += 5
            s.SP += 3
            s.HP += 2
            s.HPg += 1
            break
        elif choice == "3":
            scene("You turn away. The figure eventually stops waving. You'll wonder about them later.")
            s.TP -= 5
            s.SP -= 3
            s.HP -= 1
            s.HPg -= 1
            break
        else:
            scene("Invalid choice.")

def RadioSignalDetected():
    scene("Your receiver picks up a repeating signal — coordinates and a time. Structured. Intentional.")
    scene("1. Head to the coordinates")
    scene("2. Broadcast a response first and wait")
    scene("3. Ignore it — could be a lure")
    while True:
        choice = input("> ").strip()

        if choice == "1":
            scene("You follow the signal. A small survivor camp. Cautious faces — but real people.")
            s.TP += 15
            s.HPg += 10
            s.HP -= 5
            s.SP += 3
            break
        elif choice == "2":
            scene("You broadcast back. A voice responds. They confirm the meet. Safer arrival.")
            s.TP += 10
            s.SP += 5
            s.HP += 2
            s.HPg += 3
            break
        elif choice == "3":
            scene("You leave the signal unanswered. The broadcast eventually goes silent. You'll never know.")
            s.TP -= 8
            s.SP += 3
            s.HP -= 1
            s.HPg -= 2
            break
        else:
            scene("Invalid choice.")

def SunkenWaterTankFound():
    scene("You find a buried cistern behind a collapsed building — still sealed, possibly full of water.")
    scene("1. Crack it open and test it")
    scene("2. Use your filter kit to safely process it")
    scene("3. Mark it and come back with proper gear")
    while True:
        choice = input("> ").strip()

        if choice == "1":
            scene("The water looks okay. You fill your containers. You feel fine. Probably fine.")
            s.HPg += 12
            s.HP -= 5
            s.SP += 2
            break
        elif choice == "2":
            scene("You filter and boil a full supply. Clean water secured. Your tools take a toll.")
            s.HPg += 20
            s.SP -= 5
            s.HP += 3
            break
        elif choice == "3":
            scene("You scratch an X on the wall and head back. You'll return with the right kit.")
            s.SP += 5
            s.HP += 1
            s.HPg -= 2
            break
        else:
            scene("Invalid choice.")

def MysteriousFlashlight():
    scene("A flashlight blinks in Morse code from an alley below. Someone is signaling you.")
    scene("1. Signal back with your own torch")
    scene("2. Watch silently and try to decode the message")
    scene("3. Douse your lights and stay hidden")
    while True:
        choice = input("> ").strip()

        if choice == "1":
            scene("You flash back. A figure emerges — a child. Alone. Scared. You take them in.")
            s.TP += 10
            s.HPg -= 8
            s.SP += 5
            s.HP += 2
            break
        elif choice == "2":
            scene("You decode it slowly: 'HELP — TRAPPED — BUILDING 4.' You file the information away.")
            s.SP += 8
            s.HP += 2
            s.HPg += 2
            break
        elif choice == "3":
            scene("You kill your lights and wait. The signal stops. You feel the weight of that decision.")
            s.SP -= 5
            s.HP -= 2
            s.HPg -= 3
            break
        else:
            scene("Invalid choice.")

def ZombieHoard():
    scene("Your shelter is surrounded. Dozens of them, pressing against every wall.")
    scene("1. Fight your way through the weakest point")
    scene("2. Hold out and wait them out")
    scene("3. Create a loud distraction far from your position")
    while True:
        choice = input("> ").strip()

        if choice == "1":
            scene("You burst through the side wall, swinging hard. You make it out, barely.")
            s.HP -= 20
            s.SP += 5
            s.HPg -= 8
            break
        elif choice == "2":
            scene("You seal every crack and ration supplies for two days. They finally dis.SPerse.")
            s.HPg -= 15
            s.SP -= 10
            s.HP -= 5
            break
        elif choice == "3":
            scene("You rig a noise trap three blocks away and trigger it remotely. The horde follows the sound.")
            s.HPg -= 10
            s.SP += 8
            s.HP += 3
            break
        else:
            scene("Invalid choice.")

def LootedSupermarket():
    scene("You find a supermarket — mostly stripped, but the back storage room is untouched.")
    scene("1. Take everything you can carry")
    scene("2. Take only what fits quietly")
    scene("3. Set up a hidden stash for later")
    while True:
        choice = input("> ").strip()

        if choice == "1":
            scene("You load up every bag. Halfway out, something stirs in the aisle. You run for it.")
            s.HPg += 25
            s.HP -= 8
            s.SP -= 5
            break
        elif choice == "2":
            scene("You fill two bags quietly and slip out the back. Clean exit, solid haul.")
            s.HPg += 15
            s.SP += 3
            s.HP += 2
            break
        elif choice == "3":
            scene("You seal the room and mark it carefully. A personal supply depot. Genius.")
            s.HPg += 10
            s.SP += 8
            s.HP += 2
            break
        else:
            scene("Invalid choice.")

def ZombiePackSubway():
    scene("The subway tunnel ahead echoes with shuffling. A full pack blocks your route.")
    scene("1. Fight through with whatever you have")
    scene("2. Find an alternate route")
    scene("3. Lure them into a side tunnel and slip past")
    while True:
        choice = input("> ").strip()

        if choice == "1":
            scene("You carve through the pack. Bloody but through. There's a supply cache on the other side.")
            s.HP -= 18
            s.HPg += 20
            s.SP -= 5
            break
        elif choice == "2":
            scene("You backtrack and find an overhead route through the station roof. Safe but exhausting.")
            s.SP -= 8
            s.HP -= 3
            s.HPg -= 3
            break
        elif choice == "3":
            scene("You roll a can down a side tunnel. They follow the sound. You glide past in silence.")
            s.HPg -= 5
            s.SP += 5
            s.HP += 2
            break
        else:
            scene("Invalid choice.")

def PoliceBarricadeStanding():
    scene("An old police barricade still stands across the road, mostly intact.")
    scene("1. Dismantle it for materials")
    scene("2. Use it as a defensive post for scouting")
    scene("3. Leave it — it might deter threats passively")
    while True:
        choice = input("> ").strip()

        if choice == "1":
            scene("You strip the barricade for metal and wood. Good raw material for shelter upgrades.")
            s.SP -= 5
            s.HPg += 5
            s.HP += 3
            break
        elif choice == "2":
            scene("You set up a makeshift lookout post. Better awareness of what's coming down the block.")
            s.SP += 10
            s.HP += 3
            s.HPg += 2
            break
        elif choice == "3":
            scene("You leave it standing. A few zombies bump into it and wander off. Small victories.")
            s.SP += 3
            s.HP += 1
            s.HPg += 1
            break
        else:
            scene("Invalid choice.")

def AbandonedMilitaryConvoy():
    scene("Three military trucks sit abandoned on the highway, doors open, engines cold.")
    scene("1. Loot the vehicles thoroughly")
    scene("2. Check quickly and leave — convoys draw attention")
    scene("3. Siphon the fuel and go")
    while True:
        choice = input("> ").strip()

        if choice == "1":
            scene("You find ammo crates, armors, and a field medkit. Best haul in weeks.")
            s.HPg += 25
            s.HP += 10
            s.SP -= 5
            break
        elif choice == "2":
            scene("You grab two more packs and a radio and walk. Smart. The area starts getting noisy.")
            s.HPg += 12
            s.SP += 3
            s.HP += 2
            break
        elif choice == "3":
            scene("You drain two full tanks. The generator back home gets another two weeks of power.")
            s.SP += 10
            s.HP += 5
            s.HPg += 5
            break
        else:
            scene("Invalid choice.")

def SniperFireEchoes():
    scene("Shots crack through the air — a sniper somewhere, picking off zombies or people, you can't tell.")
    scene("1. Move toward the shots — could be military or allies")
    scene("2. Stay low and cross quickly to cover")
    scene("3. Retreat and reroute — not worth it")
    while True:
        choice = input("> ").strip()

        if choice == "1":
            scene("It's a lone survivor clearing a path. Wary at first, they nod and let you pass safely.")
            s.TP += 8
            s.HP -= 3
            s.SP += 2
            s.HPg += 3
            break
        elif choice == "2":
            scene("You sprint low between cars and make it across. The shots continue behind you.")
            s.SP += 5
            s.HP += 1
            s.HPg += 1
            break
        elif choice == "3":
            scene("You go three blocks around. It takes an hour but you arrive unscathed.")
            s.SP += 3
            s.HPg -= 5
            s.HP += 1
            break
        else:
            scene("Invalid choice.")

def WildDogsHunting():
    scene("A pack of feral dogs has been trailing you for two blocks. They're getting closer.")
    scene("1. Stand your ground and scare them off")
    scene("2. Climb to higher ground and wait")
    scene("3. Throw food to distract them")
    while True:
        choice = input("> ").strip()

        if choice == "1":
            scene("You turn, shout, and bang metal together. The pack scatters. Adrenaline fades slowly.")
            s.SP -= 5
            s.HP -= 3
            s.HPg -= 2
            break
        elif choice == "2":
            scene("You scale a fire escape. They circle below for twenty minutes, then lose interest.")
            s.SP += 5
            s.HP += 1
            s.HPg -= 2
            break
        elif choice == "3":
            scene("You toss your last tin of sardines. They pounce on it. You walk away free.")
            s.HPg -= 8
            s.SP += 8
            s.HP += 2
            break
        else:
            scene("Invalid choice.")

def BrokenDownArmoredVehicle():
    scene("An armored personnel carrier sits wedged in an intersection — engine dead, hatch open.")
    scene("1. Search the interior thoroughly")
    scene("2. Use it as a temporary fortified shelter for the night")
    scene("3. Strip usable parts for your own shelter")
    while True:
        choice = input("> ").strip()

        if choice == "1":
            scene("Inside: two MREs, a flare gun, and a field dressing. You take it all.")
            s.HPg += 15
            s.HP += 8
            s.SP += 3
            break
        elif choice == "2":
            scene("You pull the hatch shut and sleep inside the steel walls. First real rest in days.")
            s.SP += 12
            s.HP += 5
            s.HPg += 3
            break
        elif choice == "3":
            scene("You unbolt plating and haul armored panels back to your shelter. Excellent fortification.")
            s.SP -= 5
            s.HP += 3
            s.HPg += 5
            break
        else:
            scene("Invalid choice.")

def AbandonedSafeZoneSigns():
    scene("Faded government signs point to a 'Safe Zone — 2 miles.' The arrows are sun-bleached and old.")
    scene("1. Follow them — maybe someone is still there")
    scene("2. Investigate cautiously before committing")
    scene("3. Ignore them — safe zones fell months ago")
    while True:
        choice = input("> ").strip()

        if choice == "1":
            scene("You follow the signs. The safe zone is overrun — but the supply depot beside it isn't.")
            s.TP += 5
            s.HPg += 18
            s.HP -= 10
            s.SP -= 3
            break
        elif choice == "2":
            scene("You scout from a rooftop first. The zone is empty — but quiet. You move through safely.")
            s.SP += 8
            s.HPg += 8
            s.HP += 3
            break
        elif choice == "3":
            scene("You keep walking. You were right — the zone was a graveyard. Smart call.")
            s.SP += 5
            s.HP += 2
            s.HPg += 1
            break
        else:
            scene("Invalid choice.")

def AirRaidSiren():
    scene("An old air raid siren blares to life somewhere in the city — someone activated it manually.")
    scene("1. Head toward the siren — it's a signal")
    scene("2. Use the noise as cover to move and scavenge")
    scene("3. Seal your shelter — the noise will draw a horde")
    while True:
        choice = input("> ").strip()

        if choice == "1":
            scene("You find a small militia group using the siren to gather survivors. Tense, but promising.")
            s.TP += 12
            s.HP -= 5
            s.SP += 3
            s.HPg += 5
            break
        elif choice == "2":
            scene("You move quickly while the zombies track the siren. Empty three buildings before it stops.")
            s.HPg += 18
            s.SP -= 3
            s.HP += 2
            break
        elif choice == "3":
            scene("You board up and wait. The horde passes your block following the sound. Safe.")
            s.SP += 8
            s.HP += 3
            s.HPg -= 3
            break
        else:
            scene("Invalid choice.")

def MilitaryAirstrike():
    scene("Jets scream overhead. An airstrike is incoming — targeting the dense zombie mass downtown.")
    scene("1. Get to the basement immediately")
    scene("2. Watch from a distance — could reveal cleared zones")
    scene("3. Use the chaos to raid nearby buildings")
    while True:
        choice = input("> ").strip()

        if choice == "1":
            scene("You hit the basement hard. The building shakes. Dust falls. You emerge unharmed.")
            s.SP += 8
            s.HP += 3
            s.HPg += 2
            break
        elif choice == "2":
            scene("The blast clears six blocks. You mark the cleared zone on your mental map.")
            s.SP += 10
            s.HP -= 5
            s.HPg += 3
            break
        elif choice == "3":
            scene("You rush a pharmacy mid-blast. Shrapnel clips you — but your bag is full.")
            s.HPg += 20
            s.HP -= 12
            s.SP -= 3
            break
        else:
            scene("Invalid choice.")

def MassGraves():
    scene("You stumble onto a mass grave at the edge of the city. Hundreds. Civilian clothing.")
    scene("This changes what you thought you knew about the outbreak.")
    scene("1. Search for identification — maybe someone you knew")
    scene("2. Mark the location and document it")
    scene("3. Walk away quickly. You don't need to know.")
    while True:
        choice = input("> ").strip()

        if choice == "1":
            scene("You find a name you recognize. A neighbor. You sit with it for a while. Then you walk on.")
            s.SP -= 15
            s.HP -= 5
            s.HPg -= 3
            break
        elif choice == "2":
            scene("You note the location, the numbers, the signs. Someone has to remember. You will.")
            s.SP -= 8
            s.HP -= 2
            s.HPg -= 2
            break
        elif choice == "3":
            scene("You don't look. You keep moving. Some things cost too much to know.")
            s.SP -= 5
            s.HP += 1
            s.HPg += 1
            break
        else:
            scene("Invalid choice.")

def EvacHelicopterLandingAttempt():
    scene("A military helicopter circles low, searching for a landing zone. It's looking for survivors.")
    scene("1. Signal them immediately")
    scene("2. Wait — it could be a trap")
    scene("3. Signal but stay armed — don't trust them fully")
    while True:
        choice = input("> ").strip()

        if choice == "1":
            scene("You wave frantically. The helicopter spots you and lands. They take you to a forward camp.")
            s.TP += 20
            s.HP += 15
            s.SP += 8
            s.HPg += 10
            break
        elif choice == "2":
            scene("You watch the helicopter leave. It was real. The window is gone. That'll stay with you.")
            s.TP -= 10
            s.SP -= 8
            s.HP -= 3
            s.HPg -= 5
            break
        elif choice == "3":
            scene("You signal carefully, staying in cover. They land. Tense standoff, then trust. You board.")
            s.TP += 12
            s.HP += 10
            s.SP -= 3
            s.HPg += 5
            break
        else:
            scene("Invalid choice.")

def RadioTowerActive():
    scene("A radio tower nearby is blinking — it's been reactivated. Someone has power.")
    scene("1. Climb it and broadcast your location")
    scene("2. Trace the power source — find who's running it")
    scene("3. Sabotage it — a signal this big will draw the wrong attention")
    while True:
        choice = input("> ").strip()

        if choice == "1":
            scene("You climb and broadcast. Within an hour, a response: coordinates. Someone heard you.")
            s.TP += 15
            s.HP -= 5
            s.SP += 5
            s.HPg += 3
            break
        elif choice == "2":
            scene("You trace the cables to a basement bunker. Eight survivors with a generator. A real group.")
            s.TP += 18
            s.SP += 5
            s.HP += 3
            s.HPg += 5
            break
        elif choice == "3":
            scene("You cut the transmitter line. The tower goes dark. You may have saved everyone nearby.")
            s.SP += 10
            s.HP += 2
            s.HPg += 2
            break
        else:
            scene("Invalid choice.")


# ______________________________________________________________ #

def BusinessZombie():
    scene("A zombie in a full business suit shuffles into view, briefcase still in hand.")
    scene("It makes eye contact — or something like it — and lurches toward you.")
    scene("1. Dodge and let it pass — too weird to deal with")
    scene("2. Check the briefcase — could be something useful")
    scene("3. Put it down with respect. It probably had a mortgage.")
    while True:
        choice = input("> ").strip()

        if choice == "1":
            scene("You sidestep it. It carries on walking into a wall. The briefcase rattles. You move on.")
            s.SP += 3
            s.HP += 1
            s.HPg += 1
            break
        elif choice == "2":
            scene("You pop the briefcase open. Inside: a laptop, a granola bar, and a USB labeled 'Q3 REPORT'.")
            scene("You eat the granola bar.")
            s.HPg += 5
            s.SP += 3
            s.HP += 2
            break
        elif choice == "3":
            scene("You handle it with quiet efficiency. You find yourself straightening its tie afterward. Strange day.")
            s.SP -= 5
            s.HP -= 1
            s.HPg -= 1
            break
        else:
            scene("Invalid choice.")

def TheRadioPlaysNeverGonnaGiveYouUp():
    scene("Your radio crackles. A signal. Clear as day.")
    rickrolled.play()
    scene("You recognize the first four notes immediately.")
    scene("You have been Rick Rolled during the apocalypse.")
    scene("1. Crank it up. This is the morale boost you needed.")
    scene("2. Turn it off. There is no joy left in this world.")
    scene("3. Broadcast it outward. Share the curse.")
    while True:
        choice = input("> ").strip()

        if choice == "1":
            scene("You dance alone in a ruined kitchen at the end of the world. It helps, somehow.")
            s.SP += 15
            s.HP += 3
            s.HPg += 2
            break
        elif choice == "2":
            scene("You click it off. Silence returns. You stare at the ceiling for a long time.")
            s.SP -= 8
            s.HP -= 2
            s.HPg -= 2
            break
        elif choice == "3":
            scene("You patch it to the external speaker and blast it across three blocks.")
            scene("Two survivors emerge from hiding, confused and laughing. You make unexpected friends.")
            s.TP += 10
            s.SP += 8
            s.HP += 3
            s.HPg += 3
            break
        else:
            scene("Invalid choice.")

def DeveloperAppearsInWorld():

    scene("A figure materializes in the middle of the street.")
    TeleportIN.play()
    scene("They're wearing a hoodie. They look very tired. They are holding a laptop.")
    scene("They look directly at you and say: 'I just wanted to test something real quick.'")
    scene("1. Ask them to fix the broken window event that was never finished")
    scene("2. Demand better loot tables. The RNG has been cruel.")
    scene("3. Offer them a granola bar. They look like they haven't slept.")
    while True:
        choice = input("> ").strip()

        if choice == "1":
            scene("They frown at their screen. 'Oh. Yeah. I'll push a patch.' They vanish.")
            TeleportOUT.play()
            scene("The window is now fixed. You feel the timeline shift slightly.")
            s.SP += 10
            s.HP += 3
            s.HPg += 3
            break
        elif choice == "2":
            scene("They sigh deeply, open a JSON file, and change a value.")
            scene("A supply crate falls from nowhere outside your door. You don't question it.")
            TeleportOUT.play()
            s.HPg += 20
            s.SP += 5
            s.HP += 5
            break
        elif choice == "3":
            scene("Their eyes widen. 'Oh... Thank you!'")
            scene("They accept it reverently. 'I'll remember this,' they say. Then they're gone.")
            TeleportOUT.play()
            s.TP += 50
            s.SP += 20
            s.HP += 75
            s.HPg -= 5
            break
        else:
            scene("Invalid choice.")

def PotatoKingEncounter():
    scene("You enter a building and find a man seated on a throne made entirely of canned potatoes.")
    scene("He is wearing a crown fashioned from a potato sack. He gestures grandly.")
    scene("'Welcome,' he says, 'to my kingdom.'")
    scene("1. Bow. You respect the commitment.")
    scene("2. Challenge his rule. There can only be one potato monarch.")
    scene("3. Trade with him. His economy is surprisingly robust.")
    while True:
        choice = input("> ").strip()

        if choice == "1":
            scene("He is moved. He grants you a can of potatoes and safe passage through his domain.")
            s.TP += 8
            s.SP += 8
            s.HPg += 5
            s.HP += 3
            break
        elif choice == "2":
            scene("You duel with a broom. It is undignified. You win. You are now the Potato King.")
            scene("The responsibility is immediate and immense.")
            s.HP -= 8
            s.HPg += 15
            s.SP -= 5
            break
        elif choice == "3":
            scene("You offer bottled water. He accepts. He gives you twelve cans of potatoes and a handshake.")
            s.TP += 10
            s.HPg += 18
            s.SP += 5
            s.HP += 3
            break
        else:
            scene("Invalid choice.")

def SeagullStealsSandwich():
    scene("You found a sealed sandwich in a vending machine. First real food in two days.")
    scene("You unwrap it carefully. You take one breath.")
    seagull.play()
    scene("A seagull hits you like a feathered missile and takes it.")
    scene("1. Chase it. That sandwich was yours.")
    scene("2. Accept your loss with dignity. You are better than this bird.")
    scene("3. Declare war on all seagulls. Start planning.")
    while True:
        choice = input("> ").strip()

        if choice == "1":
            scene("You s.print after it for half a block.")
            scene("It drops the sandwich on a roof. You can't reach it.")
            scene("The seagull watches you from above. It appears to be judging you.")
            s.SP -= 8
            s.HP -= 3
            s.HPg -= 5
            break
        elif choice == "2":
            scene("You take a slow breath. You let it go. The seagull is just surviving too.")
            scene("You respect that, a little. You go find something else to eat.")
            s.HPg -= 5
            s.SP += 5
            s.HP -= 1
            break
        elif choice == "3":
            scene("You pull out your notebook and begin sketching traps.")
            scene("You have never felt more focused. More alive. More certain of your purpose.")
            s.SP += 10
            s.HP += 2
            s.HPg -= 3
            break
        else:
            scene("Invalid choice.")