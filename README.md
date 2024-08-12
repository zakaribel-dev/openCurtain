Curtain Control with Flask and Raspberry Pi
This project uses Flask to control a motorized curtain via a Raspberry Pi.

Prerequisites
Raspberry Pi with Raspberry Pi OS
Connected servomotor
Python 3
Installation
Clone the Repository

bash
Copier le code
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
<br><br>
python openCurtain.py

<br>
Access the Routes
Open the Curtain: http://<RaspberryPiAddress>:5000/open
Close the Curtain: http://<RaspberryPiAddress>:5000/close
