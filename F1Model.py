import pandas as pd
from sklearn.model_selection import train_test_split  # split
from sklearn.linear_model import LogisticRegression  # build
from sklearn.metrics import accuracy_score, classification_report  # evaluate
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import ConfusionMatrixDisplay

merged = pd.read_csv("AllData/f1_merged_cleaned.csv")
merged = merged.dropna(subset=['points', 'championship_position'])
# Feature: qualifying_position (X)
X = merged[['qualifying_position', 'year', 'championship_position']]
# Target: podium_finish (Y)
y = merged['podium_finish']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

model = LogisticRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

# Accuracy score
print("Accuracy:", accuracy_score(y_test, y_pred))

# evaluation
print(classification_report(y_test, y_pred))

print("Coefficient:", model.coef_)
print("Intercept:", model.intercept_)

''' plotting next'''
# Get feature importance (coefficient values)
coefficients = model.coef_[0]
features = X.columns  # this is just ['qualifying_position']

# Create a DataFrame for visualization
feature_importance = pd.DataFrame({
    'Feature': features,
    'Importance': coefficients
}).sort_values(by='Importance', ascending=False)

# testing correlation for positionOrder and championship_position
sns.heatmap(X.corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Matrix")
plt.show()

# decision tree
rf = RandomForestClassifier(random_state=42)
rf.fit(X_train, y_train)
rf_pred = rf.predict(X_test)
print("RF Accuracy:", accuracy_score(y_test, rf_pred))

# Plot the importance
plt.barh(feature_importance['Feature'], feature_importance['Importance'])
plt.xlabel('Importance')
plt.title('Feature Importance from Logistic Regression')
plt.show()

# Plotting podium percentages
grouped = merged.groupby('qualifying_position')['podium_finish'].mean()
grouped = grouped * 100
plt.figure(figsize=(10, 6))
grouped.plot(kind='bar')
plt.xlabel('Qualifying Position')
plt.ylabel('Podium Rate (%)')
plt.title('Podium Finish Rate by Qualifying Position')
plt.xticks(rotation=0)
plt.grid(axis='y')
plt.tight_layout()
plt.show()

ConfusionMatrixDisplay.from_estimator(model, X_test, y_test)
plt.title("Confusion Matrix")
plt.show()



# Optional: create some helpful derived columns
merged['starting_grid_diff'] = merged['qualifying_position'] - merged['positionOrder']

# Save a cleaned CSV for Tableau
tableau_df = merged[[
    'raceId', 'driverId', 'year', 'qualifying_position', 'positionOrder',
    'championship_position', 'podium_finish', 'starting_grid_diff'
]]

tableau_df.to_csv("f1_for_tableau.csv", index=False)