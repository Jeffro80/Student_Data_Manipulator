# Student Data Manipulator
# Version 0.05 25 September 2018
# Created by Jeff Mitchell
# Takes in data files and adds details such as student email addresses

# Current work
# - add filtering of email results


# Still to do:
# - Add futher filtering options

# Future additions:
# - 


# To Fix:
# - 

# Known issues:
# - 

import custtools.admintools as ad
import custtools.filetools as ft
import numpy as np
import pandas as pd
import re
import sys


def add_email():
    """Add email address to student data.
    
    Loads student data and email data. Merges the two data sets on the
    Student ID column. Keeps all students in the student data and returns ''
    if no email is found for the Student ID.
    """
    print('\nAdding Emails to Student Data.')
    # Confirm the required files are in place
    required_files = ['Student Data File', 'Student Data Headings File',
                      'Emails File']
    ad.confirm_files('Add Emails Data', required_files)
    # Load student data file
    student_data = ft.get_csv_fname_load('Student Data')
    # Load student headings file
    student_data_headings = ft.get_headings_fname_load(
            'Student Data Headings File')
    # Load emails file
    email_data = ft.get_csv_fname_load('Email Data')
    # Create dataframe for student data
    student_data_df = pd.DataFrame(data = student_data,
                                   columns = student_data_headings)
    # Create dataframe for email data
    email_cols = ['StudentID', 'Email']
    email_data_df = pd.DataFrame(data = email_data, columns = email_cols)
    # Merge tables on StudentID
    updated_data_df = pd.merge(student_data_df, email_data_df, on='StudentID',
                               how='left')
    # Check if wish to filter results based on course
    message = 'Do you wish to filter the results?'
    to_filter = ad.check_action(message)
    # Filter results based on course if necessary
    if to_filter:
        updated_data_df = filter_results(updated_data_df)
    # Save file to disk
    file_name = 'Student_Data_Emails_{}.csv'.format(ft.generate_time_string())
    updated_data_df.to_csv(file_name, index=False)
    print('\nData has been saved to {}'.format(file_name))


def apply_course_filter(course, target, wild_cards=True):
    """Convert to NaN courses not in the target filter.
    
    Args:
        course (str): Student course.
        target (str): Course code or base code to be searched for.
        wild_cards (bool): If True, .+ used either side of course code. Used if
        looking at study type etc. If False, .+ not used, e.g. for searching
        for a specific course.
    
    Returns:
       course (str) Original course or NaN if outside of filter target.
    """
    if wild_cards:
        wild = '.+'
    else:
        wild = ''
    if course in (None, ''):
        return np.nan
    elif re.search('{}{}{}'.format(wild, target, wild), course):
        return course
    else:
        return np.nan


def filter_course(student_data, filter_op):
    """Filter student data based on course.
    
    Args:
        student_data (DataFrame): Student data to be filtered.
        filter_op (str): Course to filter students on.
        
    Returns:
        updated_data_df (DataFrame): Filtered student data.
    """
    # Make copy of dataframes in case need to revert
    updated_data_df = student_data.copy()
    if filter_op == 'Online students':
        # Convert non-online courses to NaN
        updated_data_df['Course'] = updated_data_df['Course'].apply(
                apply_course_filter, args=('ON',))
        # Drop courses that are NaN
        updated_data_df.dropna(subset=['Course'], inplace=True)
    elif filter_op == 'Part-time students':
         # Convert non-part-time courses to NaN
        updated_data_df['Course'] = updated_data_df['Course'].apply(
                apply_course_filter, args=('PT',))
        # Drop courses that are NaN
        updated_data_df.dropna(subset=['Course'], inplace=True)
    return updated_data_df


def filter_options_course_message():
    """Print filtering options based on course."""
    print('\nOptions for filtering (Course):')
    print('\n1. Online students')
    print('2. Part-time students')
    print('3. CPD students')
    print('4. Specific course students')
    print('5. No further filter')


