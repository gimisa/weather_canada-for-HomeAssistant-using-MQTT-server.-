import sys
import time

# --- MESSAGE LOCAL DE DÉMARRAGE IMMÉDIAT ---
print("==================================================")
print(f" Lancement local du script : {sys.argv[0]}")
print(f" Heure locale : {time.strftime('%H:%M:%S')}")
print(" Statut : En cours d'initialisation...")
print("==================================================")

import asyncio
import json
import paho.mqtt.publish as publish
from env_canada import ECWeather

lat, lon = 45.40, -72.73             # <<<  CHANGE for your location 
MQTT_BROKER = "192.168.2.113"        # <<< MQTT server IP . 
TOPIC_METEO = "gimisa/meteo/granby"  # <<< CHANGE for your location 

async def collecter_meteo():
    try:
        print("[3] Connexion aux serveurs d'Environnement Canada...")
        ec = ECWeather(coordinates=(lat, lon))
        
        print("[4] Téléchargement des données météo (update)...")
        await ec.update()
        print("[5] Données reçues avec succès d'ECCC.")
        
        payload = {
            "temperature": ec.conditions.get("temperature", {}).get("value"),
            "condition": ec.conditions.get("condition", {}).get("value"),
            "humidite": ec.conditions.get("humidity", {}).get("value"),
            "vent_vitesse": ec.conditions.get("wind_speed", {}).get("value"),
            "pression": ec.conditions.get("pressure", {}).get("value"),
            "alerte_active": "Aucune" if not ec.alerts else list(ec.alerts.keys())[0]
        }
        
        print(f"[1] Envoi réseau unifié (QoS 1 + Retain) vers {MQTT_BROKER}...")
        
        # Envoi direct qui attend la confirmation du broker
# Envoi direct avec authentification obligatoire
        publish.single(
            topic=TOPIC_METEO,
            payload=json.dumps(payload),
            qos=1,
            retain=True,
            hostname=MQTT_BROKER,
            port=1883,
            auth={
                'username': "USER",      # <<<<  MQTT user 
                'password': "PASS"       # <<<<  MQTT password 
            }
        )
        
        print(f"[{time.strftime('%H:%M:%S')}] Météo envoyée et confirmée par le broker !")
        
    except Exception as e:
        print(f"[ERREUR] Échec durant la collecte ou l'envoi : {e}")

async def main():
    while True:
        await collecter_meteo()
        print("[7] Sommeil de 15 minutes...")
        await asyncio.sleep(900)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nArrêt du script.")
