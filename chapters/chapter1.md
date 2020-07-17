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

If you self-assessed at `4` or less consider taking the beginner track challenges during the hackathon.

If you self-assessed at  `5` or higher consider taking the intermediate / advanced track challenges during the hackathon.

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

If you self-assessed at `0` consider taking the beginner track challenges during the hackathon.

If you self-assessed at  `1` or higher consider taking the intermediate / advanced track challenges during the hackathon.


</exercise>
