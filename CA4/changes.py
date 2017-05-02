# Assignment 4 is based on transforming a large dataset in text format - over 5000 lines of text.
# You will need to scrub (clean) the data and place it into the relevant holder/container objects.
# Once in these objects you will see that there are 422 different sets of commit objects.
# So your task will be to analyse these 422 objects that are in a list and come up with 3 interesting statistical pieces of information for this dataset with supporting evidence of "interestingness'
# You code for calculating the analysis should be documented and tested.
# Tests should be in a separate file runnable from the command line.
# Your statistical analytics conclusions should be in a word document explaining in approximately 500 words the information that you have gleamed from the dataset.
# You will be required to submit your code via github along with all documentation and tests.

import pandas as pd

# Open file and read in the lines.
# 
changes_file = 'changes_python.log'

# Use strip to strip out spaces.
my_file = open(changes_file, 'r')
data = my_file.readlines()

data = [line.strip() for line in open(changes_file, 'r')]

# Create string sep that consists of 72 hyphens
sep = 72*'-'

# Search the document and break up into objects based on sep
# Create a class to store the elements of each object
class Commit(object):
    def __init__(self, revision=None, author=None, date_time=None, comment_line_length=None, 
            comment=None):
        self.revision = revision
        self.author = author
        self.date_time = date_time
        self.date = ""
        self.time = ""
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

    # Function to convert changes to string type.
    def convert_comments_to_string(self):
        self.changes =  str(self.changes).strip('[]')

index = 0
current_commit = None
commits = []

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
        else:
            commits.append(current_commit)
    except IndexError:
        break
        
# Create data frame by converting each object in commit to a dict
df = pd.DataFrame(commit.to_dict() for commit in commits)
# Reorder the columns
df=df[['author', 'date', 'time','changes']]
# Print out the first 5 columns
print df.head(5)