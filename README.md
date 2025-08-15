# ElevateLabTask8

# K-Means Clustering
##  Task Overview
This project uses **K-Means Clustering** to group customers into different segments based on their data.

##  Steps Performed
1. Load dataset
2. Use Elbow Method to choose best `K`
3. Train K-Means model
4. Assign cluster labels to customers
5. Evaluate with Silhouette Score
6. Visualize results in 2D using PCA


---

##  Interview Q&A
| # | Question | Simple Answer |
|---|----------|---------------|
| 1 | **How does K-Means work?** | It groups points into K clusters by minimizing distance to the cluster center. |
| 2 | **What is the Elbow Method?** | A way to find best K by looking for a bend in the inertia vs. K plot. |
| 3 | **Limitations of K-Means?** | Needs K in advance, sensitive to outliers, assumes clusters are round. |
| 4 | **How does initialization affect results?** | Bad starting points can lead to poor clusters. |
| 5 | **What is inertia?** | Total distance between points and their cluster center. |
| 6 | **What is Silhouette Score?** | A score from -1 to 1 showing how well points fit in their cluster. |
| 7 | **How to choose right K?** | Use Elbow Method, Silhouette Score, or domain knowledge. |
| 8 | **Clustering vs Classification?** | Clustering has no labels (unsupervised), classification uses labels (supervised). |


