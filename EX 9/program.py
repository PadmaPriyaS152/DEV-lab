import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# ---------------- Generate Employee Dataset ----------------
np.random.seed(42)
employee_id = range(1, 101)
age = np.random.randint(22, 60, size=100)
gender = np.random.choice(['Male', 'Female'], size=100)
department = np.random.choice(['HR', 'Sales', 'IT', 'Marketing'], size=100)
years_of_experience = np.random.randint(1, 15, size=100)
performance_rating = np.random.randint(1, 6, size=100)  # 1–5 scale
salary = np.random.randint(40000, 120000, size=100)

employee_data = pd.DataFrame({
    'EmployeeID': employee_id,
    'Age': age,
    'Gender': gender,
    'Department': department,
    'YearsOfExperience': years_of_experience,
    'PerformanceRating': performance_rating,
    'Salary': salary
})

# Save dataset
employee_data.to_csv('employee_data.csv', index=False)

# ---------------- Load & Explore ----------------
employee_data = pd.read_csv('employee_data.csv')
print(employee_data.info())
print(employee_data.describe())
print(employee_data.isnull().sum())

# Department distribution
department_distribution = employee_data['Department'].value_counts()
print("\nDepartment Distribution:\n", department_distribution)

# ---------------- Visualizations ----------------
# Age distribution
plt.figure(figsize=(8, 5))
sns.histplot(employee_data['Age'], bins=20, kde=True, color='skyblue')
plt.title('Distribution of Employee Ages')
plt.xlabel('Age')
plt.ylabel('Count')
plt.show()

# Performance by Department
plt.figure(figsize=(8, 5))
sns.boxplot(x='Department', y='PerformanceRating', data=employee_data, palette="Set2")
plt.title('Performance Ratings by Department')
plt.xlabel('Department')
plt.ylabel('Performance Rating')
plt.show()
