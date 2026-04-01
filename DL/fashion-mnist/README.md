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