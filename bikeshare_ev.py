import time
import pandas as pd
import numpy as np
import datetime

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
     
    """
    Asks user to specify a city, month, and day to analyze.
    Args:
        None
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
       
    while True:
      city = input('\nPlease choose the city: Washington, New York or Chicago. If you do not want to proceed please write \'exit\'.\n')
      if city.lower() not in ('chicago', 'new york', 'washington', 'exit'):
        print('Oops! Looks like you choose wrong city! Please try again.')
      elif city.lower() == 'exit':
        return None
      else:
        break
        
      
         
             
        
    while True:
      month = input('\nPlease choose the month: january, february, march, april or june.\n\
                     If you do not want to proceed please write \'exit\'.\n')
      if month.lower() not in ('january', 'february', 'march', 'april', 'june'):
        print('Oops! Looks like you choose wrong month! Please try again.')
      elif month.lower() == 'exit':
        return None
      else:
        break
                        
                
    while True:
      day = input('\nPlease choose day of the week: monday, tuesday, wednesday, thursday, friday, saturday or sunday.\n')
      if day.lower() not in ('monday', 'tuesday','wednesday','thursday', 'friday', 'saturday', 'sunday'):
        print('Oops! Looks like you choose wrong day! Please try again.')
      elif day.lower() == 'exit':
        return None
      else:
        break
                                  
    
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

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df

      

def time_stats(df):
    """
    Displays statistics on the most frequent times of travel.
    Args:
         relavant dataframe
    Returns:
         relevant time statistics
    """

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    #display the most common month
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract the month from the Start Time column to create a month column. 
    df['month'] = df['Start Time'].dt.month
    # find the most popular month
    popular_month = df['month'].mode()[0]
    print('\nMost Popular Month:', popular_month)
    
  
    # display the most common day of week
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract the day from the Start Time column to create a day column. 
    df['day'] = df['Start Time'].dt.day
    # find the most popular month
    popular_day = df['day'].mode()[0]
    print('\nMost Popular Day:', popular_day)
    
    # display the most common start hour
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract the hour from the Start Time column to create a hour column. 
    df['hour'] = df['Start Time'].dt.hour
    # find the most popular month
    popular_hour = df['hour'].mode()[0]
    print('\nMost Popular Hour:', popular_hour)
       
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """
    Displays statistics on the most popular stations and trip.
    Args: 
         relevant dataframe
    Returns:
         relevant statistics about most popular stations and trips
    """

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    # find the most popular start station
    popular_start_station = df['Start Station'].mode()[0]
    print('\nMost Popular Start Station:', popular_start_station)
    
    # display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('\nMost Popular End Station:', popular_end_station)

    # display most frequent combination of start station and end station trip
    popular_stations = df[['End Station', 'Start Station']]
    pop_stat = popular_stations.mode()
   
    print('\nMost frequent combination of Stations:', pop_stat)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """
    Displays statistics on the total and average trip duration.
    Args:
         relevant dataframe
    Returns:
         statistics about trip duration (total and anverage)
    """

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel = df['Trip Duration'].sum()
    print('\nTotal travel time was:', total_travel)

    # display mean travel time
    avg_travel = df['Trip Duration'].mean()
    print('\nTotal travel time was:', avg_travel)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """
    Displays statistics on bikeshare users.
    Args:
        rlevant dataframe
    Returns:
        statistics on bikeshare users
    """
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # display counts of user types
    user_type = df['User Type'].value_counts()
       
     
    print('\nDifferent types of users are:', user_type)

    # display counts of gender
    
    def genderdef():
      """
      Specifying exceptions in the code in order to handle ValueErrors.
      Args:
          none
      Returns:
          exception in the case there is ValueError in the code
      """
      try:
        gender_type = gender['Gender'].value_counts()
        
      except ValueError:
        print('There is no data about gender in the Washington data.')
      finally:
        print('\nGender of the user:', gender_type)
    return 

    # display earliest, most recent, and most common year of birth
    earliest_birth = df['Birth Year'].max()
    print('\nThe oldest users were born in:', earliest_birth)
    
    latest_birth = df['Birth Year'].min()
    print('\nThe youngest users were born in:', latest_birth)
    
    common_birth = df['Birth Year'].mode()
    print('\nThe most common year of birth of users was:', latest_birth)
 
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def rawdata(df):
  """
  Asking user whether he/she wants to see some raw data.
  Args:
      relevant dataframe
  Returns:
      sample of raw data on demand
  """
  question = input('\nWould you like to see raw data for the chosen city? Then print \'yes\'.\n')
  while True:
    if question != 'yes':
      break
    else:
      return df.sample(20)
  
   
    

def main():
  
  """ Promps the code to execute the procedures calculating various statistcs.
  Args:
      none
  Returns:
      procedures calculating various statistics with the datasets
  """
    
    
  while True:
    city, month, day = get_filters()
    df = load_data(city, month, day)
    
    time_stats(df)
    station_stats(df)
    trip_duration_stats(df)
    user_stats(df)
        
    print(rawdata(df))

    restart = input('\nWould you like to restart? Enter yes or no.\n')
    if restart.lower() != 'yes':
      break
         


if __name__ == "__main__":
	main()
