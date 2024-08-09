import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
MAP_OF_MONTH = {'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6, 'july': 7, 'august': 8, 'september': 9, 'october': 10, 'november': 11, 'december': 12}

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! This application gives information about bikeshare data in US')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True: 
        city = input("Select the city (chicago, new york city, washington): ").lower()  
        if city in CITY_DATA:
            break
        else:
            print("Please enter a correct city name which is in the list")
    # TO DO: get user input for month (all, january, february, ... , june)        
    while True:
        month = input("Select the month (all, january, february, ... , december): ").lower()
        if month in ['all', 'january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']:
            break
        else:
            print("Please enter a correct month")
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday) 
    while True:
        day = input("Select the day of week (all, monday, tuesday, ... sunday): ").lower()
        if day in ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
            break
        else:
            print("Please enter a correct day")
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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    
    if month != 'all':
        # months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
        # month = (months.index(month)) + 1
        # df = df[df['month'] == month]
        df = df[df['month'] == MAP_OF_MONTH[month]]
        
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
            
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]
    print('The most common month:', most_common_month)

    # TO DO: display the most common day of week
    most_common_day = df['day_of_week'].mode()[0]
    print('The most common day:', most_common_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_common_hour = df['hour'].mode()[0]
    print('The most common start hour:', most_common_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print('The most commonly used start sation:', most_common_start_station)

    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print('The most commonly used end sation:', most_common_end_station)


    # TO DO: display most frequent combination of start station and end station trip
    frequent_combination_of_trips = df.groupby(['Start Station', 'End Station']).size().idxmax()
    print('The most frequent combination of start station and end station trip:', frequent_combination_of_trips)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("Total travel time:", total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("Mean travel time:", mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type_count = df['User Type'].value_counts()
    print("User types counts:\n", user_type_count)

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender_count = df['Gender'].value_counts()
        print("Gender counts:\n", gender_count)
    else:
        print("There isn't any gender information for this city")

    # TO DO: Display earliest, most recent, and most common year of birth
    # There isn't data for below for washington
    if 'Birth Year' in df.columns:
        earliest_year_of_birth = int(df['Birth Year'].min())
        print("Earliest year of birth:", earliest_year_of_birth)

        most_recent_year_of_birth = int(df['Birth Year'].max())
        print("Most recent year of birth:", most_recent_year_of_birth)

        most_common_year_of_birth = int(df['Birth Year'].mode()[0])       
        print("Most common year of birth:", most_common_year_of_birth)
    else:
        print("There isn't any year of birth information for this city")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def print_raw_data(df):    
        rows = 0
        while True:
            if rows == 0:
                five_rows_of_data = input("Do you want to see 5 rows of the data? (yes/no) ").lower()
            else:
                five_rows_of_data = input("Do you want to see 5 more rows of the data? (yes/no) ").lower()
        
            if five_rows_of_data == 'yes':
                last_row = rows + 5
                if last_row > len(df):
                    last_row = len(df)
                print(df.iloc[rows:last_row])
                rows = last_row
                if rows >= len(df):
                    print("This was all the data")
                    break
            else:
                break
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        #print(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)        
        print_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
    
