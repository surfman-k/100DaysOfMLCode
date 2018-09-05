import pandas as pd

melbourne_file_path = '../input/melbourne-housing-snapshot/melb_data.csv'
melbourne_data = pd.read_csv(melbourne_file_path) 
melbourne_data.columns

# dropna drops missing values (think of na as "not available")
melbourne_data = melbourne_data.dropna(axis=0)

y = melbourne_data.Price

melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']

X = melbourne_data[melbourne_features]

X.describe()
#    	Rooms	Bathroom	Landsize	Lattitude	Longtitude
# count	6196.000000	6196.000000	6196.000000	6196.000000	6196.000000
# mean	2.931407	1.576340	471.006940	-37.807904	144.990201
# std	0.971079	0.711362	897.449881	0.075850	0.099165
# min	1.000000	1.000000	0.000000	-38.164920	144.542370
# 25%	2.000000	1.000000	152.000000	-37.855438	144.926198
# 50%	3.000000	1.000000	373.000000	-37.802250	144.995800
# 75%	4.000000	2.000000	628.000000	-37.758200	145.052700
# max	8.000000	8.000000	37000.000000	-37.457090	145.526350

X.head()
# 	Rooms	Bathroom	Landsize	Lattitude	Longtitude
# 1	2	    1.0	        156.0	    -37.8079	144.9934
# 2	3	    2.0	        134.0	    -37.8093	144.9944
# 4	4	    1.0	        120.0	    -37.8072    144.9941
# 6	3	    2.0	        245.0	    -37.8024	144.9993
# 7	2	    1.0	        256.0	    -37.8060	144.9954


from sklearn.tree import DecisionTreeRegressor

# Define model. Specify a number for random_state to ensure same results each run
melbourne_model = DecisionTreeRegressor(random_state=1)

# Fit model
melbourne_model.fit(X, y)
