# Project Overview

## Introduction

This project demonstrates the use of the 0.96" OLED display (SSD1306) embedded on the RoboCore BlackBoard Wisdom. The goal is to show how to initialize the display and update it in real-time using MicroPython.

## Purpose

The main objective is to build a simple counter that updates on the OLED screen every second. This example provides a foundation for more advanced applications involving I2C communication, graphic rendering, or dynamic data display on the screen.

## Architecture

The system is built using MicroPython and runs directly on the BlackBoard Wisdom microcontroller. It makes use of the following components:

- **Microcontroller**: RoboCore BlackBoard Wisdom  
- **Display**: 0.96" OLED SSD1306 (I2C interface)  
- **I2C Pins**: SDA = GPIO21, SCL = GPIO22  
- **Libraries**: `ssd1306`, `gfx`, `machine`, `time`, `sleep`

## File Structure

- `src/main.py`: Main script that initializes the display and runs the counter loop  
- `src/button_rgb_led.py`: Contains code to control RGB LED colors using PWM  
- `docs/overview.md`: This document, describing the project overview and architecture

## Future Improvements

- Add button support to control the counter
- Integrate temperature or sensor data for dynamic display
- Display graphics and custom animations
- Modularize code for easier reuse in other Wisdom-based projects

