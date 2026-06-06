# 🔒 IoT Surveillance — Raspberry Pi Pico W

Système de surveillance IoT basé sur le **Raspberry Pi Pico W**, simulé sur **Wokwi** et piloté via **Node-RED** avec un dashboard temps réel.

## 📁 Structure du projet
iot-surveillance-pico/
├── wokwi/
│   ├── diagram.json       # Schéma de simulation Wokwi
│   └── wokwi.toml         # Configuration Wokwi
├── bridge/
│   └── bridge.py          # Script Python MQTT bridge
├── node-red/
│   └── flows.json         # Flux Node-RED exportés
├── dashboard/
│   └── dashboard.html     # Interface web du dashboard
└── README.md

## ⚙️ Technologies utilisées

- 🟢 **Raspberry Pi Pico W** — microcontrôleur principal
- 🔵 **Wokwi** — simulation en ligne
- 🟠 **MicroPython** — programmation du Pico
- 🔴 **MQTT** — protocole de communication IoT
- 🟣 **Node-RED** — orchestration des flux de données
- 🌐 **HTML/JS** — dashboard de visualisation

## 🚀 Lancement

1. Ouvrir **Wokwi** avec `wokwi/diagram.json`
2. Lancer le bridge : `python bridge/bridge.py`
3. Importer `node-red/flows.json` dans Node-RED
4. Ouvrir `dashboard/dashboard.html` dans le navigateur
   
