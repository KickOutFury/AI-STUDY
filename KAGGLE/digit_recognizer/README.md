# Digit Recognizer (CNN)

## Overview
Kaggle Digit Recognizer 프로젝트로, 손글씨 숫자 이미지를 분류하는 CNN 모델을 구현하고 성능을 개선했습니다.

## Goal
- 이미지 데이터 전처리 흐름 이해
- CNN 구조 학습
- 모델 성능 개선 과정 경험
- Kaggle 제출을 통한 실전 검증

## Dataset
- 28x28 grayscale handwritten digit images
- train.csv / test.csv

## Preprocessing
- `iloc`를 사용해 X, y 분리
- 픽셀값 정규화 (`/255.0`)
- train / validation split
- reshape: `(N, 28, 28)` → `(N, 1, 28, 28)`

## Model Development
### Baseline CNN
- Conv2d (1 → 32)
- ReLU
- MaxPool2d
- Conv2d (32 → 64)
- ReLU
- MaxPool2d
- Flatten
- Linear (3136 → 128)
- Linear (128 → 10)

### Improved CNN
- Added Batch Normalization
- Added Dropout
- Applied Early Stopping
- Saved best model checkpoint
- Applied Data Augmentation
  - `RandomRotation(10)`
  - `RandomAffine(translate=(0.1, 0.1))`

## Training
- Loss: CrossEntropyLoss
- Optimizer: Adam (`lr=0.001`)
- Early Stopping with patience tuning
- Model checkpoint saving

## Results
- Best Validation Accuracy: **0.9915**
- Best Kaggle Score: **0.98975**
- Best Kaggle Rank: **433**

## Improvement History
- Baseline CNN: **0.98425** / Rank **616**
- BatchNorm + Dropout: **0.98603** / Rank **582**
- Early Stopping: **0.98871** / Rank **485**
- Data Augmentation: **0.98975** / Rank **433**

## What I Learned
- 이미지 데이터는 숫자 배열이며 CNN 입력 형태로 변환해야 한다
- `forward → loss → backward → optimizer step` 학습 흐름을 이해했다
- BatchNorm과 Dropout이 학습 안정성과 일반화에 도움을 준다는 점을 확인했다
- Early Stopping과 checkpoint 저장이 실제 성능 개선에 중요하다는 점을 배웠다
- Data augmentation이 Kaggle 점수 향상에 효과적이라는 것을 확인했다

## Tech Stack
- Python
- PyTorch
- torchvision
- pandas
- matplotlib

## Next Step
- 더 복잡한 이미지 분류 프로젝트 진행
- CNN 구조 확장 및 추가 실험
- 이후 LLM / RAG 학습으로 확장

## Experiment Log

### 26-03-27
- Baseline CNN implemented
- Kaggle Score: 0.98425
- Rank: 616

### 26-03-28
- Added BatchNorm and Dropout
- Kaggle Score: 0.98603
- Rank: 582

### 26-03-29
- Added Early Stopping and checkpoint
- Tuned patience to 2
- Kaggle Score: 0.98871
- Rank: 485

### 26-03-30
- Applied data augmentation
- Best Validation Accuracy: 0.9915
- Kaggle Score: 0.98975
- Rank: 433