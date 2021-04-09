# PySpectrometer

***Raspberry Pi Spectrometer***

![Screenshot](media/fluorescent.png)

The PySpectrometer is a Python implementation of an optical spectrometer. The motivation beind this project was to build a tool that could measure the wavelength of home-made Dye Lasers and perform some fluorescence spectroscopy.

The hardware is simple and widely avilable and so should be easily to duplicate without critical alignment or difficult construction. The hard work was developing the software.

Visit my Youtube Channel at: https://www.youtube.com/leslaboratory

This program and assiciated information is free for non-commercial use, but if you have gotten value from these kinds of projects and think they are worth something, please consider donating: https://paypal.me/leslaboratory?locale.x=en_GB

***TODO***

(Maybe) Impement suitable 3 wavelength Calibration protocol to compensate for non linearity caused by poor alignment


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

Rasberry pi 4 and PiCamera Recommended. 

(Note the software uses the Linux Video Driver, not the Picam Python module. As a consequence it is camera agnotstic, so it will work with some webcams on probably any Linux box) 

First attach the Picam, and enable it with raspi-config

Install the dependencies:

sudo apt-get install python3-opencv

sudo apt-get install python-dev libatlas-base-dev

pip3 install scipy

pip3 install peakutils


Run the program with: python3 pyspectrometer-v1.py


To calibrate, shine 2 Lasers of known wavelength (He-Ne, Argon or DPSS recommended! (Diode Lasers can have wavelengths that can be +/- several nm!)) at a piece of card in front of the spectrometer.

Click the two peaks on the graph, and in each of the boxes enter the corresponding wavelength. Then hit 'Calibrate'. In this example I have Calibrated with 532nm (DPSS) and 633nm He-Ne. The Scale and lablels will then adjust to match your values.

For good accuracy make sure your wavelengths are quite far apart, ideally one at the red end and one at the blue end

![Screenshot](media/calib.png)

Alternatively, you may use a Fluorescent tube (or any other gas discharge tube) in front of the Spectrometer, you will have to research the wavelengths of the emission lines (Mercury for Fluorescent tubes, Neon, Argon, Xeonon for other types) That will be an excercise for you! If you are feeling particularly adventurous, you could calibrate with plain daylight (do NOT point it at the Sun!) and use the fraunhofer lines to perform your calibration!

***Other settings***

"Label Peak width" and "Label threshold" set the width of a peak to label, and the level to consider it a peak respectively. The Defaults ae fine, but if you find the graph too cluttered, you can play with these values.

Snapshot, takes a snapshot of the graph section like this:
![Screenshot](media/spectrum-09-04-2021-15:19:27.jpg)


***Example Spectra***

Here is an example of the spectra of a fluorescent bulb (there is slight non linearity toward the blue)
![Screenshot](media/fluorescent.png)

Measuring the wavelength of a cheap red laser pointer (661nm)
![Screenshot](media/pointer.png)

Measuring the wavelength of a cheap violet Laser pointer, note the strong fluorescence from the paper! Paper is optically brightened with a fluorescent dyes.Most likely Coumarin.

Also note the wavelength is 8nm out, due to misalignment.
![Screenshot](media/uv.png)

The spectra of Daylight (pointed out of the window at a blue sky)
![Screenshot](media/daylight.png)








