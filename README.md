# INF560_hw7
# instruction to Create a virtual environment and run code [ In Windows System ]


## step one:
Clone the repository to local. 

Way One: Downloading the App and clone the repository from the App.

Way Two: Getting into the terminal and using code : git clone [git address]

Way Three: Downloading the zip file of that repository


## Step Two:
Installing virtualenv by calling this code in the terminal:

>> pip install virtualenv

Then run the following code, env is the name of the environment or name of the path(you could change it):

>> py -m venv env

After using this code you will have a document called env; then, you could activate it by:

>> .\env\Scripts\activate


## Step Three:
After you called the code above, you enter the virtual envirment. Now, you need to install the all the package we need, using:

>> pip install -r requirement.txt

Now you can run the code by:

>> bokeh serve ./result.py


This is the picture to run the code:

![image](https://user-images.githubusercontent.com/54834260/98059831-ee2fb480-1dfc-11eb-83a6-ad14b2de5baf.png)

Then for stop running using ctrl + C to stop it.

## Step Four(Optional for user not push the file to Github):
Quiting the virtual environment, by:

>> deactivate

Because we don't want to upload the environment so we need to write a file called .gitignore to omit the env file:

>> vim .gitignore

You will entering the .gitignore file and could edit it by pressing i button; after that, write the code:

>> env/

Then, press ESC and enter: 

>> :wq!

Now, you done with the .gitignore file editing.
