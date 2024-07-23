import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Some extra libraries for date conversions and build the webapp
import streamlit as st

# ----- Page configs -----
st.set_page_config(
    page_title="Ayman's Portfolio",
    page_icon="📊",
)


# ----- Left menu -----
with st.sidebar:
    st.write("Project to predict the actual market value of football players based on their Fifa stats.")
    st.write("Data extracted from SoFifa.com using web-scraping (with some cleaning and modifications).")


# ----- Title of the page -----
st.title("📖 Market Value Prediction")
st.divider()

@st.cache_data
def load_data_football():
    data_path = "data/FootballPlayers_cleaned.xlsx"

    result = pd.read_excel(data_path)  # TODO: Ex 2.1: Load the dataset using Pandas, use the data_path variable and set the index column to "show_id"

    return result   # a Pandas DataFrame

result = load_data_football()

# Displaying the dataset in a expandable table
with st.expander("Check the complete dataset:"):
    st.dataframe(result)
    
# Creating correlation matrix
result_without_name = result.drop(columns=['Name', 'Team', 'Foot', 'Best Position'])
corr = result_without_name.corr()


# ----- Displaying the extracted information metrics -----
st.write("##")
st.header("Correlation Matrix With All Attributes")

fig = plt.figure(figsize=(25, 21))

# Draw the heatmap with the correlation matrix
sns.heatmap(corr, annot=False, fmt='.2f', cmap='coolwarm', vmin=-1, vmax=1, center=0, linewidths=0.5)

# Add title and labels for better readability
plt.title('Correlation Matrix', fontsize=16)
plt.xticks(rotation=45, ha='right')
plt.yticks(rotation=0)

st.pyplot(fig)


st.write("##")
st.header("Correlation Matrix With All Attributes (Most Correlated)")

#Correlation With Market Value (most correlated)
market_value_most = pd.DataFrame(corr["Market Value"]).sort_values("Market Value", ascending=False).head(25)
st.dataframe(data=market_value_most, width=300)

st.write("##")
st.header("Correlation Matrix With All Attributes (Least Correlated)")

#Correlation With Value (least correlated)
market_value_least = pd.DataFrame(corr["Market Value"]).sort_values("Market Value", ascending=True).head(25)
st.dataframe(data=market_value_most, width=300)


# Selecting attributes that will be used for the model
selected_columns = result[['Overall Rating','Release Clause','Best Overall','International Reputation','Potential', 'Base Stats', 'Total Stats', 'Wage', 'Height', 'Age', 'Weight']]



st.write("##")
st.header("Correlation Matrix With Selected Attributes")

fig = plt.figure(1, figsize=(18, 7))
sns.set(style="whitegrid")
sns.heatmap(selected_columns.corr(), cmap="seismic", annot=True, vmin=-1, vmax=1)
plt.yticks(rotation=0)

st.pyplot(fig)



st.write("##")
st.header("Pairplot Selected Attributes")

#Pairplot of selected features
plt.figure(1, figsize=(18, 7))
sns.set(style="whitegrid")
fig2 = sns.pairplot(selected_columns, height=1.2, aspect=1.5)
plt.yticks(rotation=90); 
st.pyplot(fig2)


st.write("##")
st.header("Developing a model using Random Forest Regressor")


@st.cache_data
def train_model(result):

    # Making the Machine Learning model
    from sklearn.preprocessing import StandardScaler
    from sklearn.model_selection import cross_val_score, train_test_split
    from sklearn.ensemble import RandomForestRegressor
    from sklearn.metrics import mean_squared_error
    import numpy as np

    # Select features and target
    X_selected_rfg = result.loc[:, ['Overall Rating', 'Release Clause', 'Best Overall', 'International Reputation', 'Potential', 'Base Stats', 'Total Stats', 'Wage', 'Height', 'Age', 'Weight']]
    y_selected_rfg = result.loc[:, "Market Value"]

    # Scale the features
    scaler = StandardScaler()
    X_scaled_rfg = scaler.fit_transform(X_selected_rfg)

    # Split the data
    X_train_rfg, X_test_rfg, y_train_rfg, y_test_rfg = train_test_split(X_scaled_rfg, y_selected_rfg, test_size=0.2, random_state=42)

    # Train the model
    rf = RandomForestRegressor(n_estimators=300, random_state=42)
    rf.fit(X_train_rfg, y_train_rfg)

    # Predict and evaluate
    y_pred_test_rfg = rf.predict(X_test_rfg)
    mse_rfg = mean_squared_error(y_test_rfg, y_pred_test_rfg)
    r2_rfg = rf.score(X_test_rfg, y_test_rfg)
    rmse_rfg = np.sqrt(mse_rfg)


    # Calculate Adjusted R²
    n = len(y_test_rfg)
    k = X_test_rfg.shape[1]
    adjusted_r2_rfg = 1 - ((1 - r2_rfg) * (n - 1) / (n - k - 1))

    # Cross-validation
    cv_scores_rfg = cross_val_score(rf, X_scaled_rfg, y_selected_rfg, cv=5, scoring='r2')

    # print(f"R² Score RFG: {r2_rfg}")
    # print(f"Mean Squared Error RFG: {mse_rfg}")
    # print(f"Cross-Validation R² Scores RFG: {cv_scores_rfg}")
    # print(f"Root Mean Squared Error RFG: {rmse_rfg}")
    # print(f"Adjusted R² Score RFG: {adjusted_r2_rfg}")


    # Predict on the entire dataset
    y_pred_all_rfg = rf.predict(X_scaled_rfg)

    
    return {
        "r2_rfg": r2_rfg,
        "mse_rfg": mse_rfg,
        "rmse_rfg": rmse_rfg,
        "adjusted_r2_rfg": adjusted_r2_rfg,
        "cv_scores_rfg": cv_scores_rfg,
        "y_pred_all_rfg": y_pred_all_rfg,
        "y_selected_rfg": y_selected_rfg
    }

