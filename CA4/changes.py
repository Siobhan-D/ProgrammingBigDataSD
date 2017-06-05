# Siobhan Dunphy 10353786
# Assignment 4 is based on transforming a large dataset in text format - over 5000 lines of text.
# You will need to scrub (clean) the data and place it into the relevant holder/container objects.
# Once in these objects you will see that there are 422 different sets of commit objects.
# So your task will be  to analyse these 422 objects that are in a list and come up with 3 interesting statistical pieces of information for this dataset with supporting evidence of "interestingness'
# You code for calculating the analysis should be documented and tested.
# Tests should be in a separate file runnable from the command line.
# Your statistical analytics conclusions should be in a word document explaining in approximately 500 words the information that you have gleamed from the dataset.
# You will be required to submit your code via github along with all documentation and tests.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
import datetime as dt
import calendar

# library('ggplot2') # visualization
def prep_file(my_file):
    # Use strip to strip out spaces.
    data = [line.strip() for line in open(my_file, 'r')]
    return data

# Search the document and break up into objects based on sep
# Create a class to store the elements of each object
class Commit(object):
    def __init__(self, revision=None, author=None, date_time=None, comment_line_length=None, 
            comment=None):
        self.revision = revision
        self.author = author
        self.date_time = date_time
        self.comment_line_length = comment_line_length
        self.changes = comment

    def to_dict(self):
        return {'author': self.author,
                'date': self.date,
                'time': self.time,
                'changes': self.changes
                }
    
    def get_date_time(self):
        details = self.date_time.split(' ')
        self.date = details[0] 
        self.time = details[1]
        # Extract hour details from time and convert to int as this will be used later
        self.time = self.time[0:2]
        self.time = int(self.time)
        
    # Function to convert changes to string type
    def convert_comments_to_string(self):
        self.changes =  str(self.changes).strip('[]')
    
# Function to extract data from log file containing records of commits by different authors
def get_commits(data):
    index = 0
    current_commit = None
    commits = []
    # Create string sep that consists of 72 hyphens
    sep = 72*'-'
    while True:
        try:
            details = data[index+1].split('|')
            current_commit = Commit()
            current_commit.revision = details[0].strip()
            current_commit.author = details[1].strip()
            current_commit.date_time = details[2].strip()
            current_commit.get_date_time()
            current_commit.comment_line_length = int(details[3].strip().split(' ')[0])
            index = data.index(sep, index+1)
            current_commit.changes = data[index-current_commit.comment_line_length:index]
            current_commit.convert_comments_to_string()
        
            # Skip uninteresting entries
            if current_commit.author == '/OU=Domain Control Validated/CN=svn.company.net':
                continue  
            elif current_commit.author == 'ajon0002':
                continue
            elif current_commit.author == 'murari.krishnan':
                continue
            else:
                # Add the current commit to the list of commit objects.
                commits.append(current_commit)
        except IndexError:
            break
    return commits

# Create functions to analyse and plot the changes data.

# Function to get a list of all authors.
def get_authors(commits=[]):
    authors = []
    for commit in commits:
        author = commit.author
        if author in authors:
            continue
        else:    
            authors.append(author)
    return authors

# Prepare changes_python.log file
changes_file = prep_file('changes_python.log')
# Extract relevant data from changes_file by create a list of commit objects and adding
# them to a list called commits.
commits = get_commits(changes_file)
# Check the list of authors
authors = get_authors(commits)
print(authors)
# Create data frame by converting each object in commit to a dict and adding it.
df = pd.DataFrame(commit.to_dict() for commit in commits)
# Reorder columns in the df
df = df[['author', 'date', 'time', 'changes']]
# Convert data and time to pandas datetime
df['date'] = pd.to_datetime(df['date'], format="%Y-%m-%d")
# df['time'] = pd.to_datetime(df['time'], format="%H:%M:%S")

# Check df was created properly by printing the first 5 columns, checking data types and viewing info
# print(df.head(5))
# print(df.dtypes)

# Count changes per author and plot. 
# Look at time of day and number of commits for each author.
# Plot time series of commits.
#Look at duration of dataframe - what time is included.
# Look at days of the week?
# Try group by month and group by day of the week?
# Could calculate best performer by looking at average monthly output and calculating stats based on this.
# counts = df['author'].value_counts()

# Create additional columns with month
df['month'] = df['date'].apply(lambda x: "%s" %(x.month))
df['month'] = df['month'].apply(lambda x: calendar.month_abbr[int(x)])

# Create additional column with days of the week
df['day'] = df['date'].apply(lambda x: "%s" %(x.dayofweek))
df['day'] = df['day'].apply(lambda x: calendar.day_abbr[int(x)])

# Group and aggregate the data to get some meaningful insights.
# Look at total commits per author
counts = df['author'].value_counts()
# Look at total commits per month
months = df['month'].value_counts()

# Do some exploratory analysis of the data
# Start by looking at monthly patterns
# Calculate average monthly and daily commits per author
monthly_df = pd.DataFrame({'count' : df.groupby(['author', 'month']).size()}).reset_index()
daily_df = pd.DataFrame({'count' : df.groupby(['author', 'day']).size()}).reset_index()

