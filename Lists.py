from functions import scene
import Scenes

HOME = [
    ("BrokenWindow", 15),
    ("FoodSpoilage", 15),
    ("StrangeNoiseUpstairs", 12), 
    ("BarricadeWeakening", 10),
    ("RatInfestation", 9), 
    ("MysteriousKnock", 9),
    ("HiddenSupplies", 6), 
    ("RadioBroadcast", 5),
    ("SupplyDrop", 3), 
    ("FriendlySurvivor", 2),
    ("InjuredSurvivor", 3), 
    ("PetReturns", 1),
    ("FamilyPhotoFound", 1)
]

ROOF = [
    ("ZombieHordeSpotted", 18), 
    ("DistantSmoke", 14),
    ("RoofLeak", 12),
    ("BirdFlockExplosion", 10),
    ("StrayCatAppears", 10), 
    ("SolarPanelMalfunction", 9),
    ("ZombieClimber", 8), 
    ("RooftopGarden", 6),
    ("SupplyCrateFalls", 3), 
    ("SniperSurvivorWaves", 2),
    ("RadioSignalDetected", 2), 
    ("SunkenWaterTankFound", 1),
    ("MysteriousFlashlight", 1)
]

OUT = [
    ("ZombieHoard", 20), 
    ("LootedSupermarket", 16),
    ("ZombiePackSubway", 15), 
    ("SeagullStealsSandwich", 12),
    ("PoliceBarricadeStanding", 10),
    ("AbandonedMilitaryConvoy", 9), 
    ("WildDogsHunting", 8),
    ("BrokenDownArmoredVehicle", 7), 
    ("AbandonedSafeZoneSigns", 6),
    ("AirRaidSiren", 5), 
    ("MilitaryAirstrike", 3),
    ("MassGraves", 2), 
    ("EvacHelicopterLandingAttempt", 1),
    ("RadioTowerActive", 1)
]

LEGEND = [
    ("BusinessZombie", 0.3),
    ("TheRadioPlaysNeverGonnaGiveYouUp", 0.1)
]

ULTRA = [
    ("DeveloperAppearsInWorld", 0.01),
    ("PotatoKingEncounter", 0.01)
]


ALL = HOME + ROOF + OUT + LEGEND + ULTRA

event_pool = {name: getattr(Scenes, name) for name, _ in ALL}

event_weights = {name: weight for name, weight in ALL}



home_events         = {name: w for name, w in HOME}
roof_events         = {name: w for name, w in ROOF}
out_events          = {name: w for name, w in OUT}
legend_events       = {name: w for name, w in LEGEND}
ultra_legend_events = {name: w for name, w in ULTRA}