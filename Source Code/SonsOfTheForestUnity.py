from time import sleep
from uniref import WinUniRef

ref = WinUniRef("SonsOfTheForest.exe")
local_player = ref.find_class_in_image("Sons.dll", "TheForest.Utils.LocalPlayer")
vitals_instance = local_player.find_field("<Vitals>k__BackingField").value
vitals = ref.find_class_in_image("Sons.dll", "Vitals")

def UnlimitedStats():
    vitals.set_instance(vitals_instance)
    health_instance = vitals.find_field("_health").value
    health_stat = ref.find_class_in_image("Sons.StatSystem.dll", "Sons.StatSystem.HealthStat")
    health_stat.set_instance(health_instance)
    health = health_stat.find_field("_currentValue")

    hydration_instance = vitals.find_field("_hydration").value
    hydration_stat = ref.find_class_in_image("Sons.StatSystem.dll", "Sons.StatSystem.HydrationStat")
    hydration_stat.set_instance(hydration_instance)
    hydration = hydration_stat.find_field("_currentValue")

    stamina_instance = vitals.find_field("_stamina").value
    stamina_stat = ref.find_class_in_image("Sons.StatSystem.dll", "Sons.StatSystem.StaminaStat")
    stamina_stat.set_instance(stamina_instance)
    stamina = stamina_stat.find_field("_currentValue")

    fullness_instance = vitals.find_field("_fullness").value
    fullness_stat = ref.find_class_in_image("Sons.StatSystem.dll", "Sons.StatSystem.FullnessStat")
    fullness_stat.set_instance(fullness_instance)
    fullness = fullness_stat.find_field("_currentValue")

    rested_instance = vitals.find_field("_rested").value
    rested_stat = ref.find_class_in_image("Sons.StatSystem.dll", "Sons.StatSystem.RestedStat")
    rested_stat.set_instance(rested_instance)
    rested = rested_stat.find_field("_currentValue")
    while True:
        health.value = 100.0
        hydration.value = 100.0
        stamina.value = 100.0
        fullness.value = 100.0
        rested.value = 100.0
        sleep(0.8)
def MaxStrength():
    vitals.find_field("_currentStrengthLevel").value = vitals.find_field("_maxStrengthLevel").value
def UnlimitedEnergy(toggle : bool):
    cheat_energy = ref.find_class_in_image("Sons.dll", "Cheats")
    cheat_energy.find_field("InfiniteEnergy").value = toggle
def SpeedHack(toggle : bool):
    fpc_instance = local_player.find_field("<FpCharacter>k__BackingField").value
    fpc = ref.find_class_in_image("Sons.dll", "FirstPersonCharacter")
    fpc.set_instance(fpc_instance)

    speeds = ["_runSpeed", "_swimSpeed", "crouchSpeed"]
    for speed in speeds:
        speed_field = fpc.find_field(speed)
        origin_value = speed_field.value
        speed_field.value = origin_value * 8 if toggle else origin_value / 8

    fpc.find_field("_baseFallDamage").value = 0.0 if toggle else 20.0
    fpc.find_field("_fallDamagePower").value = 0.0 if toggle else 2.0
def GodMode():
    inf_health = ref.find_class_in_image("Sons.dll", "Cheats")
    inf_health.find_field("GodMode").value = True