# Calculate monthly average commits and SD per author
author_monthly_avg = monthly_df.groupby(['author']).agg(['mean','std']).reset_index(['author', 'mean'])
# print(author_monthly_avg)

# Convert dataframe to csv to do additional stats if required
author_monthly_avg.to_csv('author_monthly_avg.csv')

# set background style and other parameters for plots
sns.set(style="whitegrid")
sns.set_context("paper", rc={"font.size":20,"axes.titlesize":20,"axes.labelsize":15})

# Create a grouped bar chart of average monthly commits per author
plt.figure()
average_monthly_commits = sns.barplot(x='author', y='count', data=monthly_df, capsize=.2, errwidth = .8, order = authors)
average_monthly_commits.set_ylabel("average commits per month")
average_monthly_commits.set_xlabel("")
average_monthly_commits.figure.savefig("average_monthly.jpg")

# Create a grouped bar chart of average monthly commits per author
plt.figure()
commits_by_author = sns.countplot(x='author', data=df, order = authors)
commits_by_author.set_ylabel("total commits per author")
commits_by_author.set_xlabel("")
commits_by_author.figure.savefig("commits_by_author.jpg")

plt.figure()
commits_by_month = sns.countplot(x='month', data=df)
commits_by_month.figure.savefig("commits_by_month.jpg")

# commits_by_author_by_month = sns.countplot(x='author', hue='month', data=df)
# commits_by_author_by_month = sns.countplot(x='author', hue='month', data=df)
# Create a factorplot of total commits per month for each author
commits_by_author_by_month = sns.factorplot(x='month', 
        y='count', 
        col = 'author', 
        col_wrap=2, 
        data=monthly_df, 
        kind='bar', 
        order=['Jul','Aug','Sep', 'Oct','Nov'], 
        size = 3)
commits_by_author_by_month.set_xlabels('')
commits_by_author_by_month.set_ylabels('count (per month)')
for ax in commits_by_author_by_month.axes:
    plt.setp(ax.get_xticklabels(), visible=True, rotation=45)
plt.subplots_adjust(hspace=1)
commits_by_author_by_month.savefig("commits_by_author_by_month.jpg")

# Next look at daily patterns
# Create a grouped bar chart of average daily commits per author
plt.figure()
average_daily_commits = sns.barplot(x='author', y='count', data=daily_df, capsize=.2, errwidth = .8, order = authors)
average_daily_commits.set_ylabel("average commits per day")
average_daily_commits.set_xlabel("")
average_daily_commits.figure.savefig("average_daily.jpg")

plt.figure()
commits_by_weekday = sns.countplot(x='day', data=df, order = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'],)
commits_by_weekday.figure.savefig("commits_by_weekday.jpg")

# Create a dataframe grouped by author and date
dates_df = pd.DataFrame({'count' : df.groupby(['author','date']).size()}).reset_index()
daily_avg = dates_df.groupby(['author']).agg(['mean','std']).reset_index(['author', 'mean'])

# Add a column for day of the week
dates_df['day']= dates_df['date'].apply(lambda x: "%s" %(x.dayofweek))
dates_df['day'] = dates_df['day'].apply(lambda x: calendar.day_abbr[int(x)])

# Calculate averages based on day of the week
author_weekday_avg = pd.DataFrame(dates_df.groupby(['author','day'])['count'].agg(['mean', 'std'])).reset_index()

# Convert dataframe to csv 
author_weekday_avg.to_csv('author_weekday_avg.csv')

# Plot mean values based on day of the week for each author
avg_commits_by_author_by_weekday = sns.factorplot(x='day', 
        y='mean', 
        col = 'author', 
        col_wrap=2, 
        data=author_weekday_avg, 
        kind='bar', 
        order = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'],
        size = 3)
avg_commits_by_author_by_weekday.set_xlabels('')
avg_commits_by_author_by_weekday.set_ylabels('average (day of week)')
for ax in avg_commits_by_author_by_weekday.axes:
    plt.setp(ax.get_xticklabels(), visible=True, rotation=45)
plt.subplots_adjust(hspace=1)
avg_commits_by_author_by_weekday.savefig("avg_commits_by_author_by_weekday.jpg")

# Get information on time of day
# If time is before midday then change to AM otherwise change to PM
df['time']= df['time'].apply(lambda x:'AM' if x<12 else 'PM')

# How many commits occur in AM versus PM?
time_of_day_counts = df['time'].value_counts()
time_df = pd.DataFrame({'count' : df.groupby(['author','time']).size()}).reset_index()

# Plot mean values based on time of day for each author
avg_commits_by_author_by_time_of_day = sns.factorplot(x='time', 
        y='count', 
        col = 'author', 
        col_wrap=3, 
        data=time_df, 
        kind='bar', 
        order = ['AM', 'PM'],
        size = 3)
avg_commits_by_author_by_time_of_day.set_xlabels('')
avg_commits_by_author_by_time_of_day.set_ylabels('count')
for ax in avg_commits_by_author_by_time_of_day.axes:
    plt.setp(ax.get_xticklabels(), visible=True)
plt.subplots_adjust(hspace=1)
avg_commits_by_author_by_time_of_day.savefig("avg_commits_by_author_by_time_of_day.jpg")
