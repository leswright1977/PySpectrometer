
***PySpectrometer2 released!!***
Check it out at: https://github.com/leswright1977/PySpectrometer2


***Update Sept 27th 2022***
A new Raspberry Pi OS Bullseye compatible version of this software is now available in src/PySpectrometer-3.2!
This is a quick ugly hack to simply get this thing working on Bullseye and keep everyone happy, whilst I get time to work on the latest and greatest version of this software.

For now, simply download the contents of 3.2, read the new README file, install the dependencies, uses raspi-config to enable legacy camera support and have fun!




***Update Sept 25th 2022***
It seems Raspberry Pi OS Bullseye, has broken everything (camera software has significantly changed, peakutils is broken, scipy is broken, and it looks like they are preventing installation of the older versions of the OS!...) :-(

I am in the proceess of a brand new build, which will incorporate all of the features that folk have asked for previously including:

Ditching reliance on too many external libraries (scipy and peakutils).

Ditching the TK interface, for leaner, more maintainable software. Simple key bindings will allow all the functionaility of previous versions.
Resizable window for the spectrometer display.

A waterfall display (for those of us measuring changes over time).

Windows compatible filenames for the data.

I may incorporate some other changes as well (time permiting, I will have a look at issues, and see what I can rustle up.




# PySpectrometer 2021-03-05

***Update 2021-10-30 The software works well on the new Raspberry Pi Zero 2 W!***

***V3 is now released that can export CSV, and has a peak hold feature! Scroll to bottom for changes!***

***This program, hardware design, and associated information is Open Source (see Licence), but if you have gotten value from these kinds of projects and think they are worth something, please consider donating:*** https://paypal.me/leslaboratory?locale.x=en_GB

***Raspberry Pi Spectrometer***

![Screenshot](media/fluorescent.png)

The PySpectrometer is a Python (OpenCV and Tkinter) implementation of an optical spectrometer. The motivation beind this project was to build a tool that could measure the wavelength of home-made Dye Lasers and perform some fluorescence spectroscopy. Most importantly at a cost that is in reach of everyone!

The hardware is simple and widely avilable and so should be easily to duplicate without critical alignment or difficult construction. The hard work was developing the software.

Resolution/accuracy seems to be +/- a couple of nm or so, pretty reasonable for the price of the hardware, especially when you consider the price of commercial components such as the Hamamatsu C12880MA breakout boards which run north of 300 bucks, and has a resolution of 15nm. Of course, this build is physically much larger, but not enormous!


Visit my Youtube Channel at: https://www.youtube.com/leslaboratory

Videos of this project are here:


[![Raspberry Pi Spectrometer](https://img.youtube.com/vi/T_goVwwxKE4/0.jpg)](https://www.youtube.com/watch?v=T_goVwwxKE4 "Raspberry pi Spectrometer")

[![Software Update](https://img.youtube.com/vi/dm3woVQp8Xc/0.jpg)](https://www.youtube.com/watch?v=dm3woVQp8Xc "Software Update")

[![MINIATURE Raspberry Pi Spectrometer](https://img.youtube.com/vi/Tw3HJEhE2dI/0.jpg)](https://www.youtube.com/watch?v=Tw3HJEhE2dI "MINIATURE Raspberry pi Spectrometer")

***Hardware***

![Screenshot](media/scope.png)

The hardware consists of: 

***A commercial Diffraction grating Spectroscope***
https://www.patonhawksley.com/product-page/benchtop-spectroscope

***A Raspberry Pi Camera (with an M12 Thread)***
https://thepihut.com/products/raspberry-pi-camera-adjustable-focus-5mp

***A CCTV Lens with Zoom (M12 Thread)*** 
(Search eBay for F1.6 zoom lens)

Everything is assembled on an aluminium base (note the Camera is not cooled, the heatsink was a conveniently sized piece of aluminium.)

![Screenshot](media/parts.png)

![Screenshot](media/pi.png)


***For the MINIATURE version the hardware is:***


![Screenshot](media/minispect.png)

***A commercial Diffraction grating Pocket Spectroscope:*** https://www.patonhawksley.com/product-page/pocket-spectroscope

***A Raspberry Pi Camera (with an M12 Thread):*** https://thepihut.com/products/raspberry-pi-camera-adjustable-focus-5mp

***M12x0.5 F2.0 Fixed 12mm Focal length Lens:*** https://www.ebay.co.uk/itm/114551239930

***Installation***

Developed and tested on: 2021-01-11-raspios-buster-armhf-full.img for anything else your milage may vary!

Rasberry pi 4 and PiCamera Recommended. 

(Note the software uses the Linux Video Driver, not the Picam Python module. As a consequence it will work with some webcams on probably any Linux box (Tested on Debian with a random webcam)) 

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

Alternatively, you may use a Fluorescent tube (or any other gas discharge tube) in front of the Spectrometer, you will have to research the wavelengths of the emission lines (Mercury for Fluorescent tubes, Neon, Argon, Xenon for other types) That will be an excercise for you!


***Other settings***

"Label Peak width" and "Label threshold" set the width of a peak to label, and the level to consider it a peak respectively. The Defaults are fine, but if you find the graph too cluttered, you can play with these values.

Snapshot, takes a snapshot of the graph section like this:
![Screenshot](media/spectrum-09-04-2021-15:19:27.jpg)


***Example Spectra***

Here is an example of the spectrum of a fluorescent bulb. The peaks at 405,435,545,650 are Mercury, Europium (one of the lamp phosphors) is visible at ~610nm.

![Screenshot](media/fluorescent.png)

Measuring the wavelength of a cheap red laser pointer (661nm)

![Screenshot](media/pointer.png)

Measuring the wavelength of a cheap violet Laser pointer, note the strong fluorescence from the paper! Paper is optically brightened with a fluorescent dyes, most likely Coumarin.

![Screenshot](media/uv.png)

The spectrum of Daylight (pointed out of the window at a blue sky)

![Screenshot](media/daylight.png)


The spectrum of of a Helium-Neon Discharge.

![Screenshot](media/henespectrum.png)


Minimum smoothing applied:

![Screenshot](media/maxres.png)

Maximum smoothing applied:

![Screenshot](media/maxsmooth.png)

***Version 3***

Version 3 has a Peak hold feature to detect transient events, such as a Laser pulse, or a Camera Flash!

![Screenshot](media/v3.png)

Pressing the snapshot button also dumps data to a CSV file. This is far more accurate data than the graph window, and can be imported into OpenOffice on the Pi.

![Screenshot](media/csv.png)

***Note: Filenames have colons in them. Unix like OS's e.g. Linux have no issue, but you will find that you have to rename these if you want to import to Windows!***

![Screenshot](media/tuning-curves.png)

Tuning curves obtined from a home-made pulsed Dye Laser.
From Left to right: Coumarin-1,Rhodamine 6G, Rhodmine B.

***TODO***
Add in a 3 wavelength Calibration functionality to counteract nonlinearity.




