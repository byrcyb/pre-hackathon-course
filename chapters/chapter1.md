---
title: 'Chapter 1: Before we start, assess yourself!'
description:
    'This chapter will help you evaluate your skills with Python and Data Science before you take part in a Callysto hackathon.'
prev: null
next: /chapter2
type: chapter
id: 1
---

<exercise id="1" title="How's Your Python">

# Levels of Python Comfort

This is a self-assessment tool, which of the following code snippets do you think you could have written?

0. I have never seen any Python before.

1. Basics
```python
print('Hello World')
```

2. Variables
```python
phrase = 'Hello World'
print(phrase)
```

3. Loops
```python
for x in range(5):
    print(x + 2)
```

4. Conditions
```python
for x in range(5):
    print(x)
    if x == 2:
        print('This is two')
```

5. Functions
```python
def multiply_by_three(x):
    y = x * 3
    return y
multiply_by_three(9)
```

6. Dictionaries
```python
mars_missions_2011 = {'Fobos-Grunt':'Roskosmos', 
                      'Yinghuo-1':'CNSA', 
                      'Curiosity':'NASA'}
for mission, agency in mars_missions_2011.items():
    print('The',mission,'mission was led by',agency)
```

If you self-assessed at `5` or less consider taking the beginner track challenges during the hackathon.

If you self-assessed at  `6` or higher consider taking the intermediate / advanced track challenges during the hackathon.

</exercise>

<exercise id="2" title="How's Your Data Science">

# Levels of Data Science Comfort

This is a self-assessment tool, which of the following code snippets do you think you could have written?

0. I have never seen any of this before.

1. Creating a Data Frame
```python
import pandas as pd
df = pd.read_html('https://en.wikipedia.org/wiki/List_of_missions_to_Mars')[0]
```

2. Basic Statistics
```python
df.describe()
df['Column 1'].mean()
```

2. Filtering Data
```python
df[df['Column 1']=='green']
```

3. Cleaning Data
```python
df['Year'] = df['Launch Date'].str.split(' ', expand=True)[2]
df.fillna(value=0, inplace=True)
```

4. More Statistics
```python
df.groupby(by='Year')['Year'].count()
df.agg(['min', 'max'])
```

5. Merging Data
```python
df.append(df2, ignore_index=True)
new_df = pd.concat([df, df2], axis=1)
```

6. Plotting
```python
import cufflinks as cf
cf.go_offline()
df.iplot(kind='barh', x='Column 1', y='Column 2', xTitle='Time', yTitle='Frequency', title='Frequency over Time')
```

If you self-assessed at `1` consider taking the beginner track challenges during the hackathon.

If you self-assessed at  `2` or higher consider taking the intermediate / advanced track challenges during the hackathon.


</exercise>

<exercise id="4" title="Where It Begins">

Hello. We need your help to settle an argument. One of the Grade 3 teachers insists that June has nicer weather than August, so we should change the school calendar to have time off in June and go back in August.
Can you use data science to solve this argument?

</exercise>

<exercise id="5" title="The Data">

The first thing we need to do to solve this argument is to find some weather data. We'll use data from **Edmonton, Alberta**, in this case because that's where the teacher is from. In our course we'll also show you how you can get weather data from other places in Canada, or the world.

Historical weather data sets are available from the [Canadian Centre for Climate Services](https://www.canada.ca/en/environment-climate-change/services/climate-change/canadian-centre-climate-services.html).

We can use an online data science platform called Jupyter notebooks to run code, create visualizations, and write about what we find. To log in to a free server that runs Jupyter notebooks, all you need in order to access it is a Google or Microsoft account. (We'll do this later.)

</exercise>

<exercise id="6" title="Let's Wrangle">

<codeblock id="01_01">

This is a hint.

</codeblock>



</exercise>

