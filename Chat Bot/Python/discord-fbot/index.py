from PIL import Image
import cv2 as cv
import discord
import math
import numpy as np
import time
import threading
import random
import requests

class Config():
    player_token = "x"
    bot_token = "x"
    channel = "x"
    
    player = None # No es necesario tocar
    player_name = None # No es necesario tocar
    player_mention = None # No es necesario tocar

    preferred_area = 1 # Area preferida para RPG AREA
    max_preferred = True # Fija el area maxima como preferida, ignora preferred_area

    adventure_heal_trigger = 10 # Disparador de HEAL para ADVENTURE
    hunt_heal_trigger = 10 # Disparador de HEAL para  HUNT

    is_hunt_enabled = True # True Activa HUNT
    is_adventure_enabled = True # True activa ADVENTURE
    is_training_enabled = True # True activa TRAINING
    is_quest_enabled = True # True activa QUEST
    is_work_enabled = True # True activa WORK
    is_farm_enabled = True # True gasta 4,000 y activa FARM
    is_buy_lootbox_enabled = True # True gasta el valor del LOOTBOX y activa compra de LOOTBOX

    hunt_hardmode_first = False # Prioriza HUNT HARDMODE en lugar de HUNT
    ultraining_first = False # Prioriza ULTRAINING en lugar de TRAINING
    epic_quest_first = False # Prioriza EPIC QUEST

    work1 = "mine"
    work2 = "mine"
    work3 = "mine"
    work4 = "mine"

    ultraining_choice = 'attack' # Elección en los ULTRAINING
    epic_quest_waves = 15 # Numero de oleadas para las EPIC QUEST
    farm_target = 'bread' # Objetivo de los FARM

    buy_edgylb = True # True gasta 420,666
    buy_epiclb = True # True gasta 150,000
    buy_rarelb = True # True gasta 40,000
    buy_uncommonlb = True # True gasta 6,000
    buy_commonlb = True # True gasta 800

    solve_epic_guard = True # Resuelve el captcha
    solve_events = True # Resuelve los eventos

    test_mode = True
    test_messages = False

class Aux():
    version = 'alpha_0.11.0'
    is_paused = False

    epic_prefix = '<@555955826880413696> '
    check = 0
    switch_work = 0
    last_work = ''
    last_found = ''
    
    megarace_notify_switch = False
    
    min_sec = 1
    max_sec = 4

    banana_patron = [(209, 135, 22),(225, 191, 0),(253, 215, 0)]
    is_banana = False

    apple_patron = [(38, 198, 86),(201, 120, 31),(219, 17, 28),(237, 28, 36),(240, 68, 77),]
    is_apple = False

    epic_coin_patron = [(1, 4, 139),(1, 5, 177),(17, 20, 162),(21, 26, 196),(22, 27, 194),(47, 21, 62),(48, 52, 231),(62, 29, 84),(74, 37, 173),(78, 35, 103),(106, 65, 214),(117, 48, 163),(121, 55, 121),(135, 61, 135),(152, 77, 202),(153, 68, 153),(154, 69, 154),(167, 75, 167),(184, 95, 184),(255, 244, 36),]
    is_epic_coin = False

    coin_patron = [(89, 85, 0),(149, 141, 0),(179, 170, 0),(217, 206, 0),(221, 210, 0),(239, 227, 0),(255, 242, 0),]
    is_coin = False

    wolf_skin_patron = [(49, 49, 55),(51, 51, 57),(57, 57, 64),(61, 61, 69),(63, 63, 68),(77, 62, 60),]
    is_wolf_skin = False
    
    epic_fish_patron = [(32, 107, 54),(32, 172, 74),(33, 71, 44),(33, 83, 48),(33, 176, 76),(34, 179, 77),(34, 184, 79),(35, 188, 81),(37, 197, 85),(103, 211, 41),]
    is_epic_fish = False

    normie_fish_patron = [(0, 141, 182),(0, 142, 183),(0, 155, 200),(0, 165, 213),(0, 198, 255),]
    is_normie_fish = False

    dragon_scale_patron = [(49, 8, 10),(54, 9, 11),(74, 12, 15),(119, 11, 16),(131, 14, 19),(155, 20, 26),(172, 24, 31),(185, 27, 35),(197, 30, 39),(212, 34, 43),(224, 37, 47),(237, 41, 51),]
    is_dragon_scale = False

    life_potion_patron = [(109, 64, 1),(198, 252, 255),(217, 17, 27),]
    is_life_potion = False

    golden_fish_patron = [(94, 74, 0),(192, 153, 0),(220, 176, 0),(255, 204, 0),]
    is_golden_fish = False

    zombie_eye_patron = [(77, 98, 11),(194, 235, 71),]
    is_zombie_eye = False

    unicorn_horn_patron = [(37, 34, 35),(39, 33, 35),(56, 21, 32),(255, 130, 170),(255, 144, 180),(255, 146, 181),(255, 148, 182),(255, 148, 183),(255, 153, 186),]
    is_unicorn_horn = False

    mermaid_hair_patron = [(0, 170, 242),(43, 191, 255),]
    is_mermaid_hair = False

    ruby_patron = [(115, 0, 0),(119, 0, 0),(120, 0, 0),(127, 0, 0),(134, 0, 0),(139, 0, 0),(158, 0, 0),(164, 0, 0),(170, 0, 0),(180, 0, 0),(196, 0, 0),(201, 1, 1),(225, 10, 10),(230, 0, 0),(249, 19, 19),(255, 21, 21),]
    is_ruby = False

    chip_patron = [(0, 28, 7),(19, 103, 45),(20, 106, 46),(22, 118, 51),(23, 121, 52),(25, 134, 58),(38, 200, 86),(39, 203, 88),(240, 233, 142),]
    is_chip = False

class Cooldown():
    daily = 0
    weekly = 0
    lootbox = 0
    vote = 0
    hunt = 0
    adventure = 0
    training = 0
    duel = 0
    quest = 0
    work = 0
    farm = 0
    horse = 0
    arena = 0
    dungeon = 0
    megarace = 0

class Stats():
    actual_area = 0
    max_area = 0
    life = 1
    coins = 0
    bank = 0
    actual_hp = 0
    max_hp = 0
    horse_boost = ''
    
class Inv():
    life_potion = 0
    basic_seeds = 0
    carrot_seeds = 0
    potato_seeds = 0
    bread_seeds = 0
    ruby = 0

bot = discord.Client()

@bot.event
async def on_ready():
    game = discord.Game("EPIC RPG for you.")
    await bot.change_presence(status=discord.Status.online, activity=game)
    print('Bot is ready')
    await bot.get_channel(int(Config.channel)).send('Bot is ready\nType ` EGO HELP ` to take a look to the bot commands')

@bot.event
async def on_connect():
    print('Bot is connected')
    await bot.get_channel(int(Config.channel)).send('Bot is connected')

@bot.event
async def on_disconnect():
    print('Bot is disconnected')
    sendMessage('Bot is disconnected')

