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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("Please, Choose a city name (chicago, new york city, washington) :\n ").lower()
    while city not in ["chicago", "new york city", "washington"]:
        print("Please enter a valid city")
        city = input("Please choose between chicago, new york city or washington\n").lower()


    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['january', 'february', 'march','april', 'may','june', 'all']
    while True:
        month = input("Please, Choose month :(all, january, february, march , april, may, june)\n ").lower()
        if month in months:
            break
        else:
            print("Sorry, it's not valid")


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday','all']
    while True:
        day = input("Please, Choose day :(sunday, monday, tuesday, wednesday, thursday, friday, saturday)\n ").lower()
        if day in days:
            break
        else:
            print("Sorry, it's not valid")


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
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['start hour'] = df['Start Time'].dt.hour

    if month != 'all':
        months = ['january', 'february', 'march','april', 'may','june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]
    print("The most common month:\n", most_common_month)


    # TO DO: display the most common day of week
    most_common_day = df['day_of_week'].mode()[0]
    print("The most common month:\n", most_common_day)


    # TO DO: display the most common start hour
    most_common_hour = df['start hour'].mode()[0]
    print("The most common start hour:\n", most_common_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start = df['Start Station'].mode()[0]
    print("The most common start station:\n", most_common_start)


    # TO DO: display most commonly used end station
    most_common_end = df['End Station'].mode()[0]
    print("The most common end station:\n", most_common_end)


    # TO DO: display most frequent combination of start station and end station trip
    df['way'] = df['Start Station']+","+df["End Station"]
    print("The most frequent combination of start and end station:\n {}".format(df['way'].mode()[0]))




    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = (df['Trip Duration'].sum()).round()
    print("Total travel time:\n", total_travel_time)


    # TO DO: display mean travel time
    mean_travel_time = (df['Trip Duration'].mean()).round()
    print("Average travel time:\n", mean_travel_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts().to_frame()
    print("User Type: ", user_types)


    # TO DO: Display counts of gender
    if city !="washington":
        gender_type = df['Gender'].value_counts().to_frame()
        print("Gender: ", gender_type)


    # TO DO: Display earliest, most recent, and most common year of birth
        earliest_year = int(df['Birth Year'].min())
        print('The earliest year of birth: ', earliest_year)
        most_recent_year = int(df['Birth Year'].max())
        print('The most recent year of birth: ', most_recent_year)
        most_common_year = int(df['Birth Year'].mode()[0])
        print('The most common year of birth: ' , most_common_year)
    else:
        print('No data for this city')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def display_data(df):
    """Display the data due filteration.
    5 raw will added in each press"""
    print('press enter to see raw data,press no to skip')
    x = 0
    while (input() != 'no'):
        x = x+5
        print(df.head(x))

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
