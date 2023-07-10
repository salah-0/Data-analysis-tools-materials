import moodle
# import mysql.connector
# import pandas as pd
# from sklearn.linear_model import LinearRegression
# import matplotlib.pyplot as plt

# # Connect to MySQL database
# db = mysql.connector.connect(
#     host=moodle.host,
#     user=moodle.user,
#     password=moodle.password,
#     database=moodle.database
# )

# # Check if the connection is successful
# if db.is_connected():
#     print("Connected to the MySQL database")

# # Create a cursor object to interact with the database
# cursor = db.cursor()

# # Execute a query to retrieve the data


# query = "SELECT maximum_nights, price FROM London_Airbnb_Listings_March_2023"
# cursor.execute(query)

# print("Query executed successfully")

# # Fetch all the results
# results = cursor.fetchall()

# # Close the database connection
# cursor.close()
# db.close()

# print("Database connection closed")

# # Convert the results into a pandas DataFrame
# df = pd.DataFrame(results, columns=["maximum_nights", "price"])

# # Preprocess the "price" column to remove commas
# df["price"] = df["price"].str.replace(",", "").astype(float)

# # Split the data into independent (X) and dependent (y) variables
# X = df[["maximum_nights"]]
# y = df["price"]

# # Create a linear regression model
# model = LinearRegression()

# # Fit the model to the data
# model.fit(X, y)

# # Make predictions based on the model
# y_pred = model.predict(X)

# # Plot the data points and the regression line
# plt.scatter(X, y, color='b', label="Actual Data")
# plt.plot(X, y_pred, color='r', label="Linear Regression")
# plt.xlabel("Maximum Nights")
# plt.ylabel("Price")
# plt.title("Linear Regression: Maximum Nights vs Price")
# plt.legend()
# plt.show()



import mysql.connector

db = mysql.connector.connect(
    host=moodle.host,
    user=moodle.user,
    password=moodle.password,
    database=moodle.database
)
cursor=db.cursor()

cursor.execute("SELECT London_Airbnb_Listings_March_2023 FROM information_schema.tables")

for London_Airbnb_Listings_March_2023 in cursor:
   print(London_Airbnb_Listings_March_2023)