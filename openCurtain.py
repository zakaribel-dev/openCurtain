from flask import Flask, jsonify
import RPi.GPIO as GPIO
import time

app = Flask(__name__)


SERVO_PIN = 18  # broche 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(SERVO_PIN, GPIO.OUT)


pwm = GPIO.PWM(SERVO_PIN, 50)  # 50hz
pwm.start(0)

def set_servo_angle(angle):
    duty_cycle = (angle / 18) + 2
    GPIO.output(SERVO_PIN, True)
    pwm.ChangeDutyCycle(duty_cycle)
    time.sleep(1)
    GPIO.output(SERVO_PIN, False)
    pwm.ChangeDutyCycle(0)

@app.route('/')
def home():
    return "Welcome !!"

@app.route('/open', methods=['GET'])
def open_curtain():
    set_servo_angle(90)  
    return jsonify({"status": "Curtain opened"}), 200

@app.route('/close', methods=['GET'])
def close_curtain():
  -
    set_servo_angle(0)  
    return jsonify({"status": "Curtain closed"}), 200

@app.route('/shutdown', methods=['GET'])
def shutdown():
    pwm.stop()
    GPIO.cleanup()
    return jsonify({"status": "Shutting down"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
