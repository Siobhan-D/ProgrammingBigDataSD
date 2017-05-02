# Create a separate class as an object to store attributes and functions
# that relate to the analysis of a log file so that it can be reused for all files of 
# the same type.

import Commit from changes.py

class Analyse_log_file():

    def __init__(self, file_name = ''):
        self.commits = []
        self.current_commit = None
        self.file_name = file_name
        self.data = self.prep_file
        self.authors = []
    
    # Function to extract data from the file.
    def prep_file(self):
        # Use strip to strip out spaces.
        data = [line.strip() for line in open(self.file_name, 'r')]
        return data
    
    # # Function to extract data from a log file containing a recorded of commits by different authors.
    def get_commits(self):
        index = 0
        sep = 72*'-'
        while True:
            try:
                details = self.data[index+1].split('|')
                current_commit = Commit()
                current_commit.revision = details[0].strip()
                current_commit.author = details[1].strip()
                current_commit.date_time = details[2].strip()
                current_commit.get_date_time()
                current_commit.comment_line_length = int(details[3].strip().split(' ')[0])
                index = self.data.index(sep, index+1)
                current_commit.changes = data[index-current_commit.comment_line_length:index]
                current_commit.convert_comments_to_string()
                # Skip uninteresting entries
                if current_commit.author == '/OU=Domain Control Validated/CN=svn.company.net':
                    continue  
                else:
                    commits.append(current_commit)   
            except IndexError:
                break
        return self.commits

    # Create functions to analyse and plot the changes data.

    # Function to get a list of all authors.
    def get_authors(self):
        for commit in self.commits:
            author = commit.author
            if author in authors:
                continue
            else:    
                authors.append(author]
        return authors
    print authors

    # Function to count the number of revisions per author.
    def count_revisions():
        pass


        
