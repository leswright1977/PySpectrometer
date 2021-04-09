# PySpectrometer

***Raspberry Pi Spectrometer***

![Screenshot](media/fluorescent.png)

The PySpectrometer is a Python implementation of an optical spectrometer. The motivation beind this project was to build a tool that could measure the wavelength of home-made Dye Lasers and perform some fluorescence spectroscopy.

The hardware is simple and widely avilable and so should be easily to duplicate without critical alignment or difficult construction. The hard work was developing the software.

Visit my Youtube Channel at: https://www.youtube.com/leslaboratory

This program and assiciated information is free for non-commercial use, but if you have gotten value from these kinds of projects and think they are worth something, please consider donating: https://paypal.me/leslaboratory?locale.x=en_GB

***TODO***

(Maybe) Impement suitable 3 wavelength Calibrtion protocol to compensate for non linearity caused by poor alignment


***Hardware***

![Screenshot](media/scope.png)

The harware consists of: 

A commercial Diffraction grating Spectroscope

A Raspberry Pi Camera (with an M12 Thread)

A CCTV Lens with Zoom (M12 Thread)

Everything is assembled on an aluminium base (note the Camera is not cooled, the heatsink was a conveniently sized piece of aluminium.

![Screenshot](media/parts.png)

***Installation***
Developed and tested on: 2021-01-11-raspios-buster-armhf-full.img for anything else your milage may vary!

Rasberry pi 4 Recommended.

First attach the Picam, and enable it with raspi-config

Install the dependencies:

sudo apt-get install python3-opencv
sudo apt-get install python-dev libatlas-base-dev
pip3 install scipy
pip3 install peakutils

Run the program with: python3 pyspectrometer-v1.py


To calibrate, shine 2 Lasers of known wavelength (He-Ne, Argon or DPSS recommended! (Diode Lasers have wavelengths that can be +/- 10nm!)) at a piece of card in front of the spectrometer.

Click the two peaks on the graph, and in each of the boxes enter the corresponding wavelength. Then hit 'Calibrate'. In this example I have Calibrated with 532nm (DPSS) and 633nm He-Ne. The Scale and lablels will then adjust to match your values.

![Screenshot](media/calib.png)








