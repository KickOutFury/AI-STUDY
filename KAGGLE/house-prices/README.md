# House Prices Prediction

## Overview
This project focuses on predicting house prices using various machine learning models and improving performance through feature engineering and ensemble techniques.

## Goal
- Understand tabular data preprocessing
- Apply feature engineering techniques
- Compare multiple models
- Improve performance using ensemble methods

## Dataset
- Kaggle House Prices Dataset
- train.csv / test.csv

## Preprocessing
- Handling missing values
- Log transformation: `SalePrice → log1p(SalePrice)`
- Encoding categorical variables
- Aligning train/test features

## Feature Engineering
- TotalSF (Total square footage)
- TotalBathrooms
- HouseAge
- TotalRooms

## Models
- RandomForestRegressor
- Ridge Regression
- Lasso Regression
- LightGBM

## Validation
- Cross-validation used for model comparison
- Evaluation metric: RMSE

## Final Model
- Ensemble (Weighted Average)
  - Lasso: 0.45
  - LightGBM: 0.55

## Results
- Best Kaggle Score: **0.12334**
- Best Rank: **Top 600**

## Key Insights
- Linear models outperformed tree-based models due to effective feature engineering
- Lasso showed the best individual performance
- LightGBM contributed as a complementary model in ensemble
- Model diversity improved ensemble performance

## What I Learned
- Feature engineering is critical in tabular data problems
- Simple models can outperform complex ones with proper preprocessing
- Ensemble methods improve stability and performance
- Model evaluation using cross-validation is essential

## Tech Stack
- Python
- pandas, numpy
- scikit-learn
- LightGBM

## Project Pipeline
1. Data Preprocessing
2. Feature Engineering
3. Model Training
4. Cross Validation
5. Ensemble
6. Submission

## Next Step
- Apply OOF (Out-of-Fold) stacking
- Experiment with advanced ensemble techniques
- Expand to deep learning models

---

## Experiment Log

### 2026-03-22
- Compared Ridge, Lasso, and LightGBM
- Ridge showed best individual performance
- Applied Lasso + LightGBM ensemble
- Score: 0.12629 (Top ~935)

### 2026-03-23
- Fine-tuned ensemble weights
- Best: 0.45 (Lasso) / 0.55 (LGBM)
- Score: 0.12334
- Rank: Top ~600

### 2026-03-24
- Further tuning confirmed optimal ratio
- Observed importance of model diversity