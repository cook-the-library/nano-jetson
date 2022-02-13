# nano-jetson SETTING



**setting jetson nano**

tool setting: apt-get update&upgrade

sudo apt-get update

sudo apt-get upgrade

-----------------------------

**tool setting: text editor & pip, jetson-stats**

sudo apt-get install nano

sudo apt-get install python-pip

python3 -m pip install --upgrade pip

sudo -H pip install -U jetson-stats

**tool setting : reboot**

sudo reboot

**tool setting : jetson-stats**

jtop

**tool setting : display manager**

sudo apt-get install lightdm

sudo apt-get purge gdms

--------------------------------------

**increasing memory**

sudo apt-get install dphys-swapfile

sudo nano /sbin/dphys-swapfile

CONF_SWAPSIZE=4096

CONF_SWAPFACTOR=2

CONF_MAXSWAP=4096

**THEN, ctrl + x, y, Enter**

**same with**

sudo nano /etc/dphys-swapfile

**reboot**

free -m

**and check memory 6074**

----------------------


# OPENCV 4.5.4 WITH  CUDA

wget https://github.com/Qengineering/Install-OpenCV-Jetson-Nano/raw/main/OpenCV-4-5-4.sh

sudo chmod 755./OpenCV-4-5-4.sh

./OpenCV-4-5-4.sh

**check OpenCV: 4.5.4 compiled CUDA: YES with jtop**

---------------------------------

**YOLOv5**

get clone https://github.com/ultralytics/yolov5

cd yolov5

wget https://github.com/ultralytics/yolov5/releases/download/v6.0/yolov5s.pt

**download all modules inside requirements one by one**

**check**

cd yolov5

python3 detect.py --source ./data/images

----------------------------------

**webcam**

ls /dev/video*

**print /dev/video**

python3 detect.py --source 0

**for external trained model, mode to yolov5 directroy & --weights model_name.pt**

--------------------------

**CSI camera at home directory**

wget https://github.com/ArduCAM/MIPI_Camera/releases/download/v0.0.3/install_full.sh
chmod +x install_full.sh
./install_full.sh -m imx477

**reboot**

git clone https://github.com/amirhosseinh77/JetsonYolo.git
cd JetsonYolo
python3 JetsonYolo.py
