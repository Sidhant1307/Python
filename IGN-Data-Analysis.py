import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("F:\WORK\Language\ign.csv")
df['release_year'].max()

##df1 has games of release year 2012 
df1 = df[df['release_year']==2012].values


###df2 hold data in form of columns of release year 2012
df2 = pd.DataFrame(df1,columns = df.columns)


##df3 has data of games with score 'Amazing ' and release year 2012
df3 = df[(df.score_phrase == 'Amazing') & (df.release_year == 2012)]


from IPython.display import display
pd.options.display.max_rows = 99999

df.shape
df.score_phrase.value_counts()
df.score_phrase.unique()
fight = df[df.genre == 'Fighting']
pd.DataFrame(fight.release_year.value_counts()).sort_index().plot.line()
plt.legend(['Fighting'])
plt.show()


pie = df.score_phrase.value_counts()
pie = pie.values


plt.figure(figsize = (5,5))
plt.pie(pie)
plt.legend(df.score_phrase.unique())
plt.show()

df.score_phrase.value_counts().plot.bar()
plt.show()
