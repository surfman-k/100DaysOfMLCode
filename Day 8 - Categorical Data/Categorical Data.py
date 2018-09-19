# Categorical Data

# Categorical data is data that takes only a limited number of values.
# For example, if you people responded to a survey about which what brand of car they owned, the result would be categorical (because the answers would be things like Honda, Toyota, Ford, None, etc.). Responses fall into a fixed set of categories.
# You will get an error if you try to plug these variables into most machine learning models in Python without "encoding" them first. Here we'll show the most popular method for encoding categorical variables.

# One hot encoding is the most widespread approach, and it works very well unless your categorical variable takes on a large number of values (i.e. you generally won't it for variables taking more than 15 different values. It'd be a poor choice in some cases with fewer values, though that varies.)
# One hot encoding creates new (binary) columns, indicating the presence of each possible value from the original data. 


# Pandas assigns a data type (called a dtype) to each column or Series. Let's see a random sample of dtypes from our prediction data:

train_predictors.dtypes.sample(10)
# Heating          object
# CentralAir       object
# Foundation       object
# Condition1       object
# YrSold            int64
# PavedDrive       object
# RoofMatl         object
# PoolArea          int64
# EnclosedPorch     int64
# KitchenAbvGr      int64
# dtype: object

# Object indicates a column has text (there are other things it could be theoretically be, but that's unimportant for our purposes). It's most common to one-hot encode these "object" columns, since they can't be plugged directly into most models. Pandas offers a convenient function called get_dummies to get one-hot encodings. Call it like this:
one_hot_encoded_training_predictors = pd.get_dummies(train_predictors)

# Alternatively, you could have dropped the categoricals. To see how the approaches compare, we can calculate the mean absolute error of models built with two alternative sets of predictors:

# One-hot encoded categoricals as well as numeric predictors
# Numerical predictors, where we drop categoricals.
# One-hot encoding usually helps, but it varies on a case-by-case basis. In this case, there doesn't appear to be any meaningful benefit from using the one-hot encoded variables.

from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestRegressor

def get_mae(X, y):
    # multiple by -1 to make positive MAE score instead of neg value returned as sklearn convention
    return -1 * cross_val_score(RandomForestRegressor(50), 
                                X, y, 
                                scoring = 'neg_mean_absolute_error').mean()

predictors_without_categoricals = train_predictors.select_dtypes(exclude=['object'])

mae_without_categoricals = get_mae(predictors_without_categoricals, target)

mae_one_hot_encoded = get_mae(one_hot_encoded_training_predictors, target)

print('Mean Absolute Error when Dropping Categoricals: ' + str(int(mae_without_categoricals)))
print('Mean Abslute Error with One-Hot Encoding: ' + str(int(mae_one_hot_encoded)))

