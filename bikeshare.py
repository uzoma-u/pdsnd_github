import time
import pandas as pd
import numpy as np


CITY_DATA = {'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv'}

CITIES = ["chicago", "new york city", "washington"]

MONTHS = ["january", "february", "march", "april", "may", "june", "all"]

DAYS = ["all", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]


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
        city = input("\nChoose a city to explore (Washington, Chicago, New York City):\n").lower()
        if city not in CITIES:
            print("Sorry, that was an invalid input.")
            continue
        else:
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("\nFilter by month (January, February, March, April, May, June or All to apply no month filter):\n").lower()
        if month in MONTHS:
            break
        else:
            print("\nNo information for the month provided")
            continue

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("\nFilter by day {Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or All to apply no day filter}:\n").lower()
        if day in DAYS:
            break
        else:
            print("\nPlease provide an input.")
            continue


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

    #load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extracting month, week day, hour from Start Time
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.day
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != "all":
        month = MONTHS.index(month) + 1
        df = df[ df["month"] == month]

    # filter by day if applicable
    if day != "all":
        day = DAYS.index(day) + 1
        df = df[ df["day"] == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()


    # TO DO: display the most common month
    most_common_month = df["month"].mode()[0]
    print("\nThe most common month: ", most_common_month)

    # TO DO: display the most common day of week
    most_common_day = df["day"].mode()[0]
    print("\nThe most common day of week: ", most_common_day)

    # TO DO: display the most common start hour
    most_common_starthour = df["hour"].value_counts().idxmax
    print("\nThe most common start hour: ", most_common_starthour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_startstation = df["Start Station"].value_counts().idxmax
    print("\nThe most commonly used start station: ", most_common_startstation)

    # TO DO: display most commonly used end station
    most_common_endstation = df["End Station"].value_counts().idxmax
    print("\nThe most commonly used end station: ", most_common_endstation)

    # TO DO: display most frequent combination of start station and end station trip
    most_frequent_start_end_station_trip = df[["Start Station", "End Station"]].mode().loc[0]
    print("\nThe most frequent combination of start and end station trip: ", most_frequent_start_end_station_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df["Trip Duration"].sum()
    print("\nThe total travel time: ", total_travel_time)

    # TO DO: display mean travel time
    average_travel_time = df["Trip Duration"].mean()
    print("\nThe average travel time: ", average_travel_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types_counts = df["User Type"].value_counts()
    print("\nThe value count for each user type: ", user_types_counts)


    if ("Gender", "Birth Year") in df.columns:
        # TO DO: Display counts of gender
        gender_counts = df["Gender"].value_counts()
        for index, gender_count in enumerate(gender_counts):
            print("{}: {}".format(gender_counts.index[index], gender_counts)

        # Display Trip Duration per gender
        gender_trips = df.groupby(["Gender"])["Trip Duration"].sum()
        print("\nThe duration of trips made per gender: ", gender_trips)

        # TO DO: Display earliest, most recent, and most common year of birth
        earliest_year_birth = df["Birth Year"].min()
        print("\nThe earliest birth year: ", earliest_year_birth)

        mostrecent_year_birth = df["Birth Year"].max()
        print("\nThe most recent birth year: ", mostrecent_year_birth)

        most_common_year_birth = df["Birth Year"].mode()
        print("\nThe most common birth year: ", earliest_year_birth)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def data_display(df):
    """Displays raw data on bikeshare."""

    print('\nDisplaying raw data...\n')
    start_time = time.time()

    missing_values = df.isnull().sum().sum()
    print("The number of missing valuse: ", missing_values)

    # Display raw data upon user request
    start_row = 0
    user_request = input("Would you like to view rows of raw data? Yes/No: ")
    while user_request.lower() == "yes":
        df_five = df.iloc[start_row : start_row+5]
        print(df_five)

        start_row += 5

        user_request_again = input("Would like to view more rows of raw data? Yes/No: ")
        if user_request_again.lower() != "yes":
            break

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        data_display(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