model_results = train_model(result)

st.write(f"R² Score RFG: {model_results['r2_rfg']}")
st.write(f"Mean Squared Error RFG: {model_results['mse_rfg']}")
st.write(f"Root Mean Squared Error RFG: {model_results['rmse_rfg']}")
st.write(f"Adjusted R² Score RFG: {model_results['adjusted_r2_rfg']}")
st.write(f"Cross-Validation R² Scores RFG: {model_results['cv_scores_rfg']}")



st.write("##")
st.header("Plotting Residuals")

result['Predicted Market Value'] = model_results['y_pred_all_rfg']
result['Difference'] = result['Market Value'] - result['Predicted Market Value']

# # Display the DataFrame
# print(result[['Name', 'Market Value', 'Predicted Market Value', 'Difference']].head())

fig3 = plt.figure(figsize=(10, 6))
plt.hist(result['Difference'], bins=50, edgecolor='k', alpha=0.7)
plt.title('Residuals Distribution')
plt.xlabel('Residuals')
plt.ylabel('Frequency')
plt.grid(True)
st.pyplot(fig3)



st.write("##")
st.header("Bar Chart of Undervalued Players")

undervalued_df1 = result.sort_values(by='Difference', ascending=True).head(10)

undervalued_df1.set_index('Name', inplace=True)

#Plot the comparision of Actual and Predicted Values for Under Predicted
fig4, ax = plt.subplots(figsize=(10, 5))
undervalued_df1[["Market Value","Predicted Market Value"]].plot(kind='bar', ax=ax)
ax.grid(which='major', linestyle='-', linewidth='0.5', color='green')
ax.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
ax.set_title("Actual vs Predicted Values for Undervalued Players")
ax.set_xlabel("Player Name")
ax.set_ylabel('Value')
ax.yaxis.get_major_formatter().set_scientific(False)
st.pyplot(fig4)



st.write("##")
st.header("Bar Chart of Overvalued Players")

overvalued_df1 = result.sort_values(by='Difference', ascending=False).head(10)

overvalued_df1.set_index('Name', inplace=True)

fig5, ax = plt.subplots(figsize=(10, 5))
overvalued_df1[["Market Value","Predicted Market Value"]].plot(kind='bar', ax=ax)
ax.grid(which='major', linestyle='-', linewidth='0.5', color='green')
ax.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
ax.set_title("Actual vs Predicted Values for Overvalued Players")
ax.set_xlabel("Player Name")
ax.set_ylabel('Value')
ax.yaxis.get_major_formatter().set_scientific(False)
st.pyplot(fig5)



st.write("##")
st.header("Scatter Plot of Actual Market Values vs Predicted Market Values")

fig6 = plt.figure(figsize=(10, 6))
plt.scatter(model_results['y_selected_rfg'], model_results['y_pred_all_rfg'], color='blue', edgecolor='k', alpha=0.7)
plt.plot([model_results['y_selected_rfg'].min(), model_results['y_selected_rfg'].max()], [model_results['y_selected_rfg'].min(), model_results['y_selected_rfg'].max()], 'k--', lw=2)
plt.xlabel('Actual Market Value')
plt.ylabel('Predicted Market Value')
plt.title('Actual vs Predicted Market Values')
plt.grid(True)
plt.ticklabel_format(style='plain')
st.pyplot(fig6)


st.write("##")
st.header("Scatter Plot of Predicted Market Values vs Residuals ")
residuals_rfg = result['Market Value'] - result['Predicted Market Value']

# Plot residuals
fig7 = plt.figure(figsize=(10, 6))
plt.scatter(result['Predicted Market Value'], residuals_rfg, color='blue', edgecolor='k', alpha=0.7)
plt.axhline(y=0, color='red', linestyle='--')
plt.xlabel('Predicted Market Value (in millions)')
plt.ylabel('Residuals (in millions)')
plt.title('Residuals vs. Predicted Market Value')

plt.gcf().axes[0].yaxis.get_major_formatter().set_scientific(False)
plt.gcf().axes[0].xaxis.get_major_formatter().set_scientific(False)

plt.grid(True)
st.pyplot(fig7)


