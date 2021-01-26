"""Emoji
Available Commands:
.TCL
Credits to @telugucartoonlover
"""

from telethon import events

import asyncio

from userbot.utils import admin_cmd


@borg.on(admin_cmd("RD"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 1.5
    animation_ttl = range(0,36)
    #input_str = event.pattern_match.group(1)
   # if input_str == "RD":
    await event.edit("♥H♥a♥p♥p♥y♥ ♥R♥e♥p♥u♥b♥l♥i♥c ♥D♥a♥y")
    animation_chars = [
                   "Jana            = People"
            "Gana            = Group"
            "Mana           = Mind"
            "Adhinayaka= Leader"
            "Jaya He      = Victory "
            "Bharata       = India"
            "Bhagya       = Destiny"
            "Vidhata      = Disposer"
            "Punjaba     = Punjab"
            "Sindhu       = Indus"
            "Gujarata    = Gujarat"
            "Maratha    = Marati             Maharashtra"
            "Dravida      = South"
            "Utkala        = Orissa"
            "Banga        = Bengal"
            "Vindhya     =Vindhyas"
            "Himachal   =Himalay"
            "Yamuna     = Yamuna"
            "Ganga        = Ganges"
            "Uchchhala = Moving"
            "Jaladhi      = Ocean"
            "Taranga    = Waves"
            "Tava          = Your"
            "Shubh    =Auspicious"
            "Naame = name"
            "Jage     = Awaken"
            "Tava     = Your"
            "Shubha      =             Auspicious"
            "Aashisha = Blessings"
            "Maage     = Ask"
            "Gaahe      = Sing"
            "Tava        = Your"
            "Jaya        = Victory"
            "Gatha      = Song"
            "Jana       = People"
            "Gana      = Group"
            "Mangala = Fortune"
            "Dayaka   = Giver"
            "Jay He    = Victory Be"
            "Bharata  = India"
            "Bhagya  = Destiny"
            "Vidhata = Dispenser"
            "Jay He, Jay He, Jay He, Jay Jay Jay Jay He = Victory, Victory, Victory, Victory Forever..."
            "🇮🇳🌅: Congratulation to all of us.Our national anthem Jana Gana Mana... is declared as the BEST ANTHEM OF THE WORLD by UNESCO. Just few minutes ago.

Kindly share this. 
Very proud to be an INDIAN.
🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳👏👏👏👏👏👏👏😊😊😊😊😊😊😊🇮🇳🇮🇳🇮🇳🇮🇳🚩🌹🌹🌹
💦 Meaning of our National Anthem 💦💦
💎💎💎💎💎💎💎💎
🇮🇳 Please try to understand the meaning and pronounce it clearly.

Word by word meaning..

💦Jana            = People
💦Gana            = Group
💦Mana           = Mind
💦Adhinayaka= Leader
💦Jaya He      = Victory 
💦Bharata       = India
💦Bhagya       = Destiny
💦Vidhata      = Disposer
💦Punjaba     = Punjab
💦Sindhu       = Indus
💦Gujarata    = Gujarat
💦Maratha    = Marati 💦Maharashtra
💦Dravida      = South
💦Utkala        = Orissa
💦Banga        = Bengal
💦Vindhya     =Vindhyas
💦Himachal   =Himalay
💦Yamuna     = Yamuna
💦Ganga        = Ganges
💦Uchchhala = Moving
💦Jaladhi      = Ocean
💦Taranga    = Waves
💦Tava          = Your
💦Shubh    =Auspicious
💦Naame = name
💦Jage     = Awaken
💦Tava     = Your
💦Shubha      = 💦Auspicious
💦Aashisha = Blessings
💦Maage     = Ask
💦Gaahe      = Sing
💦Tava        = Your
💦Jaya        = Victory
💦Gatha      = Song
💦Jana       = People
💦Gana      = Group
💦Mangala = Fortune
💦Dayaka   = Giver
💦Jay He    = Victory Be
💦Bharata  = India
💦Bhagya  = Destiny
💦Vidhata = Dispenser
💦Jay He, Jay He, Jay 💦He, Jay Jay Jay Jay 💦He = Victory, Victory, Victory, Victory Forever...

this plugin credits goes to :- @telugucartoonlover

JAI HIND💦💦💦💦💦HAPPY REPUBLIC-DAY ★★★★☆☆☆★★★★♣♣♣♧♧♣♣♣"
            
         ]
    for i in animation_ttl:
        	
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 18])
