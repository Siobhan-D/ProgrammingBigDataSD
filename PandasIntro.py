
# coding: utf-8

# In[1]:

# import the data analytics packages. Use np and pd so you don't have to type entire word each time.
import numpy as np
import pandas as pd


# In[36]:

# Create a series. One-dimensional array that holds any data type. similar to c function in R.
# Quick way to set up a spreadsheet
# If assigned to a variable does not display output. Must be called.
s = pd.Series(np.random.randn(5),index=['a','b','c','d','e'])
s


# In[8]:

s.index


# In[22]:

# Default series without any indexing
pd.Series(np.random.randn(5))


# In[11]:

# A dictionary is a set of named  value pairs. a, b, and c are the column names. Takes the same format as JSON.
d = {'a' : 0., 'b' : 1., 'c' : 2.}
# This will add to the next row since the names are the same as previous dictionary.
d2 = {'a' : 3., 'b' : 4., 'c' : 5.} 


# In[12]:

d


# In[13]:

# Turn the dictionary into a series by passing it in. Basically a dictionary flipped on it's side. 
# The columns become rows. Allow you to easily interrogate objects. Similar to R.
pd.Series(d)


# In[14]:

# You can change the order of the columns and add new indexes. Gives NaN if no value exists.
pd.Series(d, index = ['b','c','a','d'])


# In[30]:

# If only one value is given then python assigns same value to each index.
pd. Series(5., index = ['a','b','c','d','e'])
# Can use indexing
s[0]


# In[31]:

# Series is similar to ndarray from  numpy.
s[0]
# Can use slice notation. Gives first 3 values  back.
s[:3]


# In[32]:

# Only give values of s where it is greater than the median
s[s>s.median()]


# In[38]:

# Use double square brackets to look for a subset of values.
# Note: R indexes start at 1 and python indexes start at 0.
s[[4,3,1]]


# In[40]:

# exp will take all the values and exponentiate them.
np.exp(s)


# In[41]:

# You can also reference by using the name of the index.
s['a']


# In[44]:

# You can also set the values using indexing
s['a']=12
s['a']


# In[45]:

# If the column doesn't exist you will get an exception error. 
s['f']


# In[49]:

# This is not good so instead use the if in statement.
if 'a' in s:
    print(s['a'])


# In[52]:

# Another way of preventing error is using the get function. If it doesn't exist nothing is returned.
# Use 'np.nan' which returns nan if it doesn't exist. This will maintain consistency.
s.get('f'),np.nan


# In[53]:

# You can perfom operations on the whole series just like in R. The following will do vector-based addition and double s.
# But it does not change the values in s!
s+s


# In[54]:

s*2


# In[55]:

s*3


# In[56]:

np.exp(s)


# In[57]:

s[1:]


# In[59]:

s[:-1]


# In[60]:

# If you try do vector arithmetic where some matching values don't exist. It will give nan. 
# Safer to work with as this can have bad effects when doing statistics. We will look at how to deal with this.
s[1:]+s[:-1]


# In[61]:

# You can name your series but it's not extremely useful. Better to assign it to name in the first place.
s = pd.Series(np.random.randn(5), name = 'Something')
s.name


# In[62]:

# To add an extra column
s['f']=0
s


# In[63]:

# Pandas dataframe is a 2D data structure (table).
# Accepts many types of input.
# Here we have created a dictionary with 2 keys and each contains a series. These can then be input into a dataframe.
d = {'one' : pd.Series([1., 2., 3.], index=['a', 'b', 'c']),'two' : pd.Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd'])}
d
df = pd.DataFrame(d)
df


# In[66]:

# You can create df using only subset of the data and you can also create new columns.
pd.DataFrame(d, index=['d','b','e'], columns=['two','three'])


# In[68]:

d = {'one' : [1., 2., 3., 4.],'two' : [4., 3., 2., 1.]}
pd.DataFrame(d)


# In[70]:

# Create data frame using numpy function zeros with column names A,B,C and specify the types. Sets up the new array with
# integer of length 4, float of length 4, and string of length 10.
# The array is populated based on the given data types. Strings are given blank value as shown in the output.
# We have specified 2 columns but can be any number of rows since not specified.
data = np.zeros((2,), dtype=[('A','i4'),('B','f4'),('C','a10')])
data


# In[71]:

# Then you can set the values.
data[:] = [(1,2.,'Hello'),(2,3.,'World')]
data


# In[73]:

# Now we can convert this to a data frame
pd.DataFrame(data, index=['First','Second'])


# In[74]:

# You can specify order of columns
my_data = pd.DataFrame(data, columns = ['C','A','D'])


# In[75]:

my_data


# In[76]:

data2 = [{'a': 1, 'b': 2}, {'a': 5, 'b': 10, 'c': 20}]
pd.DataFrame(data2)


# In[77]:

pd.DataFrame(data2, index=['first', 'second'])
pd.DataFrame(data2, columns=['a', 'b'])


# In[78]:

# From a data frame of tuples. This is not the best way to do this as it's unecessary
pd.DataFrame({('a', 'b'): {('A', 'B'): 1, ('A', 'C'): 2},('a', 'a'): {('A', 'C'): 3, ('A', 'B'): 4},
            ('a', 'c'): {('A', 'B'): 5, ('A', 'C'): 6},
            ('b', 'a'): {('A', 'C'): 7, ('A', 'B'): 8},
            ('b', 'b'): {('A', 'D'): 9, ('A', 'B'): 10}})


# In[79]:

df


# In[80]:

df['one']


# In[81]:

df['three']=df['one']*df['two']


# In[82]:

df


# In[83]:

# Set a new boolian column that will test whether column one is greater than 2. NaN values will give back false value 
# so this can be misleading.
df['flag']=df['one']>2


# In[84]:

df


# In[93]:

# You can remove a column delete or using pop and you can also create a new df from these popped values.
# del df['two']
one = df.pop('one')


# In[94]:

one


# In[95]:

df


# In[97]:

# The following both insert a column
df.insert(1,'bar',df['one'])
#df['bar'] = df['one']


# In[ ]:



