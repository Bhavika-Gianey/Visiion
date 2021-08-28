# Vision
## A Wireless Autonomous Ludo Playing Robot 


<p align="center">
 <img  width="500" height="300" src="https://github.com/Robotics-Club-IIT-BHU/Vision-2.0-2020-Arena/blob/main/media/arena.gif"><br>
</p>


## Description
The project is based on applying different components of Image Processing and its applications to build robot capable of autonomous movement.The entire arena has being built using **[PyBullet](https://pybullet.org/) - a python module for physics simulations of robots.** 

## Problem Statement
The task is to complete one round from the starting position to the home position following the instructions given by the throw of a random dice and reaching the next block in the shortest possible time.<br>
Detailed PS : [Problem Statement](https://github.com/Bhavika-Gianey/Visiion/blob/master/Robonex_Pixelate.pdf)

## Installation Guidelines

### Installation Of Virtual Environment
Before installing this arena, you need to download certain modules on which it is dependent. It is **strongly** recommended to use a distribution of **Linux** as the operating system for this project. Windows installations tend to be a hassle and require, in some instances, quite a bit of time and effort to complete.

Although not compulsory,It is **strongly** recommended creating a virtual environment specific to this project. This will help in package management and for decluttering  workspace. A simple way to create a virtual environment is as follows:

   ~~~bash
   pip3 install venv
   python3 -m venv <Env_Name>
   ~~~

   Activation and deactivation of the virtual environment, will be done as specified [here](https://docs.python.org/3/library/venv.html). Scroll down to the table where the activation method for various operating systems is provided. Deactivation, in most cases, can be done by simply typing deactivate while being in in the virtual environment.

### Installation of Main Arena
Once you activate your virtual environment, you will have to install the various dependencies of this project. Follow the following steps:
   * Download/Clone this repository on to your local machine.
   * Navigate to the `Vision-2.0-2020-Arena` folder of this repository through your terminal.
   * Execute the following command in your terminal.

      ~~~bash
      pip install -e vision-arena
      ~~~

   * To check whether the installation has been successful,refer to the guide/cheatsheet to know how to build the gym in your own python script as well as use the utility functions. You can also check this [file](https://github.com/Robotics-Club-IIT-BHU/Vision-2.0-2020-Arena/blob/main/Arena_Test.py) which shows the implementation of a few functions in the guide.

In case there are problems with the PyBullet installation, you can refer to this [guide](https://github.com/Robotics-Club-IIT-BHU/Robo-Summer-Camp-20/blob/master/Part1/Subpart%201/README.md).

### Running the Project
* Navigate to the examples folder.
* Run the solution.py file in your terminal.


## Using the Arena  

0. You will have to import the package vision_arena, which will be available only if you've completed step 1 in the Installation Guidelines. The arena can be initialized by using:

~~~python
env = gym.make("vision_arena-v0")
~~~

1. Then, you will have to create the working loop, as is normally done in pybullet (using `stepSimulation()`).

2. The functions of the environment, available to you for various purposes, are as follows. Please go through the functions themselves in this [file](https://github.com/Robotics-Club-IIT-BHU/Vision-2.0-2020-Arena/blob/main/vision-arena/vision_arena/envs/vision2arena.py), if you wish to know their arguments and/or return values.
   * `env.camera_feed()`  
      This will return an RGB image of the arena as if a camera was placed on top of the arena.
   * `env.remove_car()`  
      This will be used to remove the car from the arena, in case you want to have a good look at it.
   * `env.respawn_car()`  
      This will be used to respawn the car into the arena, **only after removing it**.
   * `env.roll_dice()`  
      This will simulate the rolling of the dice and will give the next shape and colour to which the car shall have to move.
   * `env.move_husky()`  
      This will be used to give the motor velocity to each wheel individually of the car.
   * `env.reset()`
      This will reset the whole arena. This function cannot be used for your final submission.  
  
 3. You can refer the file **helper.py** to see the documentation of the different functions and **aruco_test.py** to see the detection of aruco marker.
      
## A sample arena from the Camera Feed
<p align="center">
 <img  width="400" height="400" src="https://github.com/Robotics-Club-IIT-BHU/Vision-2.0-2020-Arena/blob/main/media/aruco_detected.png"><br>
</p>

Please note that this image is only indicative, and the arena may be be shuffled.

## How it Works
* The main logic is written inside the solution.py file.
* The arena was converted into a 2D matrix using image processing techniques where a particular node number denoted each square of the arena
* Breadth-First Search Path Finding Algorithm was used to determine the shortest path to the destination node
* Nodes were inserted into the list on a priority basis to prefer the inner path
* We used the differential drive to run the bot more efficiently

## Features
* Visual representation of the arena and the bot movements were done using **PyBullet**
* **Image processing** techniques were used to manipulate the data, i.e., shape, colour and aruco marker detection in the programmable form
* **Breadth-First Search Path Finding Algorithm** determined the shortest path to reach the destination node


## Video
Demo Run: [Watch the Video](https://drive.google.com/file/d/1ZgtRm8ausAUuEJxhRXgkqwNrP1t0ITD4/view?usp=sharing)

