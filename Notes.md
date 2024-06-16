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
1. Income (+ve relation with Personal Loan)
2. Education (+ve relation with Personal Loan) (-ve with income)

Other significant influencers of Personal Loan:
1. CCAvg (Monthly credit card expense) (+ve relation with Personal Loan, +ve cuve-linear income)
2. CD Account (+ve relation with Personal Loan, +ve income)
3. Home Ownership (rent is bad for getting loan)
4. Mortgage (-ve relation with Personal Loan, -ve curve-linear income)
5. Gender (effected Personal Loan due to income distribution between genders)

## Feature Enginnering
1. Gender:  Label Encoding
2. Zip code: drop
3. Family :  Already has gone through Label Encoding 
4. Home Ownership: Label Encoding
Split data into training and testing set in 7:3 ratio.

## Modeling & Evaluation
Trained KNN, Decision tree, SVM and Logistic Regression models on best found parameters which were identified using GridSearchCV.  Then evaluated there training & testing accuracy alongside plotting their confusion matrix. 

1. KNN: False negatives seems to be a big problem for this KNN model.
2. Decision Tree: Here, problem of false negative is substantially lower compared to KNN but the problem of false positive seems to have risen.
3. SVM: This model has by far the best accuracy score of 95.02% but is a little worse compared to the Decision Tree model as the true positive is a little lower. It also took an exceptionally long time to train this model i.e. about 30 minutes, this is with optimization for best performance.
4. Logistic Regression: This model has the highest false positives but is still better than the KNN model due to its lower false negative and higher true positives.
### Model Comparison
  
| Model               | TestPerformance |
| ------------------- | --------------- |
| Logistic Regression | 0.9415421       |
| SVM                 | 0.9502492       |
| Decision Tree       | 0.9477613       |
| K Near Neighbor     | 0.921642        |
We can clearly see that the SVM model has the best accuracy of 95.02% but as it takes a very **long time to train**, i.e. about 30 min in my case, and has less true positives compared to the second best model i.e. Decision Tree model with 94.77% accuracy. I have decided that the Decision Tree model is better overall.


## Model Export & Import
The decision tree model which was considered the best was exported using joblib so that it could easily be access. This model was imported again using joblib to make some predictions.

When we inputted best values for key attributes like. **Income, Home Ownership, CCAvg, Education, Mortgage & CD Account** and worst values for other irrelevant attributes, based on the Exploratory Data Analysis done before, it is predicated that loan application will be approved. 

## Conclusion
This shows that the relationship discovered between various factors were correct and the trained model is working accurately.
