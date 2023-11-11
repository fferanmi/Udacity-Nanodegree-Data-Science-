import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    cities = ['chicago', 'new york city', 'washington']
    months = ['all', 'january', 'february', 'march', 'april', 'may', 'june', 'july', 'august',
                         'september', 'october', 'november', 'december']
    days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    
    # get user input for city
    while True:
        city = input("Enter name of city to analyze (chicago, new york city, washington): ").lower()
        if city in cities:
            break
        else:
            print("invalid city name!. Please enter a valid city name.")
            
    # get user input for month 
    while True:
        month = input("Enter name of month to filter by or 'all': ").lower()
        if month in months:
            break
        else:
            print("Invalid month name!. Please enter a valid month name or 'all'.")
            
    # get user input for day 
    while True:
        day = input("Enter name of day of the week to filter by or 'all': ").lower()
        if day in days:
            break
        else:
            print("Invalid day name!. Please enter a valid name of a day of the week or 'all'.")    
            
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    # Load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # Convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month_name().str.lower()
    df['day_of_week'] = df['Start Time'].dt.day_name().str.lower()

    # Filter by month if applicable
    if month != 'all':
        df = df[df['month'] == month]

    # Filter by day of week if applicable
    if day != 'all':
        df = df[df['day_of_week'] == day]
        
        
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    try:
        most_common_month = df['month'].mode()[0]
        print('Most Common Month:', most_common_month.title())
    except IndexError:
        print('No data available for the selected month.')

    # TO DO: display the most common day of week
    try:
        most_common_day = df['day_of_week'].mode()[0]
        print('Most Common Day of Week:', most_common_day.title())
    except IndexError:
        print('No data available for the selected day.')

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    try:
        most_common_hour = df['hour'].mode()[0]
        print('Most Common Start Hour:', most_common_hour)
    except IndexError:
        print('No data available for the selected hour.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    try:
        most_common_start_station = df['Start Station'].mode()[0]
        print('Most Commonly Used Start Station:', most_common_start_station)
    except IndexError:
        print('No data available for the most commonly used start station.')

    # TO DO: display most commonly used end station
    try:
        most_common_end_station = df['End Station'].mode()[0]
        print('Most Commonly Used End Station:', most_common_end_station)
    except IndexError:
        print('No data available for the most commonly used end station.')

    # TO DO: display most frequent combination of start station and end station trip
    df['Start_End_Station'] = df['Start Station'] + ' to ' + df['End Station']
    try:
        most_common_start_end_station = df['Start_End_Station'].mode()[0]
        print('Most Frequent Combination of Start Station and End Station Trip:', most_common_start_end_station)
    except IndexError:
        print('No data available for the most frequent combination of start and end station.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    try:
        total_travel_time = df['Trip Duration'].sum()
        print('Total Travel Time:', total_travel_time, 'seconds')
    except IndexError:
        print('No data available for total travel time.')

    # TO DO: display mean travel time
    try:
        mean_travel_time = df['Trip Duration'].mean()
        print('Mean Travel Time:', mean_travel_time, 'seconds')
    except IndexError:
        print('No data available for mean travel time.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """ 
    Displays statistics on bikeshare users.
    Args: 
        df(pd.Dataframe): pandas dataframe containing bikeshare data.

    Returns: 
        None

    """
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    try:
        user_types = df['User Type'].value_counts()
        print('Counts of User Types:')
        print(user_types)
    except KeyError:
        print('No data available for user types.')

    # Display counts of gender
    if 'Gender' in df.columns:
        try:
            gender_counts = df['Gender'].value_counts()
            print('\nCounts of Gender:')
            print(gender_counts)
        except IndexError:
            print('No data available for gender counts.')
    else:
        print('\nGender data not available for this city.')

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        try:
            earliest_year = df['Birth Year'].min()
            most_recent_year = df['Birth Year'].max()
            most_common_year = df['Birth Year'].mode()[0]
            print('\nEarliest Year of Birth:', int(earliest_year))
            print('Most Recent Year of Birth:', int(most_recent_year))
            print('Most Common Year of Birth:', int(most_common_year))
        except IndexError:
            print('No data available for birth year statistics.')
    else:
        print('\nBirth year data not available for this city.')

    print(f"\nThis took {time.time() - start_time:.2f} seconds.")
    print('-'*40)
    
def display_data(df):
    """
    Displays five rows of data upon user request and 
    if the user wants to view the next five rows of trip data.
    
    """
    
    view_data = input("\nWould you like to view the first 5 rows of individual trip data? Enter yes or no?\n").lower()
    start_loc = 0 
    
    while view_data == 'yes':
        print(df.iloc[start_loc:start_loc+5])
        start_loc += 5
        view_data = input("\nDo you wish to view the next 5 rows of data? Enter yes or no?\n").lower()


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() !='yes':
            break


if __name__ == "__main__":
	main()