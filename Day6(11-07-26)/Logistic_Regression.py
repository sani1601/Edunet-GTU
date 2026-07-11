# --- Applying Classification Algorithm: Logistic Regression ---
print("--- Preparing for Classification: Logistic Regression ---")

# For classification, we need a categorical target variable.
# Let's create a binary target variable from 'RCACScore' by categorizing it.
# For example, we can classify 'RCACScore' as 'High' (e.g., > median) or 'Low' (e.g., <= median).

# Create a binary target 'RCACScore_High' based on the median RCACScore
median_rcac_score = df_bio_encoded['RCACScore'].median()
df_bio_encoded['RCACScore_High'] = (df_bio_encoded['RCACScore'] > median_rcac_score).astype(int)

# Define the new target variable (y_clf) and features (X_clf)
target_variable_clf = 'RCACScore_High'
y_clf = df_bio_encoded[target_variable_clf]
X_clf = df_bio_encoded.drop(columns=[target_variable, target_variable_clf]) # Drop original and new target

# Ensure X_clf only contains numerical features and handle potential inf/NaNs from previous steps
X_clf = X_clf.select_dtypes(include=np.number)
X_clf.replace([np.inf, -np.inf], np.nan, inplace=True)
X_clf.dropna(axis=1, inplace=True) # Drop columns with any remaining NaNs

# Align X_clf and y_clf
X_clf, y_clf = X_clf.align(y_clf, join='inner', axis=0)

print(f"New binary target variable (y_clf): '{target_variable_clf}'")
print(f"Shape of features (X_clf): {X_clf.shape}")
print(f"Shape of target (y_clf): {y_clf.shape}")
print(f"Value counts for the binary target:\n{y_clf.value_counts()}")

print("--- Splitting Data for Classification ---")
X_train_clf, X_test_clf, y_train_clf, y_test_clf = train_test_split(X_clf, y_clf, test_size=0.2, random_state=42, stratify=y_clf)
print(f"Training features shape (classification): {X_train_clf.shape}")
print(f"Testing features shape (classification): {X_test_clf.shape}")
print(f"Training target shape (classification): {y_train_clf.shape}")
print(f"Testing target shape (classification): {y_test_clf.shape}")


from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

print("\n--- Applying Logistic Regression ---")

# Initialize the Logistic Regression model
# Set max_iter for convergence and solver for better performance with large datasets
logistic_model = LogisticRegression(max_iter=1000, random_state=42, solver='liblinear') 

# Train the model
logistic_model.fit(X_train_clf, y_train_clf)
print("Logistic Regression model trained successfully.")

# Make predictions
y_pred_logreg = logistic_model.predict(X_test_clf)

# --- Evaluating the Classification Model ---
print("\n--- Evaluating Logistic Regression Model ---")
accuracy_logreg = accuracy_score(y_test_clf, y_pred_logreg)
classification_rep = classification_report(y_test_clf, y_pred_logreg)
conf_matrix = confusion_matrix(y_test_clf, y_pred_logreg)

print(f"Accuracy: {accuracy_logreg:.4f}")
print("\nClassification Report:\n", classification_rep)
print("\nConfusion Matrix:\n", conf_matrix)

print("\n--- Explanation of Model Error Values (Classification) ---")
print("**Accuracy:**")
print("   - Accuracy is the ratio of correctly predicted observations to the total observations. It's a good measure when the target classes are balanced.")
print("   - Range: 0 to 1 (or 0% to 100%). Higher is better.")

print("\n**Precision:** (from Classification Report)")
print("   - Precision is the ratio of correctly predicted positive observations to the total predicted positive observations. It answers: 'Of all the instances our model predicted as positive, how many were actually positive?'")

print("\n**Recall (Sensitivity):** (from Classification Report)")
print("   - Recall is the ratio of correctly predicted positive observations to all observations in actual class. It answers: 'Of all the actual positive instances, how many did our model correctly identify?'")

print("\n**F1-Score:** (from Classification Report)")
print("   - The F1-Score is the weighted average of Precision and Recall. It tries to find the balance between precision and recall. It's particularly useful when you have an uneven class distribution.")

print("\n**Support:** (from Classification Report)")
print("   - The number of actual occurrences of the class in the specified dataset.")

print("\n**Confusion Matrix:**")
print("   - A table used to describe the performance of a classification model. Each row of the matrix represents the instances in an actual class while each column represents the instances in a predicted class.")
print("   - Top-Left (True Negative): Correctly predicted negative instances.")
print("   - Top-Right (False Positive): Incorrectly predicted positive instances (Type I error).")
print("   - Bottom-Left (False Negative): Incorrectly predicted negative instances (Type II error).")
print("   - Bottom-Right (True Positive): Correctly predicted positive instances.")
