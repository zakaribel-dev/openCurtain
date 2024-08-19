
# Contrôle de rideau avec Flask et Raspberry Pi

## Prérequis

- Raspberry Pi
- Connected servomotor
- Python 3

## Clone le repo

```bash
git clone https://github.com/zakaribel-dev/openCurtain.git
cd openCurtain
```
## Creez un environnement virtuel
```bash
python3 -m venv venv
source venv/bin/activate
```
## Installez les dépendences
```bash

pip install -r requirements.txt
```
## config
Modifiez openCurtain.py afin d'ajuster le numéro de pin qui va avec votre config (SERVO_PIN).

## Lancez le serveur
```bash
python openCurtain.py
```
## Les routes
Ouverture rideau: http://<RaspberryPiAddress>:5000/open <br>
Fermeture rideau: http://<RaspberryPiAddress>:5000/close