def filter_results(data_df):
    """Filters results based on course.
    
    Args:
        data_df (DataFrame): Student data prior to filtering.
        
    Returns:
        updated_data_df (DataFrame): DataFrame with filtered results.
    """
    # Get course to filter on
    filter_op = get_course_filter()
    if not filter_op:
        # Return unfiltered results
        print('\nThe results have not been filtered')
        return data_df
    # Filter on Online
    if filter_op == 'Online students':
        updated_data_df = filter_course(data_df, filter_op)
    # Filter on Part-time
    elif filter_op == 'Part-time students':
        updated_data_df = filter_course(data_df, filter_op)
    elif filter_op == 'CPD students':
        print('\nThat option is not yet available.')
        return data_df
    elif filter_op == 'Specific course students':
        print('\nThat option is not yet available.')
    else:
        # Return unfiltered results
        print('\nThe results have not been filtered')
        return data_df
    return updated_data_df
    

def get_course_filter():
    """Return course filter selection.
    
    Returns:
        selection (str): Course filter selection.
    """
    # List of allowed selections
    allowed = ['1', '2', '3', '4', '5']
    filter_options_course_message()
    while True:
        selection = input('\nPlease enter your selection (number) for the '
                          'course filter you would like to apply. Enter {} if '
                          'you do not wish to add another filter: '.format(
                                  len(allowed)))
        if selection in allowed:
            if selection == '1':
                return 'Online students'
            elif selection == '2':
                return 'Part-time students'
            elif selection == '3':
                return 'CPD students'
            elif selection == '4':
                return 'Specific course students'
            elif selection == '5':
                return None  
        else:
            print('\nThat is not a valid option. Please select from the '
                  'available options.')


def help_menu():
    """Display the requested help information."""
    repeat = True
    low = 1
    high = 7
    while repeat:
        try_again = False
        help_menu_message()
        try:
            action = int(input('\nPlease enter the number for your '
                               'selection --> '))
        except ValueError:
            print('Please enter a number between {} and {}.'.format(low, high))
            try_again = True
        else:
            if action < low or action > high:
                print('\nPlease select from the available options ({} - {})'
                      .format(low, high))
                try_again = True
            elif action == low:
                continue
            elif action == 2:
                continue
            elif action == 3:
                continue
            elif action == 4:
                continue
            elif action == 5:
                continue
            elif action == 6:
                continue
            elif action == high:
                repeat = False
        if not try_again:
            repeat = ad.check_repeat_help()


def help_menu_message():
    """Display the help menu options."""
    print('\nPlease enter the number for the item you would like help on:\n')
    print('1: TBC')
    print('2: TBC')
    print('3: TBC')
    print('4: TBC')
    print('5: TBC')
    print('6: TBC')
    print('7: TBC')


def main():
    repeat = True
    low = 1
    high = 9
    while repeat:
        try_again = False
        main_message()
        try:
            action = int(input('\nPlease enter the number for your '
                               'selection --> '))
        except ValueError:
            print('Please enter a number between {} and {}.'.format(low, high))
            try_again = True
        else:
            if action < low or action > high:
                print('\nPlease select from the available options ({} - {})'
                      .format(low, high))
                try_again = True
            elif action == low:
                help_menu()
            elif action == 2:
                add_email()
            elif action == 3:
                continue
            elif action == 4:
                continue
            elif action == 5:
                continue
            elif action == 6:
                continue
            elif action == 7:
                continue
            elif action == 8:
                continue
            elif action == high:
                print('\nIf you have generated any files, please find them '
                      'saved to disk. Goodbye.')
                sys.exit()
        if not try_again:
            repeat = ad.check_repeat()
    print('\nPlease find your files saved to disk. Goodbye.')
    

def main_message():
    """Print the menu of options."""
    print('\n\n*************==========================*****************')
    print('\nStudent Data Manipulator version 0.05')
    print('Created by Jeff Mitchell, 2018')
    print('\nOptions:')
    print('\n1. Help Menu')
    print('2. Add Emails')
    print('3. TBC')
    print('4. TBC')
    print('5. TBC')
    print('6. TBC')
    print('7. TBC')
    print('8. TBC')
    print('9. Exit')


if __name__ == '__main__':
    main()