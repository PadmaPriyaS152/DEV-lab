import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ----------------- Generate Synthetic Wine Dataset -----------------
np.random.seed(42)
data = {
    'fixed acidity': np.random.uniform(5, 15, 100),
    'volatile acidity': np.random.uniform(0.1, 1.5, 100),
    'citric acid': np.random.uniform(0, 1, 100),
    'residual sugar': np.random.uniform(0, 10, 100),
    'alcohol': np.random.uniform(8, 15, 100),
    'quality': np.random.randint(1, 11, 100)  # quality scale 1–10
}

wine_df = pd.DataFrame(data)
wine_df.to_csv('wine_quality_dataset.csv', index=False)

# ----------------- Load Dataset -----------------
wine_df = pd.read_csv('wine_quality_dataset.csv')
print(wine_df.info())
print(wine_df.describe())
print(wine_df.isnull().sum())

# ----------------- Distribution of Wine Quality -----------------
plt.figure(figsize=(8, 5))
sns.countplot(x='quality', data=wine_df, palette="viridis")
plt.title('Distribution of Wine Quality')
plt.show()

# ----------------- Correlation Heatmap -----------------
correlation_matrix = wine_df.corr(numeric_only=True)
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Matrix')
plt.show()

# ----------------- Pairplot -----------------
selected_features = ['alcohol', 'volatile acidity', 'citric acid', 'residual sugar', 'quality']
pairplot = sns.pairplot(wine_df[selected_features], hue='quality', palette="husl")
pairplot.fig.suptitle('Pairplot of Selected Features', y=1.02)
plt.show()

# ----------------- Boxplot -----------------
plt.figure(figsize=(10, 6))
sns.boxplot(x='quality', y='alcohol', data=wine_df, palette="Set2")
plt.title('Boxplot of Alcohol Content by Wine Quality')
plt.show()
