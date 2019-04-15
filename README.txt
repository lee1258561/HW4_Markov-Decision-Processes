For this assignment, most of my source code for the reinforcement learning experiment are credit to the following two implementations from Juan J. San Emeterio and William Ma based on BURLAP.
	Juan J. San Emeterio - https://github.com/juanjose49/omscs-cs7641-machine-learning-assignment-4
	William Ma -  https://github.com/willzma/CS4641-Machine-Learning/tree/master/4.%20MDPs%20and%20Reinforcement%20Learning

I only make some minor changes such as hyperparameter tuning, exploration strategy, and the states reward definition in order to do my experiment. In order to run the code:
	0. git clone https://github.com/juanjose49/omscs-cs7641-machine-learning-assignment-4.git
	1. Do the setup as mentioned in this github repository
		 - Download and install Eclipse IDE.
		 - Import this github project inside of Eclipse.
		 - When the project is imported, right click on the top-level directory shown on the left.
		 - Navigate through context menu to Maven, then click Update Project. This should resolve classpath issues. Note: if you're having issues related to the classpath, or import/dependency issues try to repeat steps 4 and 5.

	2. Right click EasyGridWorldLauncher and select run as java application.
		This will run Policy Iteration, Value Iteration, and Q Learning on a easy grid world and output the result and visualization

	3. Right click HardGridWorldLauncher and select run as java application.
		This will run Policy Iteration, Value Iteration, and Q Learning on a hard grid world and output the result and visualization

	Note that the grid world defined in each file should be change to the correspond MDPs I analyzed in my report to get the correct output.

To run my plotting code:
	0. git clone https://github.com/lee1258561/HW4_Markov-Decision-Processes.git
	1. pip install numpy matplotlib
	3. under the cloned repo, run:
		python plot.py [easyGridWorld|hardGridWorld]
		this will plot all experiment figure in the report based on the data in easyGridData.py/hardGridData.py. you may also plot you own data by copy and paste the result output from the previous reinforcement experiment to the correspond field in easyGridData.py/hardGridData.py.



