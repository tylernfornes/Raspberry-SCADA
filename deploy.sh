git clone git://git.drogon.net/wiringPi
cd wiringPi
git pull origin
./build
cd ..
# initialize the registers to be output registers
gpio mode 0 out
gpio mode 1 out
# enables gpio device at boot
`exec dtoverlay=w1-gpio`
sudo modprobe w1-gpio
sudo modprobe w1-therm
sudo apt-get install python-dev
sudo pip install pymodbus Twisted pycrypto
