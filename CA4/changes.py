# Assignment 4 is based on transforming a large dataset in text format - over 5000 lines of text.
# You will need to scrub (clean) the data and place it into the relevant holder/container objects.
# Once in these objects you will see that there are 422 different sets of commit objects.
# So your task will be to analyse these 422 objects that are in a list and come up with 3 interesting statistical pieces of information for this dataset with supporting evidence of "interestingness'
# You code for calculating the analysis should be documented and tested.
# Tests should be in a separate file runnable from the command line.
# Your statistical analytics conclusions should be in a word document explaining in approximately 500 words the information that you have gleamed from the dataset.
# You will be required to submit your code via github along with all documentation and tests.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
import datetime as dt
import calendar
from os import path

sns.set(style="whitegrid")

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
                'date_time': self.date_time,
                'changes': self.changes
                }
    
    def get_date_time(self):
        details = self.date_time.split(' ')
        self.date_time = details[0] + ' ' + details[1]
    
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

# Function to count the number of revisions per author.
def count_revisions():
    pass

# Prepare changes_python.log file
changes_file = prep_file('changes_python.log')
# Extract relevant data from changes_file by create a list of commit objects and adding
# them to a list called commits.
commits = get_commits(changes_file)
# Check the list of authors
print(get_authors(commits))
# Create data frame by converting each object in commit to a dict and adding it.
df = pd.DataFrame(commit.to_dict() for commit in commits)
# Reorder columns in the df
df = df[['author', 'date_time', 'changes']]
# Convert data and time to pandas datetime
df['date_time'] = pd.to_datetime(df['date_time'], format="%Y-%m-%d %H:%M:%S")

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
df['month'] = df['date_time'].apply(lambda x: "%s" %(x.month))
df['month'] = df['month'].apply(lambda x: calendar.month_abbr[int(x)])

# print df.head(5)

# Group and aggregate the data to get some meaningful insights.


# Look at total commits per author
counts = df['author'].value_counts()
# Look at total commits per month
months = df['month'].value_counts()

# Make some exploratory plots
# generate figure with axes

# Calculate average monthly commits per author
monthly_df = pd.DataFrame({'count' : df.groupby(['author', 'month']).size()}).reset_index()
print(monthly_df)
author_monthly_avg = monthly_df.groupby(['author']).mean().reset_index(['author', 'mean'])
print(author_monthly_avg)

# Create a grouped bar chart of average monthly commits per author
plt.figure()
average_monthly = sns.barplot(x='author', y='count', data=author_monthly_avg)
average_monthly.figure.savefig("average_monthly.jpg")


plt.figure()
commits_by_author = sns.countplot(x='author', data=df)
commits_by_author.figure.savefig("commits_by_author.jpg")

plt.figure()
commits_by_month = sns.countplot(x='month', data=df)
commits_by_month.figure.savefig("commits_by_month.jpg")

plt.figure()
commits_by_author_by_month = sns.countplot(x='author', hue='month', data=df)
commits_by_author_by_month.figure.savefig("commits_by_author_by_month.jpg")


# print(df.groupby(df['author'].count()))
# print(df.groupby(df['date_time', 'author'].dt.month).size())
# by_date = pd.DataFrame({'count' : df.groupby( [ "author", "date"] ).size()}).reset_index()
# print by_date
# 
# for i, group in by_date.groupby('author'):
#     plt.figure()
#     group.plot(x='author', y='date')
# if df['date_time'].dt.time() < dt.time(12):
#     df['time of day'] = 'morning'
# else:
#     df['time of day'] = 'afternoon'
# df['Hour'] = df['Timestamp'].apply(lambda x: "%d/%d" %(x.month, x.year))