## Preface
This is a small project I decided to work on. I got a skull from the dollar store that had a moving jaw and I thought why not try and motorize it.  I did some searching online and found some traces of [JawDuino](https://www.servomagazine.com/magazine/article/bob-the-talking-skull-controlled-by-jawduino) but I wanted to use a Raspberry Pi and Python(*since I'm slowly working on learning python*). 

This isnt a complete project. Current *(As of Oct 29, 2019)* all the attached code will do is move the jaw in a somewhat smooth fashion - this is completed by running a range that takes the initial number of 4, deviding that 10.0 then adding 3. The end goal is to control the jaw using a PWM signal from a hat. It will take an audio file and turn the audio spectrum into a PWM signal to control the servo. 

## Parts

* Raspberry Pi 3
* EMAX ES08A II servo
* Some sort of skull?
* jumper wires, etc

*Some photos can be found in the doc folder*

## Schematic

Here is a down & dirty schematic:

![pinout](https://github.com/scottyedmonds/skull-monster-mash/blob/master/doc/MonsterMashSkull%20Pinout_bb.png)

## Setup

**Please Note** If the below steps arent straight forward to you, you may want to check on YouTube for videos on getting started with a Raspberry Pi and Raspbian. I probably missed something, or it just wont work like it should - some basic knowledge and troubleshooting may be needed. 

1. Get the latest image of [Raspbian Lite](https://www.raspberrypi.org/downloads/raspbian/) - *current version was Buster as of writing this*
2. Write to an SD card using [Etcher](https://www.balena.io/etcher/) - *This is avaialble for Windows, Linux and even MacOS*
3. Boot the pi - default login is username: pi | password: raspberry
4. Connect to wifi using raspi-config tool, access with the command `sudo raspi-config` 
5. Once connected to wifi, let's update & upgrade using `sudo apt-get update && sudo apt-get upgrade -y` 
6. Probably a good time to reboot, do a `sudo reboot`
7. Let's install python3 and pip
* `sudo apt install python3.8` -- This will install Python 3.8 which is the latest as of writing this.
* `sudo apt install python3-pip` -- You will *(wait do you actually for this?)* also need pip installed. 
8. You should now have the latest python 3.8 and pip installed, check by doing `python3.8 -V` and `pip3 -V`
9. Do a `sudo nano servo.py` in the root directory, paste the code from the file above and save using **Ctrl+X** then **y** then **Enter**
10. Now you should be able to run the code using the command `python3.8 servo.py`


## To-Do

Some to-do items for Halloween 2020

* Find a hat that will translate an audio file into PWM to better control the jaw
* Add button or proximity sensor to trigger **or** *Idea: Use an ESP8266 hooked to the doorbell to trigger*
* Get better with python