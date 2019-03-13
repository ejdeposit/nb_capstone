the Readig Group Scheduler program will load the list of students from the file students.csv.  More students can be 
added to the file by inserting addional rows, but the user should not edit the number of columns.

the Reading Group Scheduler Program will load the schedule of teachers from the teachers.csv file.  More staff 
members can be added to the file by adding additional rows, but the user should not modify the number of columns.

To run the program, enter the following at the command line:
---------------------------------------------------------------------------------------------------------------------
user$ python3.6 driver.py
---------------------------------------------------------------------------------------------------------------------
the program will then prompt you to enter information to customize the schedule.  Alternatively, to run the program
with out entering all the schedule parameters at the command line. You may redirect input from the testInput.txt file
by typeing the the following at the command line:
---------------------------------------------------------------------------------------------------------------------
user$ python3.6 driver.py < testInput.txt
---------------------------------------------------------------------------------------------------------------------

After running, the program will create two csv files: teacher_sched.csv and student_sched.csv.  Open this files to
view the schedules created by the program.
