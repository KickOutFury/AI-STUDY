26-04-02
## Fashion-MNIST CNN

### Overview
- Fashion-MNIST dataset을 활용한 이미지 분류 CNN 모델 구현

### Model Architecture
- Conv2d + BatchNorm + ReLU
- MaxPooling
- Dropout
- Fully Connected Layer

### Training Techniques
- Early Stopping (patience=2)
- Model checkpoint (best_model.pth)
- Data augmentation

### Hyperparameter Experiments
- Tested combinations of:
  - Learning rate (0.001, 0.0005, 0.0003)
  - Dropout (0.3, 0.4, 0.5)
  - Epoch (10, 15, 20)
  - Additional Conv layer

### Key Findings
- Dropout 0.3 performed best
- Learning rate 0.001 showed fastest and most stable convergence
- Increasing model depth did not improve performance
- Early Stopping effectively prevented overfitting

### Best Result
- Validation Accuracy: **0.9354**

### Insight
- More complex models do not always guarantee better performance
- Proper balance between model complexity and regularization is critical
- Hyperparameter tuning significantly impacts performance

26-04-04
## Augmentation Experiment
- Applied controlled augmentation with fixed seed and fixed train/validation split
- Used:
  - RandomRotation(8)
  - RandomAffine(translate=(0.08, 0.08))
- Increased patience from 2 to 3 and epochs from 10 to 20
- Best validation accuracy improved from **0.9354** to **0.9364**

## Insight
- Augmentation did not produce a dramatic gain, but showed a small improvement under controlled comparison
- Slightly longer training with patience=3 helped the model reach a better peak
- In this setup, augmentation required more training time to show its benefit

26-04-06
# Fashion-MNIST CNN (Improvement & Experiments)

## Overview
CNN 모델을 기반으로 Fashion-MNIST 데이터셋을 학습하고,  
다양한 실험을 통해 성능을 개선했습니다.

## Goal
- CNN 구조 이해 및 성능 개선
- Regularization 기법 적용
- LR Scheduler 비교 실험
- 모델 일반화 성능 향상

---

## Dataset
- Fashion-MNIST (28x28 grayscale images)
- 10 classes (의류 이미지 분류)

---

## Model Architecture
- Conv2d → BatchNorm → ReLU
- MaxPool2d
- 3 Conv Block
- Fully Connected Layer
- Dropout 적용

---

## Techniques Applied

### 1. Regularization
- Batch Normalization
- Dropout (0.3)

### 2. Data Augmentation
- RandomRotation(8)
- RandomAffine (translation 0.08)
- RandomErasing (p=0.3)

→ 일부 이미지가 가려져도 인식하도록 학습하여 일반화 성능 향상

---

### 3. LR Scheduler Experiments

#### StepLR
- step_size=5, gamma=0.5
- 일정한 간격으로 learning rate 감소

#### ReduceLROnPlateau
- validation 성능 기반으로 learning rate 감소
- mode='max', patience=2~4 실험

---

## Results

### Best Result (StepLR)
- Validation Accuracy: **0.9415**

### ReduceLROnPlateau Result
- Validation Accuracy: **0.9344**

---

## Key Findings

- StepLR이 더 안정적으로 성능을 향상시킴
- ReduceLROnPlateau는 validation accuracy 변동에 민감하게 반응
- LR이 너무 빨리 감소하여 성능이 제한됨

---

## What I Learned

- Learning Rate Scheduler는 모델 성능에 큰 영향을 준다
- "똑똑한" 방법이 항상 더 좋은 것은 아니다
- 실험 기반 비교가 중요하다
- Augmentation + Scheduler 조합이 성능 개선에 핵심적이다

---

## Next Steps

- Augmentation 강도 최적화
- Conv layer 추가 실험
- Confusion Matrix 기반 오분류 분석
- 0.95 accuracy 도전