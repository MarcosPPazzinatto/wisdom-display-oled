# Wisdom Display OLED

This project demonstrates how to use the 0.96" OLED display (SSD1306) on the RoboCore BlackBoard Wisdom to show a simple counter using MicroPython.

## Features

- Displays a numeric counter on the OLED screen
- Uses SSD1306 over I2C interface
- Written in MicroPython
- Compatible with RoboCore BlackBoard Wisdom

## Hardware

- RoboCore BlackBoard Wisdom
- OLED Display 0.96" (128x64, I2C, SSD1306)

## Software Requirements

- MicroPython firmware installed on the board
- Required libraries:
  - `ssd1306`
  - `gfx`
  - `machine`
  - `time`

## How it works

The script initializes the OLED display via the I2C interface and uses a simple infinite loop to update a counter on the screen every second. The display is cleared and redrawn with each update.

## Getting Started

1. Upload the script to the BlackBoard Wisdom.
2. Ensure the OLED display is connected via I2C (default pins: SDA = GPIO21, SCL = GPIO22).
3. Run the script to see the counter in action.