@bot.event
async def on_message(message):
    msg_at = message.author
    msg_ch = message.channel
    msg_ct = message.content
    msg_eb = message.embeds
    cmd_parameter = msg_ct.split(" ", 100)

    if msg_at == bot.user:
        return

    if cmd_parameter[0].upper() == "EGO" or cmd_parameter[0].upper() == "E": 
        if len(cmd_parameter) > 1:

            if cmd_parameter[1].upper() == "DISABLE" or cmd_parameter[1].upper() == "D":
                if len(cmd_parameter) > 2:

                    if cmd_parameter[2].upper() == "ADVENTURE" or cmd_parameter[2].upper() == "AD":
                        if len(cmd_parameter) > 3:
                            None
                        else:
                            Config.is_adventure_enabled  = False
                            await msg_ch.send('Adventure is now disabled')

                    elif cmd_parameter[2].upper() == "ALL" or cmd_parameter[2].upper() == "A":
                        if len(cmd_parameter) > 3:
                            await msg_ch.send('Too much parameters.')

                        else:
                            Config.is_adventure_enabled  = False
                            Config.is_buy_lootbox_enabled = False
                            Config.is_farm_enabled = False
                            Config.is_hunt_enabled = False
                            Config.is_quest_enabled = False
                            Config.is_training_enabled = False
                            Config.is_work_enabled = False
                            Config.epic_quest_first = False
                            Config.ultraining_first = False
                            Config.hunt_hardmode_first = False
                            await msg_ch.send('Every command is now disabled')

                    elif cmd_parameter[2].upper() == "CAPTCHA" or cmd_parameter[2].upper() == "C":
                        if len(cmd_parameter) > 3:
                            None
                        else:
                            Config.solve_epic_guard  = False
                            await msg_ch.send('Captcha solving is now disabled')
                    
                    elif cmd_parameter[2].upper() == "EVENTS" or cmd_parameter[2].upper() == "E":
                        if len(cmd_parameter) > 3:
                            None
                        else:
                            Config.solve_events  = False
                            await msg_ch.send('Event solver is now disabled')

                    elif cmd_parameter[2].upper() == "FARM" or cmd_parameter[2].upper() == "F":
                        if len(cmd_parameter) > 3:
                            None
                        else:
                            Config.is_farm_enabled  = False
                            await msg_ch.send('Farm is now disabled')
                    
                    elif cmd_parameter[2].upper() == "HELP" or cmd_parameter[2].upper() == "H":
                        await msg_ch.send(
                            '**DISABLE COMMANDS:**\n'
                            +'**`ALL`**: (Disable all commands)\n'
                            +'**`ADVENTURE`**: (Disable adventure command)\n'
                            +'**`CAPTCHA`**: (Disable captcha solving)\n'
                            +'**`EVENTS`**: (Disable events solving)\n'
                            +'**`FARM`**: (Disable farm command)\n'
                            +'**`HUNT`**: (Disable hunt command)\n'
                            +'**`HUNT HARDMODE`**: (Disable hunt hardmode command)\n'
                            +'**`LOOTBOX`**: (Disable buy lootbox commands)\n'
                            +'**`QUEST`**: (Disable quest command)\n'
                            +'**`QUEST EPIC`**: (Disable epic quest command)\n'
                            +'**`TEST`**: (Disable test mode)\n'
                            +'**`TRAINING`**: (Disable training command)\n'
                            +'**`ULTRAINING`**: (Disable ultraining command)\n'
                            +'**`WORK`**: (Disable work commands)')

                    elif cmd_parameter[2].upper() == "HUNT" or cmd_parameter[2].upper() == "HT":
                        if len(cmd_parameter) > 3:
                            if cmd_parameter[3].upper() == "HARDMODE" or cmd_parameter[3].upper() == "HM":
                                if len(cmd_parameter) > 4:
                                    None
                                else:
                                    Config.hunt_hardmode_first  = False
                                    await msg_ch.send('Hunt hardmode is now disabled')
                        else:
                            Config.is_hunt_enabled  = False
                            await msg_ch.send('Hunt is now disabled')

                    elif cmd_parameter[2].upper() == "LOOTBOX" or cmd_parameter[2].upper() == "L":
                        if len(cmd_parameter) > 3:
                        
                            if cmd_parameter[3].upper() == "ALL" or cmd_parameter[3].upper() == "A":
                                Config.buy_commonlb = False
                                Config.buy_edgylb = False
                                Config.buy_epiclb = False
                                Config.buy_rarelb = False
                                Config.buy_uncommonlb = False
                                await msg_ch.send('All lootboxes buying is now disabled')

                            elif cmd_parameter[3].upper() == "COMMON" or cmd_parameter[2].upper() == "C":
                                Config.buy_commonlb = False
                                await msg_ch.send('Common lootbox buying disabled')
                            
                            elif cmd_parameter[3].upper() == "EDGY" or cmd_parameter[2].upper() == "ED":
                                Config.buy_edgylb = False
                                await msg_ch.send('Edgy lootbox buying disabled')

                            elif cmd_parameter[3].upper() == "EPIC" or cmd_parameter[2].upper() == "EP":
                                Config.buy_epiclb = False
                                await msg_ch.send('Edgy lootbox buying disabled')

                            elif cmd_parameter[3].upper() == "HELP" or cmd_parameter[3].upper() == "H":
                                await msg_ch.send(
                                    'DISABLE LOOTBOX COMMANDS:\n'
                                    +'**`COMMON`**: (Disable common lootbox buying)\n'
                                    +'**`EDGY`**: (Disable edgy lootbox buying)\n'
                                    +'**`EPIC`**: (Disable epic lootbox buying)\n'
                                    +'**`RARE`**: (Disable rare lootbox buying)\n'
                                    +'**`UNCOMMON`**: (Disable uncommon lootbox buying)')
                            
                            elif cmd_parameter[3].upper() == "RARE" or cmd_parameter[2].upper() == "R":
                                Config.buy_rarelb = False
                                await msg_ch.send('Edgy lootbox buying disabled')
                            
                            elif cmd_parameter[3].upper() == "UNCOMMON" or cmd_parameter[2].upper() == "UC":
                                Config.buy_uncommonlb = False
                                await msg_ch.send('Edgy lootbox buying disabled')   
                        
                        elif len(cmd_parameter) == 3:
                            Config.is_buy_lootbox_enabled = False
                            await msg_ch.send('Buying lootboxes is now disabled')     
                    
                    elif cmd_parameter[2].upper() == "QUEST" or cmd_parameter[2].upper() == "Q":
                        if len(cmd_parameter) > 3:
                            
                            if cmd_parameter[3].upper() == "EPIC" or cmd_parameter[3].upper() == "E":
                                Config.epic_quest_first = False
                                await msg_ch.send('Epic quest is now disabled')
                                
                        else:
                            Config.is_quest_enabled  = False
                            await msg_ch.send('Quest is now disabled')

                    elif cmd_parameter[2].upper() == "TEST" or cmd_parameter[2].upper() == "TT":
                        if len(cmd_parameter) > 3:
                            
                            if cmd_parameter[3].upper() == "MESSAGES" or cmd_parameter[3].upper() == "M":
                                Config.test_messages = False
                                await msg_ch.send('Test messages is now disabled')

                        else:
                            Config.test_mode  = False
                            await msg_ch.send('Test mode is now disabled')  

                    elif cmd_parameter[2].upper() == "TRAINING" or cmd_parameter[2].upper() == "T":
                        if len(cmd_parameter) > 3:
                            None
                        else:
                            Config.is_training_enabled = False
                            await msg_ch.send('Training is now disabled')  

                    elif cmd_parameter[2].upper() == "ULTRAINING" or cmd_parameter[2].upper() == "UT":
                        if len(cmd_parameter) > 3:
                            None
                        else:
                            Config.ultraining_first  = False
                            await msg_ch.send('Ultraining is now disabled') 

                    elif cmd_parameter[2].upper() == "WORK" or cmd_parameter[2].upper() == "W":
                        if len(cmd_parameter) > 3:
                            None
                        else:
                            Config.is_work_enabled  = False
                            await msg_ch.send('Work is now disabled')                                       

            elif cmd_parameter[1].upper() == "ENABLE" or cmd_parameter[1].upper() == "E":
                if len(cmd_parameter) > 2:
                    
                    if cmd_parameter[2].upper() == "ADVENTURE" or cmd_parameter[2].upper() == "AD":
                        if len(cmd_parameter) > 3:
                            None
                        else:
                            Config.is_adventure_enabled  = True
                            await msg_ch.send('Adventure is now enabled')

                    elif cmd_parameter[2].upper() == "ALL" or cmd_parameter[2].upper() == "A":
                        if len(cmd_parameter) > 3:
                            await msg_ch.send('Too much parameters.')

                        else:
                            Config.is_adventure_enabled  = True
                            Config.is_buy_lootbox_enabled = True
                            Config.is_farm_enabled = True
                            Config.is_hunt_enabled = True
                            Config.is_quest_enabled = True
                            Config.is_training_enabled = True
                            Config.is_work_enabled = True
                            Config.epic_quest_first = True
                            Config.ultraining_first = True
                            Config.hunt_hardmode_first = True
                            await msg_ch.send('Every command is now enabled')
                    
                    elif cmd_parameter[2].upper() == "CAPTCHA" or cmd_parameter[2].upper() == "C":
                        if len(cmd_parameter) > 3:
                            None
                        else:
                            Config.solve_epic_guard  = True
                            await msg_ch.send('Captcha solving is now enabled')
                    
                    elif cmd_parameter[2].upper() == "EVENTS" or cmd_parameter[2].upper() == "E":
                        if len(cmd_parameter) > 3:
                            None
                        else:
                            Config.solve_events  = True
                            await msg_ch.send('Event solver is now enabled')
                    
                    elif cmd_parameter[2].upper() == "FARM" or cmd_parameter[2].upper() == "F":
                        if len(cmd_parameter) > 3:
                            None
                        else:
                            Config.is_farm_enabled  = True
                            await msg_ch.send('Farm is now enabled')
                    
                    elif cmd_parameter[2].upper() == "HELP" or cmd_parameter[2].upper() == "H":
                        await msg_ch.send(
                            '**ENABLE COMMANDS:**\n'
                            +'**`ALL`**: (Enable all commands)\n'
                            +'**`ADVENTURE`**: (Enable adventure command)\n'
                            +'**`CAPTCHA`**: (Enable captcha solving)\n'
                            +'**`EVENTS`**: (Enable events solving)\n'
                            +'**`FARM`**: (Enable farm command)\n'
                            +'**`HUNT`**: (Enable hunt command)\n'
                            +'**`HUNT HARDMODE`**: (Enable hunt hardmode command)\n'
                            +'**`LOOTBOX`**: (Enable buy lootbox commands)\n'
                            +'**`QUEST`**: (Enable quest command)\n'
                            +'**`QUEST EPIC`**: (Enable epic quest command)\n'
                            +'**`TEST`**: (Enable test mode)\n'
                            +'**`TRAINING`**: (Enable training command)\n'
                            +'**`ULTRAINING`**: (Enable ultraining command)\n'
                            +'**`WORK`**: (Enable work commands)')

                    elif cmd_parameter[2].upper() == "HUNT" or cmd_parameter[2].upper() == "HT":
                        if len(cmd_parameter) > 3:

                            if cmd_parameter[3].upper() == "HARDMODE" or cmd_parameter[3].upper() == "HM":
                                if len(cmd_parameter) > 4:
                                    None
                                else:
                                    Config.hunt_hardmode_first  = True
                                    await msg_ch.send('Hunt hardmode is now enabled')
                        else:
                            Config.is_hunt_enabled  = True
                            await msg_ch.send('Hunt is now enabled')

                    elif cmd_parameter[2].upper() == "LOOTBOX" or cmd_parameter[2].upper() == "L":
                        if len(cmd_parameter) > 3:

                            if cmd_parameter[3].upper() == "ALL" or cmd_parameter[3].upper() == "A":
                                Config.buy_commonlb = True
                                Config.buy_edgylb = True
                                Config.buy_epiclb = True
                                Config.buy_rarelb = True
                                Config.buy_uncommonlb = True
                                await msg_ch.send('All lootboxes buying is enabled')

                            elif cmd_parameter[3].upper() == "COMMON" or cmd_parameter[3].upper() == "C":
                                Config.buy_commonlb = True
                                await msg_ch.send('Common lootbox buying enabled')
                            
                            elif cmd_parameter[3].upper() == "EDGY" or cmd_parameter[3].upper() == "ED":
                                Config.buy_edgylb = True
                                await msg_ch.send('Edgy lootbox buying enabled')

                            elif cmd_parameter[3].upper() == "EPIC" or cmd_parameter[3].upper() == "EP":
                                Config.buy_epiclb = True
                                await msg_ch.send('Edgy lootbox buying enabled')

                            elif cmd_parameter[3].upper() == "HELP" or cmd_parameter[3].upper() == "H":
                                await msg_ch.send(
                                    '**ENABLE LOOTBOX COMMANDS:**\n'
                                    +'**`COMMON`**: (Enable common lootbox buying)\n'
                                    +'**`EDGY`**: (Enable edgy lootbox buying)\n'
                                    +'**`EPIC`**: (Enable epic lootbox buying)\n'
                                    +'**`RARE`**: (Enable rare lootbox buying)\n'
                                    +'**`UNCOMMON`**: (Enable uncommon lootbox buying)')
                            
                            elif cmd_parameter[3].upper() == "RARE" or cmd_parameter[3].upper() == "R":
                                Config.buy_rarelb = True
                                await msg_ch.send('Edgy lootbox buying enabled')
                            
                            elif cmd_parameter[3].upper() == "UNCOMMON" or cmd_parameter[3].upper() == "UC":
                                Config.buy_uncommonlb = True
                                await msg_ch.send('Edgy lootbox buying enabled')
                        elif len(cmd_parameter) == 3:
                            Config.is_buy_lootbox_enabled = True
                            await msg_ch.send('Buying lootboxes is now enabled')

                    elif cmd_parameter[2].upper() == "QUEST" or cmd_parameter[2].upper() == "Q":
                        if len(cmd_parameter) > 3:
                            
                            if cmd_parameter[3].upper() == "EPIC" or cmd_parameter[3].upper() == "E":
                                Config.epic_quest_first = True
                                await msg_ch.send('Epic quest is now enabled')
                                
                        else:
                            Config.is_quest_enabled  = True
                            await msg_ch.send('Quest is now enabled')

                    elif cmd_parameter[2].upper() == "TEST" or cmd_parameter[2].upper() == "TT":
                        if len(cmd_parameter) > 3:
                            
                            if cmd_parameter[3].upper() == "MESSAGES" or cmd_parameter[3].upper() == "M":
                                Config.test_messages = True
                                await msg_ch.send('Test messages is now enabled')

                        else:
                            Config.test_mode  = True
                            await msg_ch.send('Test mode is now enabled')  

                    elif cmd_parameter[2].upper() == "TRAINING" or cmd_parameter[2].upper() == "T":
                        if len(cmd_parameter) > 3:
                            None
                        else:
                            Config.is_training_enabled  = True
                            await msg_ch.send('Training is now enabled')  

                    elif cmd_parameter[2].upper() == "ULTRAINING" or cmd_parameter[2].upper() == "UT":
                        if len(cmd_parameter) > 3:
                            None
                        else:
                            Config.ultraining_first  = True
                            await msg_ch.send('Ultraining is now enabled')  
                            
                    elif cmd_parameter[2].upper() == "WORK" or cmd_parameter[2].upper() == "W":
                        if len(cmd_parameter) > 3:
                            None
                        else:
                            Config.is_work_enabled  = True
                            await msg_ch.send('Work is now enabled') 

            elif cmd_parameter[1].upper() == "EVALUATE" or cmd_parameter[1].upper() == "EVAL" or cmd_parameter[1].upper() == "EV":
                try:
                    await msg_ch.send('Result to ` '+stringSublist(cmd_parameter, 2, len(cmd_parameter))+' ` is: **'+str(eval(stringSublist(cmd_parameter, 2, len(cmd_parameter))))+'**')
                except:
                    await msg_ch.send('Syntax error')
                finally:
                    None

            elif cmd_parameter[1].upper() == "HELP" or cmd_parameter[1].upper() == "H":
                await msg_ch.send('**EGO COMMANDS:**\n'
                    +'**`DISABLE`**: (Disable some features)\n'
                    +'**`ENABLE`**: (Enable some features)\n'
                    +'**`PAUSE`**: (Pause farming)\n'
                    +'**`SET`**: (Set new variable values)\n'
                    +'**`START`**: (Launch farming)\n'
                    +'**`SUMMARY`**: (List variable values)\n'
                    +'**`TEST`**: (Development testing features)')

            elif cmd_parameter[1].upper() == "SET" or cmd_parameter[1].upper() == "S":
                if len(cmd_parameter) > 2:

                    if cmd_parameter[2].upper() == "AREA" or cmd_parameter[2].upper() == "A":
                        if len(cmd_parameter) > 3:
                            
                            if str(cmd_parameter[3]).upper() == "MAXIMUM" or str(cmd_parameter[3]).upper() == "MAX":
                                Config.max_preferred = True
                                Config.preferred_area = Stats.max_area
                                await msg_ch.send('Preferred area set as Maximum ('+str(Stats.max_area)+')')

                            elif cmd_parameter[3].isdigit():
                                Config.max_preferred = False
                                if Stats.max_area >= int(cmd_parameter[3]):
                                    Config.preferred_area = int(cmd_parameter[3])
                                    await msg_ch.send('Preferred area set as '+str(Config.preferred_area))
                                else:
                                    Config.preferred_area = Stats.max_area
                                    await msg_ch.send('This is higher than your max area!\nPreferred area set as '+str(Config.preferred_area))

                            else:
                                await msg_ch.send('[4] Must be a numeric value')
                    
                    elif cmd_parameter[2].upper() == "FARM" or cmd_parameter[2].upper() == "F":
                        if len(cmd_parameter) > 3:
                            Config.farm_target =  stringSublist(cmd_parameter, 3, len(cmd_parameter))
                            await msg_ch.send('Farm target set as '+Config.farm_target)

                    elif cmd_parameter[2].upper() == "HEAL" or cmd_parameter[2].upper() == "HL":
                        if len(cmd_parameter) > 3:

                            if cmd_parameter[3].upper() == "ADVENTURE" or cmd_parameter[3].upper() == 'AD':
                                if len(cmd_parameter) > 4:
                                    
                                    if cmd_parameter[4].isdigit():
                                        Config.adventure_heal_trigger = int(cmd_parameter[4])
                                        await msg_ch.send('Adventure healing limit established at '+str(Config.adventure_heal_trigger))
                                    else:
                                        await msg_ch.send('Limit must be numeric')
                                
                                else:
                                    await msg_ch.send('You must write a limit')
                            
                            if cmd_parameter[3].upper() == "HUNT" or cmd_parameter[3].upper() == 'HT':
                                if len(cmd_parameter) > 4:
                                    
                                    if cmd_parameter[4].isdigit():
                                        Config.hunt_heal_trigger = int(cmd_parameter[4])
                                        await msg_ch.send('Hunt healing limit established at '+str(Config.hunt_heal_trigger))
                                    else:
                                        await msg_ch.send('Limit must be numeric')
                                
                                else:
                                    await msg_ch.send('You must write a limit')

                            elif cmd_parameter[3].upper() == "HELP" or cmd_parameter[3].upper() == "H":
                                await msg_ch.send(
                                    '**HEAL HELP**\n'
                                    +'The correct usage for this command is:\n`'
                                    +stringSublist(cmd_parameter, 0, len(cmd_parameter)-1)+' [target] [limit]`\n'
                                    +'[target] = (ADVENTURE / HUNT)\n'
                                    +'[limit] = (Numeric value)')
                        
                        else: 
                            await msg_ch.send('Parameters are missing')

                    elif cmd_parameter[2].upper() == "HELP" or cmd_parameter[2].upper() == "H":
                                await msg_ch.send(
                                    '**SET HELP**\n'
                                    +'**`HEAL`** = (Set limits to the healing triggers)\n'
                                    +'**`WORK`** = (Set work commands)')

                    elif cmd_parameter[2].upper() == "ULTRAINING" or cmd_parameter[2].upper() == "U":
                        if len(cmd_parameter) > 3:
                            Config.ultraining_choice =  stringSublist(cmd_parameter, 3, len(cmd_parameter))
                            await msg_ch.send('Ultraining choice set as '+Config.ultraining_choice)
                    
                    elif cmd_parameter[2].upper() == "WAVES" or cmd_parameter[2].upper() == "WV":
                        if len(cmd_parameter) > 3:
                            try:
                                Config.epic_quest_waves =  int(stringSublist(cmd_parameter, 3, len(cmd_parameter)))
                                await msg_ch.send('Epic quest waves set as '+str(Config.epic_quest_waves))
                            except: 
                                await msg_ch.send('Must be an integer!')

                    elif cmd_parameter[2].upper() == "WORK" or cmd_parameter[2].upper() == "W":
                        if len(cmd_parameter) > 3:

                            if cmd_parameter[3].upper() == "HELP" or cmd_parameter[3].upper() == 'H':
                                await msg_ch.send(
                                    '**WORK HELP:**\n'
                                    +'The correct usage for this command is:\n'
                                    +'**`'+stringSublist(cmd_parameter, 0, 3)+' [n] [work]`**\n'
                                    +'**`[n]`** = (number from 1 to 4)\n'
                                    +'**`[work]`** = (chop, fish, pickup, mine, etc...)\n')

                            elif cmd_parameter[3].upper() in ['1','2','3','4','A','ALL']:
                                if len(cmd_parameter) > 4:
                                    if len(cmd_parameter) > 5:
                                        await msg_ch.send(
                                            'Unexpected parameter **`'+cmd_parameter[5]+'`** in position [6]:\n'
                                            +'**`'+stringSublist(cmd_parameter, 0, 6)+'`**< unexpected')

                                    elif cmd_parameter[3] == " ":
                                        await msg_ch.send(
                                            'Expected missing parameter in position [4]\n'
                                            +'**`'+stringSublist(cmd_parameter, 0, 5)+'`**<? missing parameter')

                                    elif cmd_parameter[3].upper() == "ALL" or cmd_parameter[3].upper() == "A":
                                        Config.work1 = cmd_parameter[4]
                                        Config.work2 = cmd_parameter[4]
                                        Config.work3 = cmd_parameter[4]
                                        Config.work4 = cmd_parameter[4]
                                        await msg_ch.send('All work variables set as '+Config.work4)

                                    elif cmd_parameter[3] == "1":
                                        Config.work1 = cmd_parameter[4]
                                        await msg_ch.send('Work 1 variable set as '+Config.work1)

                                    elif cmd_parameter[3] == "2":
                                        Config.work2 = cmd_parameter[4]
                                        await msg_ch.send('Work 2 variable set as '+Config.work2)

                                    elif cmd_parameter[3] == "3":
                                        Config.work3 = cmd_parameter[4]
                                        await msg_ch.send('Work 3 variable set as '+Config.work3)

                                    elif cmd_parameter[3] == "4":
                                        Config.work4 = cmd_parameter[4]
                                        await msg_ch.send('Work 4 variable set as '+Config.work4)

                                    elif cmd_parameter[3].upper() == "HELP" or cmd_parameter[3].upper() == 'H':
                                        await msg_ch.send()
                                else:
                                    await msg_ch.send(
                                        'The correct usage for this command is:\n'
                                        +'**`'+stringSublist(cmd_parameter, 0, len(cmd_parameter))+' [work]`**\n'
                                        +'[work] = (chop, fish, pickup, mine, etc...)\n'
                                        +'[work] is missing in **`'+stringSublist(cmd_parameter, 0, len(cmd_parameter))+' _`**< !')
                            
                            else:
                                await msg_ch.send('Unknown parameter:')
                        else:
                            await msg_ch.send('The correct usage for this command is:\n**`'+stringSublist(cmd_parameter, 0, len(cmd_parameter))+' [n] [work]`**\n[n] = number from 1 to 4\n[work] = (chop, fish, pickup, mine, etc...)\n[n] is missing in **`'+stringSublist(cmd_parameter, 0, len(cmd_parameter))+' _`**< !')
                    
                    elif cmd_parameter[2].upper() == "HELP" or cmd_parameter[2].upper() == "H":
                         await msg_ch.send('**SET COMMANDS:**\n**`WORK`**: (Set work variables for work farming)')
                
                else:
                    await msg_ch.send(
                        'Expected parameter is missing!\n'
                        +'The correct usage for this command is:\n'
                        +'**`'+stringSublist(cmd_parameter, 0, len(cmd_parameter))+' [command]`**\n'
                        +'Type **`EGO SET HELP`** to see all **`SET`** commands.\n'
                        +'[command] is missing in **`'+stringSublist(cmd_parameter, 0, len(cmd_parameter))+' _`**< !')
            
            elif cmd_parameter[1].upper() == "PAUSE" or cmd_parameter[1].upper() == 'PS':
                Aux.is_paused = True
                await msg_ch.send("Paused.")
                
            elif cmd_parameter[1].upper() == "SHUTDOWN" or cmd_parameter[1].upper() == 'SD':
                Aux.is_paused = True
                await msg_ch.send("Shutting down...")
                await bot.change_presence(status=discord.Status.offline)
                await bot.close()

            elif cmd_parameter[1].upper() == "START" or cmd_parameter[1].upper() == 'ST':
                Aux.is_paused = False
                Config.player_name = msg_at.name
                Config.player_mention = msg_at.mention
                Config.player = msg_at
                await msg_ch.send("Farming...")
                sendMessage(Aux.epic_prefix+'profile')
                time.sleep(1)
                sendMessage(Aux.epic_prefix+'inventory')
                time.sleep(1)
                # sendMessage(Aux.epic_prefix+'hf megarace')
                # time.sleep(1)
                sendMessage(Aux.epic_prefix+'cooldown')
                time.sleep(1)
                if Config.max_preferred:
                        Config.preferred_area = Stats.max_area
                if threading.active_count() < 4:
                    farm_thread = threading.Thread(target=checkFarm, args=())
                    farm_thread.start()
                else:
                    print("No se inició porque estaba activo")

            elif cmd_parameter[1].upper() == "SUMMARY" or cmd_parameter[1].upper() == 'SM':

                if len(cmd_parameter) > 2:
                    if cmd_parameter[2].upper() == "COOLDOWN" or cmd_parameter[2].upper() == "CD":
                        await msg_ch.send(
                            "**Daily Reward:** ` "+hourFormatter(Cooldown.daily)+'`'
                            +"\n**Weekly Reward:** ` "+hourFormatter(Cooldown.weekly)+'`'
                            +"\n**Lootbox:** ` "+hourFormatter(Cooldown.lootbox)+'`'
                            +"\n**Vote:** ` "+hourFormatter(Cooldown.vote)+'`'
                            +"\n\n**Hunt:** ` "+hourFormatter(Cooldown.hunt)+'`'
                            +"\n**Adventure:** ` "+hourFormatter(Cooldown.adventure)+'`'
                            +"\n**Training:** ` "+hourFormatter(Cooldown.training)+'`'
                            +"\n**Duel:** ` "+hourFormatter(Cooldown.duel)+'`'
                            +"\n**Quest:** ` "+hourFormatter(Cooldown.quest)+'`'
                            +"\n\n**Work:** ` "+hourFormatter(Cooldown.work)+'`'
                            +"\n**Farm:** ` "+hourFormatter(Cooldown.farm)+'`'
                            +"\n**Horse breeding:** ` "+hourFormatter(Cooldown.horse)+'`'
                            +"\n**Arena:** ` "+hourFormatter(Cooldown.arena)+'`'
                            +"\n**Dungeon:** ` "+hourFormatter(Cooldown.dungeon)+'`'
                            +"\n\n**Megarace:** ` "+hourFormatter(Cooldown.megarace)+'`')

                    elif cmd_parameter[2].upper() == "INVENTORY" or cmd_parameter[2].upper() == "I":
                        await msg_ch.send(
                            "**Life potion:** ` "+str(Inv.life_potion)+' `'
                            +"\n**Ruby:** ` "+str(Inv.ruby)+' `'
                            +"\n**Basic seed:** ` "+str(Inv.basic_seeds)+' `'
                            +"\n**Carrot seed:** ` "+str(Inv.carrot_seeds)+' `'
                            +"\n**Bread seed:** ` "+str(Inv.bread_seeds)+' `'
                            +"\n**Potato seed:** ` "+str(Inv.potato_seeds)+' `')
                    
                    elif cmd_parameter[2].upper() == "STATS" or cmd_parameter[2].upper() == "S":
                        await msg_ch.send(
                            "**Actual area:** ` "+str(Stats.actual_area)+' ` **(Max:** ` '+str(Stats.max_area)+' `)'
                            +"\n**Life:** ` "+str(Stats.actual_hp)+'/'+str(Stats.max_hp)+' `'
                            +"\n**Coins:** ` "+str(Stats.coins)+' `'
                            +"\n**Bank:** ` "+str(Stats.bank)+' `'
                            +"\n**Horse boost:** ` "+Stats.horse_boost+" `")
                else:
                    tstmd = ''
                    if Config.max_preferred:
                        Config.preferred_area = Stats.max_area
                    if Config.test_mode:
                        tstmd = ' testing '
                    await msg_ch.send(
                        "**Preferred area:** ` "+str(Config.preferred_area)+' ` **Maximum:** ` '+str(Config.max_preferred)+' `'
                        +"\n\n**Adventure healing at:** ` "+str(Config.adventure_heal_trigger)+' `'
                        +"\n**Hunt healing at:** ` "+str(Config.hunt_heal_trigger)+' `'
                        +"\n\n**Work 1:** ` "+Config.work1+' `'
                        +"\n**Work 2:** ` "+Config.work2+' `'
                        +"\n**Work 3:** ` "+Config.work3+' `'
                        +"\n**Work 4:** ` "+Config.work4+' `'
                        +"\n**Next work:** ` Work "+str(Aux.switch_work+1)+' `'
                        +"\n**Ultraining choice:** ` "+Config.ultraining_choice+' `'
                        +"\n**Epic quest waves:** ` "+str(Config.epic_quest_waves)+' `'
                        +"\n**Farm:** ` "+Config.farm_target+' `'
                        +"\n\n**Hunt enabled:** ` "+str(Config.is_hunt_enabled)+' `'
                        +"\n**Adventure enabled:** ` "+str(Config.is_adventure_enabled)+' `'
                        +"\n**Training enabled:** ` "+str(Config.is_training_enabled)+' `'
                        +"\n**Work enabled:** ` "+str(Config.is_work_enabled)+' `'
                        +"\n**Farm enabled:** ` "+str(Config.is_farm_enabled)+' `'
                        +"\n**Lootbox buy enabled:** ` "+str(Config.is_buy_lootbox_enabled)+' `'
                        +"\n\n**Ultraining first:** ` "+str(Config.ultraining_first)+' `'
                        +"\n**Epic quest first:** ` "+str(Config.epic_quest_first)+' `'
                        +"\n**Hunt hardmode first:** ` "+str(Config.hunt_hardmode_first)+' `'
                        +"\n\n**Buy common lootbox:** ` "+str(Config.buy_commonlb)+' `'
                        +"\n**Buy edgy lootbox:** ` "+str(Config.buy_edgylb)+' `'
                        +"\n**Buy epic lootbox:** ` "+str(Config.buy_epiclb)+' `'
                        +"\n**Buy rare lootbox:** ` "+str(Config.buy_rarelb)+' `'
                        +"\n**Buy uncommon lootbox:** ` "+str(Config.buy_uncommonlb)+' `'
                        +"\n\n**Captcha solving:** ` "+str(Config.solve_epic_guard)+' `'
                        +"\n**Event solving:** ` "+str(Config.solve_events)+' `'
                        +"\n\n**Version:** ` "+Aux.version+tstmd+'`')
            
            elif cmd_parameter[1].upper() == "TEST" or cmd_parameter[1].upper() == "T" and Config.test_mode:
                if len(cmd_parameter) > 2:

                    if cmd_parameter[2].upper() == "FAKE" or cmd_parameter[2].upper() == "F":
                        sendMessage(stringSublist(cmd_parameter, 3, len(cmd_parameter)))

                    elif cmd_parameter[2].upper() == "HELP" or cmd_parameter[2].upper() == "H":
                        await msg_ch.send('**TEST COMMANDS:**\nQue le valga brg doña')

                    elif cmd_parameter[2].upper() == "SPLIT" or cmd_parameter[2].upper() == "SP":
                        await msg_ch.send('**EGO SPLIT:**\n'+stringSplit(stringSublist(cmd_parameter, 3, len(cmd_parameter))))

                    elif cmd_parameter[2].upper() == "SUBLIST" or cmd_parameter[2].upper() == "SL":
                        await msg_ch.send('**EGO SUBLIST:**\n'+stringSublist(cmd_parameter, 3, len(cmd_parameter)))
    
    if "EPIC GUARD" in msg_ct:

        if "Everything seems fine" in msg_ct or "I will let you go" in msg_ct:
            sendMessage("EGO START")

        elif "stop there" in msg_ct:
            
            Aux.is_paused = True

            if Config.solve_epic_guard:

                if message.attachments:

                    url1 = str(message.attachments[0].url)

                    url_rsp = requests.get(url=url1, stream=True)
                    img_array = np.array(bytearray(url_rsp.content), dtype=np.uint8)
                    img = cv.imdecode(img_array, 1)
                    color_coverted = cv.cvtColor(img, cv.COLOR_BGR2RGB)
                    pillowimg = Image.fromarray(color_coverted)

                    pixel = pillowimg.load()

                    indexes = {}
                    for x in range(pillowimg.size[0]):
                        for y in range(pillowimg.size[1]):
                            
                            if pixel[x, y] in Aux.banana_patron:
                                Aux.is_banana = True

                            if pixel[x, y] in Aux.apple_patron:
                                Aux.is_apple = True

                            if pixel[x, y] in Aux.zombie_eye_patron:
                                Aux.is_zombie_eye = True

                            if pixel[x, y] in Aux.normie_fish_patron:
                                Aux.is_normie_fish = True

                            if pixel[x, y] in Aux.life_potion_patron:
                                Aux.is_life_potion = True

                            if pixel[x, y] in Aux.wolf_skin_patron:
                                Aux.is_wolf_skin = True

                            if pixel[x, y] in Aux.ruby_patron:
                                Aux.is_ruby = True

                            if pixel[x, y] in Aux.unicorn_horn_patron:
                                Aux.is_unicorn_horn = True
                                
                            if pixel[x, y] in Aux.golden_fish_patron:
                                Aux.is_golden_fish = True
                                
                            if pixel[x, y] in Aux.coin_patron:
                                Aux.is_coin = True
                                
                            if pixel[x, y] in Aux.epic_coin_patron:
                                Aux.is_epic_coin = True
                                
                            if pixel[x, y] in Aux.epic_fish_patron:
                                Aux.is_epic_fish = True
                                
                            if pixel[x, y] in Aux.chip_patron:
                                Aux.is_chip = True
                                
                            if pixel[x, y] in Aux.dragon_scale_patron:
                                Aux.is_dragon_scale = True
                                
                            if pixel[x, y] in Aux.mermaid_hair_patron:
                                Aux.is_mermaid_hair = True

                            if pixel[x, y][0] == pixel[x, y][1] and pixel[x, y][0] == pixel[x, y][2]:
                                None
                            else: 
                                if pixel[x,y] in indexes:
                                    indexes[pixel[x,y]] += 1
                                else:
                                    indexes[pixel[x,y]] = 1
                    
                    if Aux.is_apple or Aux.is_banana or Aux.is_chip or Aux.is_coin or Aux.is_dragon_scale or Aux.is_epic_coin or Aux.is_epic_fish or Aux.is_golden_fish or Aux.is_life_potion or Aux.is_mermaid_hair or Aux.is_normie_fish or Aux.is_ruby or Aux.is_unicorn_horn or Aux.is_wolf_skin or Aux.is_zombie_eye:
                        if Aux.is_banana:
                            sendMessage('banana')
                        if Aux.is_apple:
                            sendMessage('apple')
                        if Aux.is_zombie_eye:
                            sendMessage('zombie eye')
                        if Aux.is_normie_fish:
                            sendMessage('normie fish')
                        if Aux.is_life_potion:
                            sendMessage('life potion')
                        if Aux.is_wolf_skin:
                            sendMessage('wolf skin')
                        if Aux.is_ruby:
                            sendMessage('ruby')
                        if Aux.is_unicorn_horn:
                            sendMessage('unicorn horn')
                        if Aux.is_golden_fish:
                            sendMessage('golden fish')
                        if Aux.is_coin:
                            sendMessage('coin')
                        if Aux.is_epic_coin:
                            sendMessage('epic coin')
                        if Aux.is_epic_fish:
                            sendMessage('epic fish')
                        if Aux.is_chip:
                            sendMessage('chip')
                        if Aux.is_dragon_scale:
                            sendMessage('dragon scale')
                        if Aux.is_mermaid_hair:
                            sendMessage('mermaid hair')
                    else:
                        await msg_ch.send("I cannot solve this. It's your turn. "+Config.player_mention)

                    Aux.is_apple = False
                    Aux.is_banana = False
                    Aux.is_chip = False
                    Aux.is_coin = False                     
                    Aux.is_dragon_scale = False                     
                    Aux.is_epic_coin = False                     
                    Aux.is_epic_fish = False                     
                    Aux.is_golden_fish = False
                    Aux.is_life_potion = False                     
                    Aux.is_mermaid_hair = False                     
                    Aux.is_normie_fish = False                     
                    Aux.is_ruby = False                     
                    Aux.is_unicorn_horn = False                     
                    Aux.is_wolf_skin = False                     
                    Aux.is_zombie_eye = False
                
                else:
                    sendMessage()

        elif "is now in the jail" in msg_ct and Config.solve_epic_guard:
            time.sleep(random.randint(1,6)+5)
            sendMessage("rpg jail")
            time.sleep(1)
            sendMessage("protest")

    if Aux.is_paused:
        None
    elif "EPIC RPG" in str(msg_at):
        if msg_eb:
            if Config.player_name in str(msg_eb[0].author.name) and "cooldowns" in str(msg_eb[0].author.name):
                for x in msg_eb[0].fields:
                    cdSetter(x.value)

            elif Config.player_name in str(msg_eb[0].author.name) and "profile" in str(msg_eb[0].author.name):
                for x in msg_eb[0].fields:
                    statsSetter(x.value)

            elif Config.player_name in str(msg_eb[0].author.name) and "inventory" in str(msg_eb[0].author.name):
                Inv.life_potion = 0
                Inv.basic_seeds = 0
                Inv.carrot_seeds = 0
                Inv.potato_seeds = 0
                Inv.bread_seeds = 0
                for x in msg_eb[0].fields:
                    invSetter(x.value)
            
            elif Config.player_name in str(msg_eb[0].author.name) and "bank" in str(msg_eb[0].author.name):
                None
            
            elif Config.player_name in str(msg_eb[0].author.name) and "daily" in str(msg_eb[0].author.name):
                None

            elif Config.player_name in str(msg_eb[0].author.name) and "weekly" in str(msg_eb[0].author.name):
                None

            if Config.test_messages:
                await msg_ch.send(
                    '`Author:\n'+str(msg_eb[0].author)
                    +'\n\nDescription:\n'+str(msg_eb[0].description)
                    +'\n\Provider:\n'+str(msg_eb[0].provider)
                    +'\n\nTitle:\n'+str(msg_eb[0].title)+'\n\nFields Name:`')
                for x in msg_eb[0].fields:
                    await msg_ch.send('`1: '+str(x.name)+'`')
                await msg_ch.send('`Fields value:`')
                for x in msg_eb[0].fields:
                    await msg_ch.send('`1: '+str(x.value)+'`')
                await msg_ch.send('\n`Footer:\n'+str(msg_eb[0].footer)+'`')
                await msg_ch.send("Embed. "+Config.player_mention)

            if msg_eb[0].footer:
                
                if "this is an event" in msg_eb[0].footer.text and Config.solve_events:
                    if "Type **CHOP**" in msg_eb[0].fields[0].value:
                        sendMessage("CHOP")
                    elif "Type **CATCH**" in msg_eb[0].fields[0].value:
                        sendMessage("CATCH")
                    elif "Type **FISH**" in msg_eb[0].fields[0].value:
                        sendMessage("FISH")
                    elif "Type **SUMMON**" in msg_eb[0].fields[0].value:
                        sendMessage("SUMMON")
                    elif "The first player who types" in msg_eb[0].fields[0].value:
                        _lines = msg_eb[0].fields[0].value.split("\n", 3)
                        phrase = ""
                        for x in _lines[1]:
                            if x != "*":
                                phrase = phrase+x
                        sendMessage(phrase)
                
                elif len(msg_eb[0].fields) > 0:
                    if 'SUDDENLY,' in msg_eb[0].fields[0].name and 'IS APPROACHING' in msg_eb[0].fields[0].name:
                        line = msg_eb[0].fields[0].value.split('\n', 3)
                        hunger = int(line[0][line[0].find('ness**')+8:len(line[0])])
                        if hunger <= 19:
                            sendMessage('feed pat pat pat pat')
                        elif hunger <= 19*2:
                            sendMessage('feed feed pat pat pat')
                        elif hunger <= 19*3:
                            sendMessage('feed feed feed pat pat')
                        elif hunger <= 19*4:
                            sendMessage('feed feed feed feed pat')
                        else:
                            sendMessage('feed feed feed feed feed')
                    
                    elif 'Status' in msg_eb[0].fields[0].name:
                        cdSetter(msg_eb[0].fields[0].value)
                        if Cooldown.megarace > time.time():
                            Aux.megarace_notify_switch = True

            if msg_eb[0].description:
                if "You were about to hunt a defenseless" in msg_eb[0].description and Config.solve_events:
                    time.sleep(1)
                    sendMessage("fight")
                    time.sleep(3)
                    if Stats.actual_area < Config.preferred_area:
                        sendMessage("rpg area "+str(Config.preferred_area))

                elif "You were about to open a nice lootbox, but suddenly..." in msg_eb[0].description and Config.solve_events:
                    time.sleep(1)
                    sendMessage('magic spell')

                elif "You wake up, and suddenly you have returned to the first area" in msg_eb[0].description and Config.solve_events:
                    time.sleep(1)
                    sendMessage('search')
                    time.sleep(3)
                    sendMessage('fight')
                
                elif "You were about to" in msg_eb[0].description and ", but suddenly..." in msg_eb[0].description and ('chop' in msg_eb[0].description or 'fish' in msg_eb[0].description or 'pickup' in msg_eb[0].description or 'mine' in msg_eb[0].description) and Config.solve_events:
                    time.sleep(1)
                    sendMessage("move")
                    time.sleep(3)
                    sendMessage('fight')
            
            if len(msg_eb[0].fields) > 0:
                if 'megarace boost' in msg_eb[0].fields[0].name and "you're still riding" in msg_eb[0].fields[0].name:
                    sendMessage('yes')
                elif 'passes through the boost!' in msg_eb[0].fields[0].name:
                    time_segs = totSeg(msg_eb[0].fields[0].value)-time.time()
                    Cooldown.megarace = Cooldown.megarace - time_segs
                

        else:
            if "coins have been deposited" in msg_ct:
                coins = msg_ct[2:msg_ct.find('coins')-3]
                Stats.coins -= int(removeCoinFormat(coins))
                Stats.bank += int(removeCoinFormat(coins))

            elif 'coins have been withdrawn' in msg_ct:
                coins = msg_ct[2:msg_ct.find('coins')-3]
                Stats.coins += int(removeCoinFormat(coins))
                Stats.bank -= int(removeCoinFormat(coins))

            elif "found and killed" in msg_ct:
                linea = msg_ct.split('\n', 5)
                Stats.life = linea[2][linea[2].find("HP is")+6:len(linea[2])]
                life = Stats.life.split("/", 2)
                Stats.life = int(life[0])/int(life[1])
                coins = msg_ct[msg_ct.find("Earned ")+7:msg_ct.find("coins and ")-1]
                Stats.coins += int(removeCoinFormat(coins))
                # if Aux.last_found == 'hunt':
                #     Aux.last_found = ''
                #     Cooldown.hunt = time.time()+60
                # elif Aux.last_found == 'adventure':
                #     Aux.last_found = ''
                #     Cooldown.adventure == time.time()+60*60

            elif "is mining" in msg_ct:
                if 'got' in msg_ct and 'coins' in msg_ct:
                    coins = msg_ct[msg_ct.find("got")+4:msg_ct.find("<:coin:")-1]
                    Stats.coins += int(removeCoinFormat(coins))
                else:
                    ruby = msg_ct[msg_ct.find("GOT")+4:msg_ct.find("<:ruby:")-1]
                    Inv.ruby += int(removeCoinFormat(ruby))

            elif "is training in" in msg_ct:
                if "the mine!" in msg_ct:
                    if int(removeCoinFormat(msg_ct[msg_ct.find("more than")+10:msg_ct.find("<:ruby:")-1])) < int(Inv.ruby):
                        sendMessage('yes')
                    else:
                        sendMessage('no')
                elif "the field!" in msg_ct:
                    if "**first**" in msg_ct:
                        if "Apple" in msg_ct:
                            sendMessage('a')
                        else:
                            sendMessage('b')
                    elif "**second**" in msg_ct:
                        if "Apple" in msg_ct:
                            sendMessage('p')
                        else:
                            sendMessage('a')
                    elif "**third**" in msg_ct:
                        if "Apple" in msg_ct:
                            sendMessage('p')
                        else:
                            sendMessage('n')
                    elif "**fourth**" in msg_ct:
                        if "Apple" in msg_ct:
                            sendMessage('l')
                        else:
                            sendMessage('a')
                    elif "**fifth**" in msg_ct:
                        if "Apple" in msg_ct:
                            sendMessage('e')
                        else:
                            sendMessage('n')
                    elif "**sixth**" in msg_ct:
                        if "Apple" in msg_ct:
                            sendMessage('?')
                        else:
                            sendMessage('a')
                elif "the forest!" in msg_ct:
                    if "How many <:woodenlog:" in msg_ct:
                        sendMessage(str(msg_ct.count("<:woodenlog:")-1))
                    elif "How many <:EPIClog:" in msg_ct:
                        sendMessage(str(msg_ct.count("<:EPIClog:")-1))
                    elif "How many <:SUPERlog:" in msg_ct:
                        sendMessage(str(msg_ct.count("<:SUPERlog:")-1))
                    elif "How many <:MEGAlog:" in msg_ct:
                        sendMessage(str(msg_ct.count("<:MEGAlog:")-1))
                    elif "How many <:HYPERlog:" in msg_ct:
                        sendMessage(str(msg_ct.count("<:HYPERlog:")-1))
                    elif "How many <:ULTRAlog:" in msg_ct:
                        sendMessage(str(msg_ct.count("<:ULTRAlog:")-1))
                    elif "How many <:ULTIMATElog:" in msg_ct:
                        sendMessage(str(msg_ct.count("<:ULTIMATElog:")-1))
                elif "the river!" in msg_ct:
                    if "<:normiefish:" in msg_ct:
                        sendMessage('1')
                    elif "<:goldenfish:" in msg_ct:
                        sendMessage('2')
                    elif "<:EPICfish:" in msg_ct:
                        sendMessage('3')
                elif "the... casino?" in msg_ct:
                    _coin = "COIN" in msg_ct and ":coin:" in msg_ct
                    _diamond = "DIAMOND" in msg_ct and ":gem:" in msg_ct
                    _gift = "GIFT" in msg_ct and ":gift:" in msg_ct
                    _flc = "FOUR LEAF CLOVER" in msg_ct and ":four_leaf_clover:" in msg_ct
                    _die = "DICE" in msg_ct and ":game_die:" in msg_ct
                    if  _coin or _diamond or _gift or _flc or _die:
                        sendMessage('yes')
                    else:
                        sendMessage('no')
                else:
                    print(msg_ct)
                
            elif 'successfully bought' in msg_ct:
                howmany = 0

                if msg_ct[0].isdigit():
                    howmany = int(msg_ct[0:msg_ct.find('<:')-1])
                if ':seed:' in msg_ct:
                    Inv.basic_seeds = Inv.basic_seeds + howmany

            elif 'plants' in msg_ct:
                howmany = 0
                idline = 0
                idline2 = 0
                line = msg_ct.split('\n', 10)
                for x in range(0, len(line)):
                    if 'plants' in line[x]:
                        idline = x
                if ':seed:' in line[idline] and 'plants' in line[idline]:
                    Inv.basic_seeds = Inv.basic_seeds - 1
                elif ':carrotseed:' in line[idline] and 'plants' in line[idline]:
                    Inv.carrot_seeds = Inv.carrot_seeds - 1
                elif ':potatoseed:' in line[idline] and 'plants' in line[idline]:
                    Inv.potato_seeds = Inv.potato_seeds - 1
                elif ':breadseed:' in line[idline] and 'plants' in line[idline]:
                    Inv.bread_seeds = Inv.bread_seeds - 1
                for x in range(0, len(line)):
                    if 'also got' in line[x]:
                        idline2 = x
                if 'also got' in line[idline]:
                    howmany = int(removeCoinFormat(line[idline2][line[idline2].find('got')+4:line[idline2].find('<:')-1]))
                    if ':seed:' in line[idline2]:
                        Inv.basic_seeds = Inv.basic_seeds + howmany
                    elif ':carrotseed:' in line[idline2]:
                        Inv.carrot_seeds = Inv.carrot_seeds + howmany
                    elif ':potatoseed:' in line[idline2]:
                        Inv.potato_seeds = Inv.potato_seeds + howmany
                    elif ':breadseed:' in line[idline2]:
                        Inv.bread_seeds = Inv.bread_seeds + howmany

    else:
        None

    if not Aux.is_paused and Cooldown.megarace <= time.time() and Aux.megarace_notify_switch:
        Aux.megarace_notify_switch = False
        await Config.player.send('Megarace has concluded! You can start another one now!.')

