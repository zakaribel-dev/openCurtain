Curtain Control with Flask and Raspberry Pi

<b>Prerequisites</b> <br> <br>
Raspberry Pi with Raspberry Pi <br>
Connected servomotor <br>
Python 3

<br>
<b>Clone the Repository</b> <br><br>

<br>
git clone https://github.com/zakaribel-dev/openCurtain.git <br>
cd openCurtain <br> <br>

<b>Create a Virtual Environment</b>

<br>

python3 -m venv venv
source venv/bin/activate

<br>
Install Dependencies
pip install -r requirements.txt

<br>
Configuration
Edit openCurtain.py to adjust the GPIO pin numbers to your configuration.

<br>
Run the Server
python openCurtain.py

<br>
Access the Routes
Open the Curtain: http://<RaspberryPiAddress>:5000/open<br>
Close the Curtain: http://<RaspberryPiAddress>:5000/close
