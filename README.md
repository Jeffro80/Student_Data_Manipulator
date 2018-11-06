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
Readme last updated 6 November 2018

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
Data must have a Student ID column prior to processing.

### Required Files

- Emails File
- Student Data File
- Student Data Headings File

### Notes

- The Student Data File will be structured according to the needs of the data that
requires emails added to it.
- Student Data Headings File must contain the headings specific to the provided
Student Data.

## Add Names (double)

Adds student names to a set of data. First Name field is one column and Last Name field
is a second column.
Data must have a Student ID column prior to processing.

### Required Files

- Names File (double)
- Student Data File
- Student Data Headings File

### Notes

- The Student Data File will be structured according to the needs of the data that
requires names added to it.
- Student Data Headings File must contain the headings specific to the provided
Student Data.

## Add Names (single)

Adds student names to a set of data. Name field is one column (First and Last).
Data must have a Student ID column prior to processing.

### Required Files

- Names File (single)
- Student Data File
- Student Data Headings File

### Notes

- The Student Data File will be structured according to the needs of the data that
requires names added to it.
- Student Data Headings File must contain the headings specific to the provided
Student Data.

## Add Student ID

Adds Student IDs to a set of data. The data must include an Enrolment ID.

### Required Files

- IDs file
- Student Data File
- Student Headings File

### Notes

- The Student Data File will be structured according to the needs of the data that
requires Student IDs added to it.
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

## IDs file

### File Name

ids.csv

### Contents

Enrolment ID and Student ID for each student.

### Structure

CSV file with EnrolmentID and StudentID columns.

### Source

\<create_query> from the Student Database. 

## Names File (double)

### File Name

names_double.csv

### Contents

Student ID, First Name, Last Name for each student.

### Structure

CSV file with Student ID, First Name and Last Name columns.

### Source

Student table of the Student Database.

## Names File (single)

### File Name

names_single.csv

### Contents

Student ID and First + Last Name for each student.

### Structure

CSV file with Student ID and First + Last Name columns.

### Source

Create from Students table of Student Database (combining the two name columns into
one.

## Student Data File

### File Name

\<xxx>.csv where \<xxx> is the name that the user has saved the data file with.

### Contents

Contents will depend on what the user needs updating, but at a minimum must include
the Enrolment ID or Student ID for each student, depending on the function that is
to be performed on the data.

### Structure

CSV file with Student ID or Enrolment ID and any other columns the data contains.

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

- Add functions to menu
- Add functions for new items

## Required development steps

- Add further filtering options

## Future additions

- Add addresses
- Add tutor
- Add date of birth
- Add age
- Add location
- Add filtering of results