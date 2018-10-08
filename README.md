# Overview

The Student Data Manipulator app takes in raw student data and returns updated data
such as the inclusion of email addresses.

## Inputs

The app takes in csv files containing raw student data to be manipulated.

## Outputs

The app outputs csv files containing the updated data.

## Version

Version Number 0.05  
App last updated 25 September 2018  
Readme last updated 9 October 2018

# Operation

- Place the required files into the same directory as the app file
- Run the Student_Data_Manipulator.py file from within Spyder or from the command
line
- Select the desired function from the menu
- Provide the names for any required files or press enter to open the Open file 
dialog.

# Functions

## Add Emails

Adds student emails to a set of student data.

## Required Files

- Emails File
- Student Data File
- Student Data Headings File

## Notes

- The Student Data File will be structured according to the needs of the data that
requires emails added to it.
- Student Data Headings File must contain the headings specific to the provided
Student Data.

# Files used

## Emails File

### File Name

emails.csv

### Contents

Student ID number and Student's email address.

### Structure

CSV file with StudentPK and Email columns.

### Source

Students table of the Student Database.

## Student Data File

### File Name

\<xxx>.csv where \<xxx> is the name that the user has saved the data file with.

### Contents

Contents will depend on what the user needs updating, but at a minimum must include
the Student ID for each student.

### Structure

CSV file with Student ID and any other columns the data contains.

### Source

User-specific.

## Student Data Headings File

### File Name

\<xxx_Headings>.csv where \<xxx> is the name that the user has saved the data file
with.

### Contents

Column name for each column in the Student Data File.

### Structure

TXT file with each column name from the Student Data File on one line, separated
by commas.

### Source

Created from the column headings in the Student Data File.

# Dependencies

- admintools from custtools
- filetools from custtools
- pandas

# Development

## Known bugs

## Items to fix

## Current development step

- Add filtering of email results

## Required development steps

- Add further filtering options

## Future additions