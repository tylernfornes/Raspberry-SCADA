# Modbus SCADA Project
This project is intended to build a Modbus SCADA network between multiple raspberry pi's with a temperature sensor and two colored lights. If the temperature rises above a given threshold, the lights will change (one will go off and the other will come on).

To deploy on Raspbian, run the following commands:

```
git clone https://github.com/tylernfornes/Raspberry-SCADA
cd Raspberry-SCADA
sudo ./deploy.sh
```

Hardware Requirements:
* 1x DS18B20+ Temperature Sensor (http://www.mouser.com/ProductDetail/Maxim-Integrated/DS18B20+/?qs=7H2Jq%252byxpJKegCKabDbglA%3D%3D)
* 2x Raspberry Pis
* 1x SunFounder Sidekick Basic Starter Kit (http://www.amazon.com/SunFounder-Sidekick-Breadboard-Resistors-Mega2560/dp/B00DGNZ9G8)

To wire the Raspberry Pi GPIO pins using WiringPi (installed using the deploy.sh script), follow the documentation on http://wiringpi.com/pins/

