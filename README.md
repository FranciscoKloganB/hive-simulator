# hive-simulator

##  Description
The present repository contains a custom cycle-based P2P simulator with perfect failure detection, used to test the performance of our implementation of Probabilistic Swarm Guidance Algorithms in a Distributed File Storage environment. 

##  Installation
This project is implemented using Python 3.7.6. You are free to use any version you desire, but we do not guarantee the simulator will work under such conditions. We know that any version launched before 3.7.x will not run this project. We also recommend using an IDE such as PyCharm or equivalent for easier usage.

1. Download and install Python 3.7.7
https://www.python.org/downloads/release/python-377/

2. Download our repository

3. Create a virtual environment of your choosing.
https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/

4. Install project dependencies by opening your terminal and inserting the command:
```
  pip install -r requirements txt
```

## Usage
For easier usage, the projects includes a script to create simulation files and another script to run them as many times as you desire.

1. Place a file or files you wish to test durability inside the folder /app/static/shared. We provide a 8.78MB game and a 45.0MB raw photo.

2. Create a simulation file by executing the following commands in order:
```
  cd app
  python simulation_file_generator.py --simfile=<str: file name>.json
```

3. Follow the instructions asked in the script. The script is documented so you can change it if you think something should be done differently. When you are done a new file will be generated in the /app/static/outfiles folder.

4. Execute the simulation file by executing:
```
  python simulation_file_generator.py --simfile=<str: file name>.json --epochs=<int: number of executions>
```

5. The simulation may take a while to run, especially if you have large P2P groups. The simulator was not designed for performance and is only result oriented. When simulation instances or groups within it terminate, output files are generated in folder /app/static/outfiles

6. Generate graphs of your choice by app/scripts/pyscripts and running the script you want:
```
  python <str:script name>.py --meandir=<str: folder name, where you placed your outfiles> --istate=<char: initial state {i, u, a}>
```
