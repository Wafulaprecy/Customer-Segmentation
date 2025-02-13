# Customer Segmentation Using K-Means Clustering

This project focuses on segmenting mall customers into distinct groups based on their demographic and behavioral data using **K-Means Clustering**. The dataset used is the **Mall Customer Segmentation Dataset**, which includes features like `Age`, `Annual Income`, `Spending Score`, and `Gender`.

## Table of Contents
1. [Project Overview](#project-overview)
2. [Dataset](#dataset)
3. [Steps](#steps)
4. [Installation](#installation)
5. [Usage](#usage)
6. [API Deployment](#api-deployment)
7. [Results](#results)
8. [Contributing](#contributing)
9. [License](#license)

---

## Project Overview
The goal of this project is to group mall customers into clusters based on their:
- **Age**
- **Annual Income**
- **Spending Score**

This segmentation can help the mall management tailor marketing strategies and improve customer satisfaction.

---

## Dataset
The dataset used in this project is the **Mall Customer Segmentation Dataset**, which contains the following columns:
- `CustomerID`: Unique ID for each customer.
- `Gender`: Gender of the customer (Male/Female).
- `Age`: Age of the customer.
- `Annual Income (k$)`: Annual income of the customer in thousands of dollars.
- `Spending Score (1-100)`: A score assigned by the mall based on customer behavior and spending nature.

The dataset can be downloaded from [Kaggle](https://www.kaggle.com/vjchoudhary7/customer-segmentation-tutorial-in-python).

---

## Steps
The project involves the following steps:

### 1. Data Preprocessing
- Dropped the `CustomerID` column as it is not useful for clustering.
- Encoded the `Gender` column using `OneHotEncoder`.
- Scaled the numerical features (`Age`, `Annual Income`, `Spending Score`) using `StandardScaler`.

### 2. Exploratory Data Analysis (EDA)
- Visualized the distribution of features using pairplots and heatmaps.
- Analyzed correlations between features.

### 3. K-Means Clustering
- Used the **Elbow Method** to determine the optimal number of clusters (`k=5`).
- Applied K-Means clustering to segment customers into 5 groups.

### 4. Model Evaluation
- Calculated the **Silhouette Score** to evaluate the quality of clustering.
- Visualized the clusters using scatter plots.

### 5. Dimensionality Reduction (PCA)
- Applied **Principal Component Analysis (PCA)** to reduce the data to 2 dimensions for visualization.
- Plotted the clusters in 2D space to further evaluate the model.

### 6. Pipeline Creation
- Created a **Scikit-learn Pipeline** to automate preprocessing and clustering.
- Saved the pipeline using `joblib` for future use.

### 7. API Deployment
- Deployed the model as a **Flask API** to predict clusters for new data.