def cdSetter(value):
    _lines = value.split("\n", 20)
    for x in _lines:
        if "daily" in x:
            Cooldown.daily = totSeg(x)
        elif "weekly" in x:
            Cooldown.weekly = totSeg(x)
        elif "lootbox" in x:
            Cooldown.lootbox = totSeg(x)
        elif "vote" in x:
            Cooldown.vote = totSeg(x)
        elif "hunt" in x:
            Cooldown.hunt = totSeg(x)
        elif "adventure" in x:
            Cooldown.adventure = totSeg(x)
        elif "training" in x:
            Cooldown.training = totSeg(x)
        elif "duel" in x:
            Cooldown.duel = totSeg(x)
        elif "quest" in x:
            Cooldown.quest = totSeg(x)
        elif "chop" in x:
            Cooldown.work = totSeg(x)
        elif "farm" in x:
            Cooldown.farm = totSeg(x)
        elif "horse breeding" in x:
            Cooldown.horse = totSeg(x)
        elif "arena" in x:
            Cooldown.arena = totSeg(x)
        elif "dungeon" in x:
            Cooldown.dungeon = totSeg(x)
        elif "Time remaining" in x:
            Cooldown.megarace = totSeg(x)

def statsSetter(value):
    _lines = value.split("\n", 3)
    for x in _lines:
        if "Level" in x:
            None
        elif "XP" in x:
            None
        elif "Area" in x:
            actual_area = x[x.find('Area')+8:x.find('(')-1]
            Stats.actual_area = int(removeCoinFormat(actual_area))
            max_area = x[x.find('Max')+5:x.find(')')]
            Stats.max_area = int(removeCoinFormat(max_area))
            if Config.max_preferred:
                Config.preferred_area = Stats.max_area
        elif "AT" in x:
            None
        elif "DEF" in x:
            None
        elif "LIFE" in x:
            Stats.life = x[x.find("LIFE")+8:len(x)]
            life = Stats.life.split("/", 2)
            Stats.life = int(life[0])/int(life[1])
            Stats.actual_hp = int(life[0])
            Stats.max_hp = int(life[1])
        elif "sword:" in x:
            None
        elif "armor:" in x:
            None
        elif ":tier" in x and "mount:" in x:
            Stats.horse_boost = x[x.find(">")+2:len(x)]
        elif "Coins" in x:
            coins = x[x.find("Coins")+9:len(x)]
            Stats.coins = int(removeCoinFormat(coins))
        elif "EPIC coins" in x:
            None
        elif "Bank" in x:
            bank = x[x.find("Bank")+8:len(x)]
            Stats.bank = int(removeCoinFormat(bank))

