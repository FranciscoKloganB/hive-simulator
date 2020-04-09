# hive-simulator

##  Description
The present repository contains a custom cycle-based P2P simulator with perfect failure detection, used to test the performance of our implementation of Probabilistic Swarm Guidance Algorithms in a Distributed File Storage environment. 

##  Installation
This project is implemented using Python 3.7.6. You are free to use any version you desire, but we do not guarantee the simulator will work under such conditions. We know that any version launched before 3.7.x will not run this project. We also recommend using an IDE such as PyCharm or equivalent for easier usage.

1. Download and install Python 3.7.7
  > * https://www.python.org/downloads/release/python-377/

2. Download our repository

3. Create a virtual environment of your choosing.
  > * https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/

4. Install project dependencies by opening your terminal and inserting the command:
```
  pip install -r requirements.txt
```

## Usage
We recommend that you read the paper that describes the purpose behind the creation of this repository before proceeding. You can find it in /docs folder.

For easier usage, the projects includes a script to create simulation files and another script to run them as many times as you desire. For the most part, scripts, packages and modules are extensively documented. If you have any doubts, regarding functionality or because you do not understand why I do a function or method in some way, you may contact me, but I am not available to help with installation problems as that can be dependant on many factors. You can also contact me to make improvement suggestions or inform me of something I might be doing wrong.

1. Place a file or files you wish to test durability inside the folder hive/app/static/shared. We provide a 45.0MB raw photo.

2. Create a folder named 'outfiles' and another folder named 'simfiles' inside hive/app/static/

3. Create a simulation file by executing the following commands in order:
```
  cd hive
  cd app
  python simulation_file_generator.py --simfile=<str: file name>.json
```

4. Follow the instructions asked in the script. The script is documented so you can change it if you think something should be done differently. When you are done a new file will be generated in the hive/app/static/outfiles folder.

5. Change the global variables in hive/app/globals/globals.py to what you desire. The meaning of these variables are commented and are used to change simulation settings and, among others, include:
	1. MAX_EPOCHS
	2. READ_SIZE
	3. MIN_DETECTION_DELAY
	4. MAX_DETECTION_DELAY
	5. REPLICATION_LEVEL
	6. ...

6. Execute the simulation file by executing:
```
  python simulation_file_generator.py --simfile=<str: file name>.json --epochs=<int: number of executions>
```

7. The simulation may take a while to run, especially if you have large P2P groups. The simulator was not designed for performance and is only result oriented. When simulation instances or groups within it terminate, output files are generated in folder hive/app/static/outfiles

8. Generate graphs of your choice by hive/app/scripts/pyscripts and running the script you want:
```
  python <str:script name>.py --meandir=<str: folder name, where you placed your outfiles> --istate=<char: initial state {i, u, a}>
```
