import Quandl
import pandas as pd
import html5lib
import pickle

api_key = 'BwzLcN_LfpQdyqAQdS6J'
df = Quandl.get('FMAC/HPI_AK',  authtoken = api_key)

# print df.head(10)

fiddy_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
# This is a list of dataframes
# print(fiddy_states) 

# This is a dataframe
# print fiddy_states[0]

# This is a column
# print fiddy_states[0][0]

for abv in fiddy_states[0][0][1:]:
	print "FMAC/HPI_" + str(abv)







# df.to_csv()
