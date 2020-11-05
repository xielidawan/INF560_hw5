# INF560_hw7
# instruction to Create a virtual environment and run code [ In Windows System ]

## Part1: Local environment runing

### step one:
Clone the repository to local. 

Way One: Downloading the App and clone the repository from the App.

Way Two: Getting into the terminal and using code : 
>> git clone https://github.com/xielidawan/INF560_hw5.git INF560_hw5

Way Three: Downloading the zip file of that repository


### Step Two:

Installing virtualenv by calling this code in the terminal:

>> pip install virtualenv

Then, Getting into the file that you download:

![image](https://user-images.githubusercontent.com/54834260/98066273-68ffcc00-1e0b-11eb-97d4-54d423c93e04.png)

And runing the following code, env is the name of the environment or name of the path(you could change it):

>> py -m venv env


![image](https://user-images.githubusercontent.com/54834260/98066363-9e0c1e80-1e0b-11eb-8359-145d9f8efcb2.png)

After using this code you will have a document called env; then, you could activate it by:

>> .\env\Scripts\activate

![image](https://user-images.githubusercontent.com/54834260/98066382-ac5a3a80-1e0b-11eb-8e84-c8c2d121b09e.png)


### Step Three:
After you called the code above, you enter the virtual envirment. Now, you need to install the all the package we need, using:

>> pip install -r requirement.txt

Now you can run the code by:

>> bokeh serve ./result.py


This is the picture to run the code:

![image](https://user-images.githubusercontent.com/54834260/98059831-ee2fb480-1dfc-11eb-83a6-ad14b2de5baf.png)

Then, it is runing and you could go to on your broswer and play with it.

Then for stop running using ctrl + C to stop it.

Quiting the virtual environment, by:

>> deactivate

### Step Four(Optional for user push the file to Github):

Because we don't want to upload the environment so we need to write a file called .gitignore to omit the env file:

>> vim .gitignore

You will entering the .gitignore file and could edit it by pressing i button; after that, write the code:

>> env/

Then, press ESC and enter: 

>> :wq!

Now, you done with the .gitignore file editing.

## Part2: Runing on Docker

### Step One:
Download the docker stable on docker official website and install it.
Clone the repository to local. 

Way One: Downloading the App and clone the repository from the App.

Way Two: Getting into the terminal and using code : git clone https://github.com/xielidawan/INF560_hw5.git INF560_hw5

![step1](https://user-images.githubusercontent.com/54834260/98189100-200e4d00-1ec9-11eb-9263-443ababe47e8.png)

### Step Two:

Enter to the file that you download, in this case is INF560_hw5:

>> cd INF560_hw5

![step2](https://user-images.githubusercontent.com/54834260/98189199-4df39180-1ec9-11eb-9466-dee3910fb883.png)

Then, build the image using code:
>> docker build --tag inf560_hw5 .

![build_image](https://user-images.githubusercontent.com/54834260/98189333-9743e100-1ec9-11eb-8288-d96e3c96ad90.png)

And wait it finish:

![finish_building](https://user-images.githubusercontent.com/54834260/98189360-acb90b00-1ec9-11eb-9ff6-4787f5648176.png)

Also you could check is the image created, by this code:
>> docker images

If you see the image called inf560_hw5, then, it's correct.

![check_build_or_not](https://user-images.githubusercontent.com/54834260/98189413-c8241600-1ec9-11eb-923f-4fe7500ae9d3.png)

### Step Three:
Now we could run the result.py file by calling this code:

>> docker run -p 5006:5006 -it inf560_hw5

Because I am windos and I need to use an extra word winpty:

>> winpty docker run -p 5006:5006 -it inf560_hw5

This is the pricture to run the code on my machine:

![run_code_on_my_machine](https://user-images.githubusercontent.com/54834260/98189817-99f30600-1eca-11eb-992e-ab69fbc2cdd2.png)

Then, it is runing and you could go to on your broswer and play with it.

Finnally, for stop running using ctrl + C to stop it.
