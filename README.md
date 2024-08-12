Curtain Control with Flask and Raspberry Pi

Prerequisites
Raspberry Pi with Raspberry Pi 
Connected servomotor
Python 3

<br><br>
Clone the Repository

<br><br>
git clone https://github.com/zakaribel-dev/openCurtain.git
cd openCurtain
Create a Virtual Environment

<br><br>

python3 -m venv venv
source venv/bin/activate

<br><br>
Install Dependencies
pip install -r requirements.txt

<br><br>
Configuration
Edit openCurtain.py to adjust the GPIO pin numbers to your configuration.

<br><br>
Run the Server
python openCurtain.py

<br><br>
Access the Routes
Open the Curtain: http://<RaspberryPiAddress>:5000/open<br>
Close the Curtain: http://<RaspberryPiAddress>:5000/close
