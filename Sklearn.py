import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Create DataFrame from data
data = {
    'ProductID': list(range(1, 61)),
    'Price': [951.16, 688.42, 323.91, 992.54, 559.61, 851.51, 221.3, 164.85, 716.32, 675.45, 816.79, 918.64, 
              551.96, 187.44, 519.77, 261.25, 947.96, 257.0, 897.11, 211.41, 678.82, 617.65, 856.21, 840.07, 
              551.86, 989.3, 158.84, 698.27, 524.1, 599.86, 388.43, 431.7, 795.2, 266.55, 943.24, 108.97, 
              869.29, 158.21, 786.52, 273.83, 916.31, 712.4, 249.91, 811.39, 108.05, 935.75, 431.12, 176.46, 
              634.58, 964.13, 156.61, 702.31, 517.83, 401.21, 991.76, 253.81, 831.37, 267.53, 715.62, 395.46],
    'Stock': [34, 314, 426, 276, 681, 475, 406, 468, 111, 976, 551, 910, 476, 105, 36, 727, 918, 954, 734, 
              615, 520, 119, 466, 154, 210, 859, 885, 893, 343, 116, 342, 786, 243, 921, 571, 637, 189, 
              487, 653, 498, 254, 729, 343, 211, 914, 164, 286, 743, 522, 321, 874, 639, 345, 781, 652, 
              421, 196, 481, 632, 399]
}

df = pd.DataFrame(data)

# Split the data into training and test sets
X = df[['Price']]
y = df['Stock']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model training
model = LinearRegression()
model.fit(X_train, y_train)

# Prediction on test set
y_pred = model.predict(X_test)

# Draw chart
plt.figure(figsize=(10, 6))
plt.scatter(X_test, y_test, color='blue', label='Actual Stock Quantity')
plt.plot(X_test, y_pred, color='red', linewidth=2, label='Regression Line')
plt.title('Product Growth: Price vs Stock Quantity')
plt.xlabel('Price')
plt.ylabel('Stock Quantity')
plt.legend()
plt.grid(True)
plt.show()