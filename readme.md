# CPU temperature Interpolation and Least-Squares Approximaton program

A python program that currently just parses a text file and formats the information in that file in a 
format that will be used for later Interpolation and Least-Squares Approximation calculations.


# Requirements

  * Python 3.9

> This code makes use of generic type hints which require python 3.9 and later

# Input Formatting

Input must a valid file name passed as a string. 
The main program will strip extra whitespace before 
or after the file name; but that is the extent of input validation.

# Sample Execution & Output

After changing to the 
```
./CPU_temp_program
```
directory in the terminal, run the command
```
python main.py
```

Then type your file name into the command line.

The output will be 

```
Temperature dataset: {filename}
{interval 1} seconds: [temperature list]
{interval 2} seconds: [temperature list]
........
```

