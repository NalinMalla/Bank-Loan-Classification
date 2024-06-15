Q) df.info() was outputted before the written text. Why?
```python
print("Data type of each column:",df.info())
```

### Data Profiling
#### 1. Data type
- Mortgage is of int64 type but I think it needs to be float64 like income.
- Personal Loan which contains binary values is of object type i.e. string not int.
- Check to see if "Online" is binary classification and if so convert float type to int.

#### 2. Summery Statistics
Columns with missing data:
- Gender: 3404 count (irrelevant)
- Income: 4933 count (replace with mean)
- Home Ownership: 3811 count (relevant)
- Online: 4960 count (irrelevant)

- ID: std of ID that contains sequence of [1:5000] is 1443.52 which I think suggests some issue (abnormal distribution). Even the quartile are in factions which should not be the case. 
- Age: min age is 0 but bank loans are only given to 18+. Though there is no specified max age limit for bank loans, the age of 978 is obviously an outlier. std seems right.
- Experience: min is -3 which is not possible. 
- CCAvg: If 3rd quartile is 2.5k then max of 10k seems like an outlier.
- Mortgage: std is double of mean so data fluctuates from one extreme to next. min, 25% & 50% is 0 and 75% & max is 101k & 635k resp.
- Gender: 5 different types of values even though there should only be 3.


Deduction for binary valued columns
- CD Account: It's a binary value but as min, 25%, 50% & 75% is 0 and only max is 1 we may deduce that vast majority don't have a CD Account.
- Online:  It's a binary value but as only min, 25% is 0 and only 50%, 75% & max is 1 we may deduce that majority have a internet banking.
Similarly,
- Security Account: vast majority don't have them.
- Credit Card: majority don't have them.

Note: 
- Notice that std+/- mean is always > & < than 75% & 25%. This is because that interquartile range only account 50% of sample while +/-1std usually accounts for 68%.
- Explore deducing skewness based on difference in mean & median.

## Exploratory Data Analysis

Main Influencers of Personal Loan:
1. Income (+ve)
2. Education (+ve) (-ve with income)

Other significant influencers of Personal Loan:
1. CCAvg (Monthly credit card expense) (+ve, +ve cuve-linear income)
2. CD Account (+ve, +ve income)
3. Home Ownership (rent is bad for getting loan)
4. Mortgage (-ve, -ve curve-linear income)
5. Gender (due to income distribution between genders)

## Feature Enginnering
1. Gender: One hot encoding/ Label Encoding
2. Zip code: drop
3. Family :  Already has gone through Label Encoding 
4. Home Ownership: One hot encoding/ Label Encoding
