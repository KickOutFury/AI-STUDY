26-03-27
# Digit Recognizer (CNN)

## Overview
Kaggle Digit Recognizer 프로젝트로, 손글씨 숫자 이미지를 분류하는 CNN 모델을 구현했습니다.

## Goal
- 이미지 데이터 처리 이해
- CNN 구조 학습
- 딥러닝 전체 학습 흐름 경험

## Dataset
- 28x28 grayscale handwritten digit images
- train.csv / test.csv

## Preprocessing
- `iloc`로 X, y 분리
- 픽셀값 정규화 (`/ 255.0`)
- train / validation 분리
- reshape: `(N, 28, 28)` → `(N, 1, 28, 28)`

## Model Architecture
- Conv2d (1 → 32)
- ReLU
- MaxPool2d
- Conv2d (32 → 64)
- ReLU
- MaxPool2d
- Flatten
- Linear (3136 → 128)
- Linear (128 → 10)

## Training
- Loss: CrossEntropyLoss
- Optimizer: Adam (lr=0.001)
- Epochs: 5

## Result
- Validation Accuracy: ~98.5%

### Kaggle Submission
- Score: **0.98425**
- Rank: **616 / (전체 참가자)**

## What I Learned
- 이미지 데이터는 2D 배열이며 CNN 입력 형태로 변환이 필요하다
- Conv → ReLU → Pool → Linear 구조를 이해했다
- `forward → loss → backward → optimizer` 학습 흐름 이해
- `torch.max(dim=1)`을 통해 예측값을 추출하는 방법 이해

## Key Concepts
- Convolution: 이미지 특징 추출
- ReLU: 비선형성 추가
- MaxPooling: 크기 축소 및 중요한 특징 유지
- Linear Layer: 최종 분류

## Next Step
- CNN 성능 개선 (Dropout, BatchNorm)
- 데이터 증강 (augmentation)
- 더 깊은 모델 설계