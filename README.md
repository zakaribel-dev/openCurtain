
Copier le code
# Curtain Control with Flask and Raspberry Pi

## Prerequisites

- Raspberry Pi
- Connected servomotor
- Python 3

## Clone the Repository

```bash
git clone https://github.com/zakaribel-dev/openCurtain.git
cd openCurtain
Create a Virtual Environment
bash
Copier le code
python3 -m venv venv
source venv/bin/activate
Install Dependencies
bash
Copier le code
pip install -r requirements.txt
Configuration
Edit openCurtain.py to adjust the GPIO pin numbers to your configuration.

Run the Server
bash
Copier le code
python openCurtain.py
Access the Routes
Open the Curtain: http://<RaspberryPiAddress>:5000/open
