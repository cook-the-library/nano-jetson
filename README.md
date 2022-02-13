# nano-jetson

-------------------------------------------------------

setting jetson nano

tool setting: apt-get update&upgrade

sudo apt-get update

sudo apt-get upgrade

tool setting: text editor & pip, jetson-stats

sudo apt-get install nano

sudo apt-get install python-pip

python3 -m pip install --upgrade pip

sudo -H pip install -U jetson-stats

tool setting : reboot

sudo reboot

tool setting : jetson-stats

jtop



------------------------------------------------------

download vscode

git clone https://github.com/JetsonHacksNano/installVSCode.git

cd installVSCode

./installVSCode.sh

code

--------------------------------------------------------------------


motor folder

-survo_motor : actuating survo motor using PWM (SG90)

-dc_motor_control : 2 phase stepper motor function (28BYJ-48)

-dc_motor : actuating 2 phase stepper motor using dc_motor_control
