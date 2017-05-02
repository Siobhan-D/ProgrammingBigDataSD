# Assignment 4 is based on transforming a large dataset in text format - over 5000 lines of text.
# You will need to scrub (clean) the data and place it into the relevant holder/container objects.
# Once in these objects you will see that there are 422 different sets of commit objects.
# So your task will be to analyse these 422 objects that are in a list and come up with 3 interesting statistical pieces of information for this dataset with supporting evidence of "interestingness'
# You code for calculating the analysis should be documented and tested.
# Tests should be in a separate file runnable from the command line.
# Your statistical analytics conclusions should be in a word document explaining in approximately 500 words the information that you have gleamed from the dataset.
# You will be required to submit your code via github along with all documentation and tests.

# Open file and read in the lines.
# 
changes_file = 'changes_python.log'

# Use strip to strip out spaces.
my_file = open(changes_file, 'r')
data = my_file.readlines()

print data

data = [line.strip() for line in open(changes_file, 'r')]

print len(data)

# Create string sep that consists of 72 hyphens
sep = 72*'-'

# Search the document and break up into objects based on sep
# Create a class to store the elements of each object
class Commit(object):
    def __init__(self, revision=None, author=None, date=None, comment_line_length=None, 
            changes=None, comment=None):
        self.revision = revision
        self.author = author
        self.date = date
        self.comment_line_length = comment_line_length
        self.changes = changes
        self.comment = comment

a_commit = Commit('r1551925', 'Thomas', '2015/11/27', 1, None, 
        'Renamed folder to the correct name')

print a_commit.author
print a_commit.comment