def invSetter(value):
    _lines = value.split("\n", 30)
    for x in _lines:
        if "**ruby**:" in x:
            Inv.ruby = int(removeCoinFormat(x[x.find("ruby**")+8:len(x)]))
        elif 'life potion' in x:
            Inv.life_potion = int(removeCoinFormat(x[x.find("tion**")+8:len(x)]))
        elif "**seed**:" in x:
            Inv.basic_seeds = int(removeCoinFormat(x[x.find("seed**")+8:len(x)]))
        elif "**potato seed**" in x:
            Inv.potato_seeds = int(removeCoinFormat(x[x.find("seed**")+8:len(x)]))
        elif "**carrot seed**" in x:
            Inv.carrot_seeds = int(removeCoinFormat(x[x.find("seed**")+8:len(x)]))
        elif "**bread seed**" in x:
            Inv.bread_seeds = int(removeCoinFormat(x[x.find("seed**")+8:len(x)]))

def totSeg (string):
    _total_secs = 0
    for x in range(0, len(string)):
        if "white_check_mark" in string:
            return time.time()
        elif "no_entry_sign" in string:
            return False
        elif x > 2:
            if string[x] == "d":
                if string[x-2].isdigit():
                    _total_secs = _total_secs+int(string[x-2:x])*24*60*60
                elif string[x-1].isdigit():
                    _total_secs = _total_secs+int(string[x-1])*24*60*60
            if string[x] == "h":
                if string[x-2].isdigit():
                    _total_secs = _total_secs+int(string[x-2:x])*60*60
                elif string[x-1].isdigit():
                    _total_secs = _total_secs+int(string[x-1])*60*60
            if string[x] == "m":
                if string[x-2].isdigit():
                    _total_secs = _total_secs+int(string[x-2:x])*60
                elif string[x-1].isdigit():
                    _total_secs = _total_secs+int(string[x-1])*60
            if string[x] == "s":
                if string[x-2].isdigit():
                    _total_secs = _total_secs+int(string[x-2:x])
                elif string[x-1].isdigit():
                    _total_secs = _total_secs+int(string[x-1])
    return time.time() + _total_secs

