from machine import I2C
import time
import async_buzzer
from async_buzzer import Pitches
import uasyncio

async def main():
    i2c = I2C(0, scl=9, sda=8, freq=400000)

    buzzer = async_buzzer.AsyncI2CBuzzer(i2c, 52)

    # Play some notes
    buzzer.add([(Pitches.C4, 1, 1000), (Pitches.D2, 2, 1000), (Pitches.F3, 3, 1000), (Pitches.G5, 4, 1000)])
    # Wait for first 3 notes to be played 
    await uasyncio.sleep_ms(2400)
    # Stop playing notes and replace it with silence
    buzzer.replace(async_buzzer.tabs_to_notes('S_', 4, 150)) 
    # Say Hello World in Morse code
    buzzer.add(async_buzzer.text_to_morse_notes('Hello World', (Pitches.E5, 4, 50)))
    buzzer.add(async_buzzer.tabs_to_notes('S_', 4, 150)) # Stay silent a moment
    # Play Memory from Toby Fox's Undertale using tabs
    buzzer.add(async_buzzer.tabs_to_notes("S_ G4 D5 C5 G4 B4- B4 C5- G4 C5 G4 B4- B4 C5- G4 D5 C5 G4 B4- B4 C5- G4 C5 E5 D5- C5 D5-", 3, 400))
    buzzer.add(async_buzzer.tabs_to_notes('S_', 4, 150)) # Stay silent a moment
    # Say Hello World in Tunetalk
    buzzer.add(async_buzzer.tabs_to_notes(async_buzzer.text_to_tunetalk_tabs('Hello World'), 3, 180))
    buzzer.add(async_buzzer.tabs_to_notes('S_', 4, 150)) # Stay silent a moment
    # Make a siren sound
    buzzer.add(async_buzzer.siren())


    # Wait for everything to be played 
    await uasyncio.sleep_ms(100000)

    
uasyncio.run(main())


