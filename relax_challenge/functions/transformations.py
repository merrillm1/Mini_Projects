# import necessary modules
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def check_for_user_activity_over_time_period(df, user_col, time_col, class_col, time_period = 7):
    
    '''
         
    The purpose of this function is to check the activity of a user over chunks of time in an entire 
    time period. The code is set up to check if a user was active for at least three seperate days
    in a 7 day period, over an entire time frame. It can be changed for less or more activity.
        
    ----------------------------------------------------------------------------------------------
    The use of this function us for classification purposes. The variables are defined below:
        
        df - the dataframe that holds the user_id column and the time_stamp column for each 
                 activity
        
        user_col - the user_id, as labaled in the df
        
        time_col - this should be a time stamp for each documented activity of the user
        
        class_col - this should be what the desired classification is, for example "is_retained"
        
        time_period - this is the time period that the function should check over, over the df
        
    '''
    
    # loop through each user
    user_ids = list(df[user_col].unique())
    
    # Set time_stamp as index for engagement
    df = df.set_index(time_col).sort_index()

    # This just squeezes out the day from each timestamp for grouping in the next line
    dates = pd.Series(df.index.get_level_values(time_col).date, name=time_col, index=df.index)

    # Group by the dates extracted above and by user_id
    df_temp = df.groupby([dates, user_col]).sum().sort_index()
    
    # Reset the index to re-create time_stamp column
    daily_visitors = df_temp.reset_index()
    
    # create dataframe to catch results
    adopted_users = pd.DataFrame(columns = [user_col, class_col])

    for user in user_ids:
        visits = daily_visitors[daily_visitors.user_id == user]  # filter for each user
        for i in range(len(visits)):       

            if i+3 <= len(visits): # if the user has logged in at least 3 days, check to see if it's within a week

                if i+3 == len(visits): # if the length is equal to 3 days, finalize loop here

                    if ((visits[time_col].values[i+2] - visits[time_col].values[i]) <= timedelta(days=time_period)):

                        adopted_users = adopted_users.append({user_col: user, class_col: 1}, ignore_index=True)
                        break

                    else:
                        adopted_users = adopted_users.append({user_col: user, class_col: 0}, ignore_index=True)
                        break

                elif i+3 < len(visits): # if the length is more than 3 days, loop through unless labaled adopted

                    if ((visits[time_col].values[i+2] - visits[time_col].values[i]) <= timedelta(days=time_period)):
                        adopted_users = adopted_users.append({user_col: user, class_col: 1}, ignore_index=True)
                        break

                    else:
                        continue

            elif i+3 > len(visits): # if the number of visits is less than three days, mark as not adopted

                adopted_users = adopted_users.append({user_col: user, class_col: 0}, ignore_index=True)
                break
    
    return adopted_users