def hourFormatter(value):
    _result = ""
    value = int(value-time.time())
    _days = math.trunc(value/60/60/24)
    _hours = math.trunc((value/60/60)-(_days*24))
    _min = math.trunc((value/60)-(_hours*60)-(_days*60*24))
    _seconds = math.trunc((value)-(_min*60)-(_hours*60*60)-(_days*60*60*24))
    if _seconds < 0:
        _seconds = 0
    if _min < 0:
        _min = 0
    if _hours < 0:
        _hours = 0
    if _days < 0:
        _days = 0
    if _days == 0 and _hours == 0 and _min == 0 and _seconds == 0:
        _result = 'Available '
    else:
        if _days > 0:
            _result = _result+str(_days)+'d '
        if _hours > 0:
            _result = _result+str(_hours)+'h '
        if _min > 0:
            _result = _result+str(_min)+'m '
        if _seconds > 0:
            _result = _result+str(_seconds)+'s '
    return _result

def heal(cant):
    if Stats.life <= cant:
        time.sleep(random.randint(Aux.min_sec,Aux.max_sec))
        if not Aux.is_paused and Inv.life_potion < 1 and Stats.coins >= 2500:
            sendMessage(Aux.epic_prefix+'buy life potion 1')
            time.sleep(1)
        if not Aux.is_paused and Inv.life_potion > 0:
            sendMessage(Aux.epic_prefix+'heal')
            Stats.actual_hp = Stats.max_hp
            Stats.life = 1

