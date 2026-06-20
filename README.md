# weather_canada-for-HomeAssistant
HomeAssistant-Weather-Canada A lightweight, autonomous, and resilient solution to integrate Environment Canada weather data into Home Assistant via MQTT.
Why this project?
With the recent instability of native Environment Canada integrations in Home Assistant, this project provides a robust alternative. It uses the env_canada Python library to ensure continuous compatibility with official data feeds, independent of major Home Assistant core updates.

# Architecture
Flow: ECCC Servers → Python Script → MQTT Broker → Home Assistant

# Key Features
Resilient: Runs as a systemd service for automatic restarts.

Independent: Continues data collection even if Home Assistant is offline.

Lightweight: Minimal resource usage (~70 MB RAM).

# Installation
For Advanced Users (Core / Docker / VM)
- Install dependencies: pip install env_canada paho-mqtt
- Configure your the python routine  with your coordinates and MQTT .
- Create the meteo_canada.service see servide file. 
- add the mqqt.yaml sensors as presented . 

For Home Assistant Supervised / OS Users
You can still use this solution:

use Remote Deployment: Install the script on a separate device (Raspberry Pi, secondary server) on your local network. Since it communicates via MQTT, it will push data to your Home Assistant instance seamlessly.

# Files:
- prevision_canada.py: The main collection script.
- requirements.txt: Necessary Python dependencies.
- config example: Template for your Homeasssistant mqtt.yaml settings.
