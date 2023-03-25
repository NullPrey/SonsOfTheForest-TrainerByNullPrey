import dearpygui.dearpygui as dear_ui
import dearpygui
import os as i
import SonsOfTheForestUnity as un

def SonsOfTheForest_UnlimitedEnergy():
    un.UnlimitedEnergy(True)
def SetUnlStats():
    un.UnlimitedStats()
def MAXSTRENGTH_SONSOFTHEFOREST():
    un.MaxStrength()
def Speedhack():
    un.SpeedHack(True)
def Donation():
    print("Soon")
def Godmode():
    un.GodMode()
def SetupUI():
    width, height, channels, data = dear_ui.load_image(i.getcwd() + "\\Setting\\SonsOfTheForestTrainerByNullPrey.jpg")
    dear_ui.create_context()
    with dear_ui.font_registry():
        dejavu_sans = dear_ui.add_font(i.getcwd() + "\\Setting\\DejaVuSans-BoldOblique.ttf", 16)
    dear_ui.create_viewport(title='SonsOfTheForest Trainer', resizable=False, min_width=725, min_height=725, max_height=725, max_width=725)
    dear_ui.setup_dearpygui()
    with dear_ui.texture_registry():
            image_texture = dear_ui.add_static_texture(width, height, data)
    with dear_ui.window(label="Sons Of The Forest Trainer", width=725, height=725, no_close=True, no_move=True, no_resize=True, no_collapse=True):
            dear_ui.add_image(image_texture) # Adding Image Texture :D
            dear_ui.add_text("Sons Of The Forest Trainer by NullPrey", color=[0, 125, 0])
            dear_ui.add_checkbox(label="Unlimited Energy", callback=SonsOfTheForest_UnlimitedEnergy)
            dear_ui.add_checkbox(label="Unlimited Stats", callback=SetUnlStats)
            dear_ui.add_checkbox(label="MAX STRENGTH", callback=MAXSTRENGTH_SONSOFTHEFOREST)
            dear_ui.add_checkbox(label="SET SPEEDHACK", callback=Speedhack)
            dear_ui.add_checkbox(label="GodMode", callback=Godmode)
            with dear_ui.menu_bar():
                with dear_ui.menu(label='ABOUT'):
                    dear_ui.add_text("It's Fully Updated Version of My Trainer for Game Sons Of The Forest... Enjoy!!!", color=[211, 44, 44])
                    dear_ui.add_text("Soon Donation for NullPrey :3", color=[0, 150, 55])
                    dear_ui.add_button(label="Donation", callback=Donation)
    dear_ui.bind_font(dejavu_sans)
    dear_ui.show_viewport()
    dear_ui.start_dearpygui()
    dear_ui.destroy_context()