def checkFarm():

    while (not Aux.is_paused):
        if Stats.max_hp != 0:

            if not Aux.is_paused and Config.is_hunt_enabled and Cooldown.hunt <= time.time():
                heal(Config.hunt_heal_trigger/Stats.max_hp)
                time.sleep(random.randint(Aux.min_sec,Aux.max_sec))
                if Aux.is_paused:
                    break
                if Stats.life > Config.hunt_heal_trigger/Stats.max_hp:
                    Aux.last_found = 'hunt'
                    if Stats.max_area >= 13 and Config.hunt_hardmode_first:
                        sendMessage(Aux.epic_prefix+'hunt hardmode')
                    else:
                        sendMessage(Aux.epic_prefix+'hunt')
                    Cooldown.hunt = time.time() + 60
                time.sleep(random.randint(Aux.min_sec,Aux.max_sec))
                if Aux.is_paused:
                    break
                sendMessage(Aux.epic_prefix+'inventory')

            if not Aux.is_paused and Config.is_adventure_enabled and Cooldown.adventure <= time.time():
                heal(Config.adventure_heal_trigger/Stats.max_hp)
                time.sleep(random.randint(Aux.min_sec,Aux.max_sec))
                if Aux.is_paused:
                    break
                if Stats.life > Config.adventure_heal_trigger/Stats.max_hp:
                    Aux.last_found = 'adventure'
                    sendMessage(Aux.epic_prefix+'adventure')
                    Cooldown.adventure = time.time() + 60*60
                time.sleep(random.randint(Aux.min_sec,Aux.max_sec))
                if Aux.is_paused:
                    break
                sendMessage(Aux.epic_prefix+'profile')
                time.sleep(random.randint(Aux.min_sec,Aux.max_sec))
                if Aux.is_paused:
                    break
                sendMessage(Aux.epic_prefix+'inventory')

            if not Aux.is_paused and Config.is_work_enabled and Cooldown.work <= time.time():
                time.sleep(random.randint(Aux.min_sec,Aux.max_sec))
                if Aux.is_paused:
                    break
                if Aux.switch_work == 0:
                    Aux.last_work = Config.work1
                    Aux.switch_work = 1
                elif Aux.switch_work == 1:
                    Aux.last_work = Config.work2
                    Aux.switch_work = 2
                elif Aux.switch_work == 2:
                    Aux.last_work = Config.work3
                    Aux.switch_work = 3
                elif Aux.switch_work == 3:
                    Aux.last_work = Config.work4
                    Aux.switch_work = 0
                if Aux.last_work.lower() in 'chop axe bowsaw chainsaw':
                    if Stats.max_area >= 9:
                        Aux.last_work = 'chainsaw'
                    elif Stats.max_area >= 6:
                        Aux.last_work = 'bowsaw'
                    elif Stats.max_area >= 3:
                        Aux.last_work = 'axe'
                    else:
                        Aux.last_work = 'chop'
                elif Aux.last_work.lower() in 'fish net boat bigboat':
                    if Stats.max_area >= 9:
                        Aux.last_work = 'bigboat'
                    elif Stats.max_area >= 6:
                        Aux.last_work = 'boat'
                    elif Stats.max_area >= 3:
                        Aux.last_work = 'net'
                    else:
                        Aux.last_work = 'fish'
                elif Aux.last_work.lower() in 'pickup ladder tractor greenhouse':
                    if Stats.max_area >= 11:
                        Aux.last_work = 'greenhouse'
                    elif Stats.max_area >= 8:
                        Aux.last_work = 'tractor'
                    elif Stats.max_area >= 4:
                        Aux.last_work = 'ladder'
                    elif Stats.max_area >= 3:
                        Aux.last_work = 'pickup'
                    else:
                        Aux.last_work = 'chop'
                elif Aux.last_work.lower() in 'mine pickaxe drill dynamite':
                    if Stats.max_area >= 12:
                        Aux.last_work = 'dynamite'
                    elif Stats.max_area >= 10:
                        Aux.last_work = 'drill'
                    elif Stats.max_area >= 6:
                        Aux.last_work = 'pickaxe'
                    elif Stats.max_area >= 5:
                        Aux.last_work = 'mine'
                    else:
                        Aux.last_work = 'chop'
                sendMessage(Aux.epic_prefix+Aux.last_work)
                Cooldown.work = time.time() + 60*5
                if not Aux.is_paused and Aux.last_work in 'mine pickaxe drill dynamite':
                    time.sleep(random.randint(Aux.min_sec,Aux.max_sec))
                    if Aux.is_paused:
                        break
                    sendMessage(Aux.epic_prefix+'profile')
                if Aux.is_paused:
                    break
                time.sleep(random.randint(Aux.min_sec,Aux.max_sec))
                if Aux.is_paused:
                    break
                sendMessage(Aux.epic_prefix+'inventory')

            if not Aux.is_paused and Config.is_farm_enabled and Stats.max_area >= 4 and Cooldown.farm <= time.time():
                farm = 'basic seed'
                time.sleep(random.randint(Aux.min_sec,Aux.max_sec))
                if Aux.is_paused:
                    break
                sendMessage(Aux.epic_prefix+'profile')
                time.sleep(random.randint(Aux.min_sec,Aux.max_sec))
                if Aux.is_paused:
                    break
                sendMessage(Aux.epic_prefix+'inventory')
                if "carrot" in Config.farm_target and Inv.carrot_seeds > 0:
                    farm = Config.farm_target
                if "potato" in Config.farm_target and Inv.potato_seeds > 0:
                    farm = Config.farm_target
                if "bread" in Config.farm_target and Inv.bread_seeds > 0:
                    farm = Config.farm_target
                if farm.lower() == "basic seed" and Inv.basic_seeds < 1:
                    time.sleep(random.randint(Aux.min_sec,Aux.max_sec))
                    if Aux.is_paused:
                        break
                    sendMessage(Aux.epic_prefix+'buy seed 1')
                time.sleep(random.randint(Aux.min_sec,Aux.max_sec))
                if Aux.is_paused:
                    break
                sendMessage(Aux.epic_prefix+'farm '+farm)
                Cooldown.farm = time.time() + 60*10
                time.sleep(random.randint(Aux.min_sec,Aux.max_sec))
                if Aux.is_paused:
                    break
                sendMessage(Aux.epic_prefix+'inventory')

            if not Aux.is_paused and Config.is_training_enabled and Stats.max_area >= 2 and Cooldown.training <= time.time():
                time.sleep(random.randint(Aux.min_sec,Aux.max_sec))
                if Aux.is_paused:
                    break
                sendMessage(Aux.epic_prefix+'inventory')
                time.sleep(random.randint(Aux.min_sec,Aux.max_sec))
                if Aux.is_paused:
                    break
                if Stats.max_area >= 12 and Config.ultraining_first:
                    sendMessage(Aux.epic_prefix+'ultraining')
                    time.sleep(1)
                    sendMessage(Config.ultraining_choice)
                else:
                    sendMessage(Aux.epic_prefix+'training')
                Cooldown.training = time.time() + 60*15
            
            if not Aux.is_paused and Config.is_quest_enabled and Cooldown.quest <= time.time():
                time.sleep(random.randint(Aux.min_sec,Aux.max_sec))
                if Aux.is_paused:
                    break
                if Stats.horse_boost == '[SPECIAL]' and Config.epic_quest_first:
                    sendMessage(Aux.epic_prefix+'epic quest')
                    time.sleep(1)
                    sendMessage(str(Config.epic_quest_waves))
                else:
                    None
                Cooldown.quest = time.time() + 60*60*6

            if not Aux.is_paused and Config.is_buy_lootbox_enabled and Cooldown.lootbox <= time.time():
                time.sleep(random.randint(Aux.min_sec,Aux.max_sec))
                if Aux.is_paused:
                    break
                sendMessage(Aux.epic_prefix+'profile')
                time.sleep(random.randint(Aux.min_sec,Aux.max_sec))
                if Aux.is_paused:
                    break
                if int(Stats.coins) >= 420666 and Config.buy_edgylb:
                    sendMessage(Aux.epic_prefix+'buy edgy lootbox')
                elif int(Stats.coins) >= 150000 and Config.buy_epiclb:
                    sendMessage(Aux.epic_prefix+'buy epic lootbox')
                elif int(Stats.coins) >= 40000 and Config.buy_rarelb:
                    sendMessage(Aux.epic_prefix+'buy rare lootbox')
                elif int(Stats.coins) >= 6000 and Config.buy_uncommonlb:
                    sendMessage(Aux.epic_prefix+'buy uncommon lootbox')
                elif int(Stats.coins) >= 800 and Config.buy_commonlb:
                    sendMessage(Aux.epic_prefix+'buy common lootbox')
                else: None
                Cooldown.lootbox = time.time() + 60*60*3

            if not Aux.is_paused and Cooldown.daily <= time.time():
                time.sleep(random.randint(Aux.min_sec,Aux.max_sec))
                if Aux.is_paused:
                    break
                sendMessage(Aux.epic_prefix+'daily')
                Cooldown.daily = time.time() + 60*60*24

            if not Aux.is_paused and Cooldown.weekly <= time.time():
                time.sleep(random.randint(Aux.min_sec,Aux.max_sec))
                if Aux.is_paused:
                    break
                sendMessage(Aux.epic_prefix+'weekly')
                Cooldown.weekly = time.time() + 60*60*24*7

            if not Aux.is_paused and Aux.check <= time.time():
                time.sleep(random.randint(Aux.min_sec,Aux.max_sec))
                if Aux.is_paused:
                    break
                sendMessage(Aux.epic_prefix+'cooldown')
                Aux.check = time.time() + 30

        time.sleep(1)

