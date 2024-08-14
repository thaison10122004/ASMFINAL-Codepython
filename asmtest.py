import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Step 1: Generate Synthetic Data
np.random.seed(42)
years = np.arange(1, 11)  # Years from 1 to 10
revenue = 100 + 20 * years + np.random.normal(scale=30, size=years.shape)  # Revenue with noise

# Convert to DataFrame
data = pd.DataFrame({'Year': years, 'Revenue': revenue})

# Step 2: Visualize the Data
plt.scatter(data['Year'], data['Revenue'], color='blue')
plt.title("Revenue Over Time")
plt.xlabel("Year")
plt.ylabel("Revenue")
plt.show()

# Step 3: Split the Data
X = data[['Year']]
y = data['Revenue']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 4: Train the Linear Regression Model
model = LinearRegression()
model.fit(X_train, y_train)

# Step 5: Predict on the Test Set
y_pred = model.predict(X_test)

# Step 6: Evaluate the Model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f"Mean Squared Error: {mse:.2f}")
print(f"R-squared: {r2:.2f}")

# Step 7: Visualize the Prediction
plt.scatter(data['Year'], data['Revenue'], color='blue', label='Actual Revenue')
plt.plot(data['Year'], model.predict(data[['Year']]), color='red', label='Predicted Revenue')
plt.title("Revenue Prediction Over Time")
plt.xlabel("Year")
plt.ylabel("Revenue")
plt.legend()
plt.show()

# Step 8: Predict Future Revenue
future_years = np.array([[11], [12], [13], [14], [15]])
future_revenue_pred = model.predict(future_years)

# Print Future Revenue Predictions
for year, revenue in zip(future_years.flatten(), future_revenue_pred):
    print(f"Year {year}: Predicted Revenue = {revenue:.2f}")
