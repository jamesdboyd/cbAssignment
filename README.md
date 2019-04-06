Carbon Black Technical Screen Assignment

I decide to implement the code using python 3.5. I also decided to use the python requests and argparse packages. 
I implemented the -w and -u options and started to implement the -b but I guess you only whanted two to be completed. 
The main program is called dothings.py, and it provides a help option:

./dothings.py -h | --help

I used the builtin unittest package to implement the unit tests and the unit tests are located under the test directory.
To run the test do the following:

python -m unittest -v test/test_location.py
python -m unittest -v test/test_utilities.py

I've also put this project out on githup.  To clone the repository do the following:

git clone https://github.com/jamesdboyd/cbAssignment.git destinationDirectory

I would have liked to implement the other options, and also provided a Java solution and maybe I do that in my space time,
hence the reason for putting it on github. I also only focused on implement code for Linux only and would have liked to
have provided a solution that would run on other platforms, ex Windows.

I did my testing on Ubuntu 16.04 and 18.04. I also implemented logging and the default log is log/default.log
