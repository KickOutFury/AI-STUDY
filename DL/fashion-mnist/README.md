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
## [DL] RandomErasing + LR Scheduler 비교 실험

- Added RandomErasing augmentation
- Compared StepLR and ReduceLROnPlateau
- StepLR performed better (0.9415)
- Plateau reduced LR too early due to validation fluctuations