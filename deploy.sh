git clone git://git.drogon.net/wiringPi
cd wiringPi
git pull origin
./build
cd ..
# initialize the registers to be output registers
gpio mode 0 out
gpio mode 1 out
# enables gpio device at boot
echo "dtoverlay=w1-gpio" >> /boot/config.txt
sudo modprobe w1-gpio
sudo modprobe w1-therm
sudo apt-get -y install python-dev python-pip
sudo pip install pymodbus Twisted pycrypto
