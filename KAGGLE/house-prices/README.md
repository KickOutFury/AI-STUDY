26-03-22
### Ensemble Strategy Update

- Compared Ridge, Lasso, and LightGBM models
- Ridge showed best individual performance
- Applied ensemble using Lasso + LightGBM
- Achieved Kaggle score: 0.12629 (Top ~935)

### Insight

- Linear models performed better due to feature engineering and log transformation
- Ensemble improved stability and overall performance

26-03-23
### Ensemble Optimization

- Fine-tuned ensemble weights between Lasso and LightGBM
- Best result achieved at 0.45(Lasso) / 0.55(LGBM)
- Final Score: 0.12334
- Ranking: Top ~600

### Insight

- Lasso showed the best individual Performance
- LightGBM contributed to ensemble diversity
- Fine weight tuning significantly improved ranking

26-03-24
- Fine-tuned ensemble weights between Lasso and LightGBM
- Optimal ratio found near 0.45 (Lasso) / 0.55 (LGBM)
- Observed that model diversity significantly impacts performance

26-03-26
# House Prices Prediction

## Overview
Kaggle House Prices 프로젝트로, 주택 가격을 예측하는 머신러닝 모델을 만들었습니다.

## Goal
- 데이터 전처리
- Feature Engineering
- 여러 모델 비교
- 앙상블을 통해 성능 개선

## Dataset
- train.csv
- test.csv
- Kaggle House Prices dataset

## Preprocessing
- 결측치 처리
- 로그 변환: `SalePrice -> log1p(SalePrice)`
- 범주형 변수 인코딩
- feature alignment

## Feature Engineering
- TotalSF
- TotalBathrooms
- HouseAge
- TotalRooms

## Models
- RandomForestRegressor
- Ridge
- Lasso
- LightGBM

## Validation
- Cross Validation 사용
- RMSE 기준으로 모델 비교

## Best Result
- Best Kaggle Score: `0.12334`
- Best Rank: `609`

## Key Insight
- 선형 모델이 예상보다 강력했다
- Lasso가 가장 좋은 단일 모델이었다
- LGBM은 단독 성능보다 앙상블 보조 모델로 더 유용했다
- 모델 다양성이 앙상블 성능에 중요했다

## Next Step
- OOF Stacking 적용
- 딥러닝 프로젝트(Digit Recognizer) 시작

## Model Pipeline
1. Data Preprocessing
2. Feature Engineering
3. Model Training (Lasso, Ridge, LGBM)
4. Ensemble (Weighted Average)

## Final Model
- Lasso (0.45)
- LightGBM (0.55)

## Result
- Public Score: 0.12334
- Rank: Top 600

## What I Learned
- Feature engineering is critical in tabular data
- Linear models can outperform tree models
- Ensemble improves stability and performance