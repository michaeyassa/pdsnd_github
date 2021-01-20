import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }
CITIES = ['chicago', 'new york', 'washington']
MONTHS = ['january', 'february', 'march', 'april', 'may', 'june','all']
DAYS = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday' ,'all']
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
    while True:
        city = input('Which city do you want to explore Chicago, new york or Washington? \n> ').lower()
        if city not in CITIES:
            print("\nInvalid Answer\n")
            continue
        else:
            break
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('All right! now it\'s time to provide us a month name Which month? January, February, March, April, May or June, All? \n> ').lower()
        if month not in MONTHS:
            print("\nInvalid Answer\n")
            continue
        else:
            break
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('One last thing. Could you type one of the week day you want to analyze? \n You can type \'all\' again to apply no day filter. \n(e.g. all, monday, sunday) \n> ').lower()
        if day not in DAYS:
            print("\nInvalid Answer\n")
            continue
        else:
            break
    print('-'*40)
    return city, month, day

def load_data (city, month, day):
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

    df['day_of_the_week'] = df['Start Time'].dt.weekday_name
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
    if day != 'all':
        df = df[df['day_of_the_week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month

    most_common_month = df['month'].mode()[0]

    print('The month with the most travelers is {}.'.format(most_common_month))


    # TO DO: display the most common day of week
    start_time = time.time()
    df['Start Time'] = pd.to_datetime(df['Start Time'])


    df['day_of_the_week'] = df['Start Time'].dt.weekday_name

    most_common_day = df['day_of_the_week'].mode()[0]

    print('The day of the week with the most travelers is {}.'.format(most_common_day))


    # TO DO: display the most common start hour

    df['hour'] = df['Start Time'].dt.hour

    most_common_hour = df['hour'].mode()[0]

    print('The hour of the day with the most travelers is {}.'.format(most_common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print('The most common Start Station is : ',most_common_start_station)

    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print('The most common End Station is : ',most_common_end_station)


    # TO DO: display most frequent combination of start station and end station trip
    most_frequent_combination = df.groupby(['Start Station','End Station']).size().nlargest(1)
    print('the most frequent combination of start station and end station trip:', most_frequent_combination)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_trip_duration = df['Trip Duration'].sum()
    print('The total trip duration is {}'.format(total_trip_duration))


    # TO DO: display mean travel time
    average_trip_duration = df['Trip Duration'].mean()
    print('The average trip duration is {}'.format(average_trip_duration))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    if 'User Type' in df.columns:
        user_type = df['User Type'].value_counts()
        print('The full amount of each user type is {}.'.format(user_type))

    # TO DO: Display counts of gender
    try:
        gender = df['Gender'].value_counts()
        print('The total in each gender is {}.'.format(gender))
    except:
        print('There is no gender information for Washington.\n')

    # TO DO: Display earliest, most recent, and most common year of birth


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

# TO DO: Display raw data
def display_data(df):
    i=0
    user_question=input('Would you like to see the raw data? \ntpye yes or no ,  > ').lower()
    while user_question in ['yes','y','yep','yea'] and i+5 < df.shape[0]:
        print(df.iloc[i:i+5])
        i += 5
        user_question = input('Would you like to see more data? Please enter yes or no:').lower()


def main():

   while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        display_data(df)


        q1 = input ("would you like to see data statistics? type 'yes' or 'no' : ")
        if q1 == 'yes':
            print (time_stats(df))
        else:
            break

        q2 = input ("would you like to see more statistics? type 'yes' or 'no' : ")
        if q2 == 'yes':
            print (station_stats(df))
        else:
            break

        q3 = input ("would you like to see more statistics? type 'yes' or 'no' : ")
        if q3 == 'yes':
            print (trip_duration_stats(df))
        else:
            break

        q4 = input ("would you like to see more statistics? type 'yes' or 'no' : ", )
        if q4 == 'yes':
            print (user_stats(df))
        else:
            break

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break



if __name__ == "__main__":
	main()
