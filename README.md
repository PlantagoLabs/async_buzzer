# AsyncBuzzer

This module allows to use SparkFun's Qwiic Buzzer (BOB-24474) with micropython in a non-blocking manner. Features of this library include:
- Play a list of notes on the buzzer using micropython's asyncio. This is done in a single non blocking function call.
- A text to Morse code notes translator.
- A tab string to notes translator.
- A text to tune translator. Make your robot talk by playing music !

Everything is in async_buzzer.py, so adding it in your /lib folder should be enough. See examples for more information.

This library requires the use of asyncio to work. Tested on a RP2040 and a ESP32-C3.