def removeCoinFormat(value):
    _aux = value.split(',', 100)
    _coins = ''
    for x in range(len(_aux)):
        _coins += str(_aux[x])
    return str(_coins)

def stringSplit(list):
    result = ""
    for x in range(len(list)):
        if x == 0:
            result =  result+str(x)+" "+list[x]
        else:
            result =  result+"\n"+str(x)+" "+list[x]
    return result

def stringSublist(list, start, end):
    sublist = list[start:end]
    result = ""
    for x in range(len(sublist)):
        if x == 0:
            result = result+sublist[x]
        else:
            result = result+" "+sublist[x]
    return result

def timer(segundos, target):
    time.sleep(segundos)
    if not Aux.is_paused:
        exec(target)

def sendMessage(msg):
    requestURL = 'https://discord.com/api/v9/channels/'+Config.channel+'/messages'
    header = {
        'authorization': Config.player_token
    }
    payload = {
        'content': msg
    }
    requests.post(requestURL, data = payload, headers = header)

def sendCommand(command):
    command = 'x'
    requestURL = 'https://discord.com/api/v9/channels/'+Config.channel+'/messages'
    header = {
        'authorization': Config.player_token
    }
    payload = {
        'events' : [{
            'type' : "application_command_selected",
            'properties': {
                'command_id': command
            }
        }]
    }
    requests.post(requestURL, data = payload, headers = header)

bot.run(Config.bot_token)
