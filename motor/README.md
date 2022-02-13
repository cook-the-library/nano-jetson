

**setting GPIO as PWM : at terminal**

sudo /opt/nvidia/jetson-io/jetson-io.py

Configure Jetson 40 pin header

Configure header pins manually

choose pwm pins

save / save and reboot

--------------------------------------

**download vscode : AT  terminal**

git clone https://github.com/JetsonHacksNano/installVSCode.git

cd installVSCode

./installVSCode.sh

code

-------------------------------------------------

**motor folder**

-survo_motor : actuating survo motor using PWM (SG90)

-dc_motor_control : 2 phase stepper motor function (28BYJ-48)

-dc_motor : actuating 2 phase stepper motor using dc_motor_control
