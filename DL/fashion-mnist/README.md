# Fashion-MNIST Classification (PyTorch)

## Overview
This project focuses on improving image classification performance on the Fashion-MNIST dataset using CNN-based architectures.

The goal was not only to build a model, but to iteratively improve performance through experimentation with architecture, augmentation, and training strategies.

---

## Model Architecture
- Deep CNN with multiple Conv-BatchNorm-ReLU blocks
- Channel progression: 1 → 32 → 64 → 128 → 256
- MaxPooling for spatial reduction
- Fully connected classifier (Flatten-based)

---

## Training Strategy
- Optimizer: Adam
- Loss: CrossEntropyLoss
- Scheduler: StepLR (step_size=5, gamma=0.5)
- Early Stopping (patience=5)

---

## Data Augmentation
- RandomRotation (8 → 5 tuned)
- RandomAffine (translation)
- RandomErasing (p=0.3 → 0.2 tuned)

---

## Experiments & Improvements
- Compared Flatten vs Global Average Pooling (GAP)
  - Flatten performed slightly better
- Tuned augmentation strength (rotation, erasing)
- Tuned dropout (0.3 vs 0.25)

---

## Best Result
- Validation Accuracy: **0.9473**
- Best Epoch: ~21

---

## Confusion Matrix Analysis

- Most errors occur between similar upper-body clothing classes:
  - Shirt ↔ T-shirt/top
  - Shirt ↔ Pullover
  - Coat ↔ Pullover

- These classes share similar silhouettes in 28x28 grayscale images,
  making them inherently difficult to distinguish.

- In contrast, classes with distinct shapes (Trouser, Bag, Sandal)
  achieved near-perfect accuracy.

---

## Insight

- The limitation is likely due to dataset characteristics rather than model capacity
- Further improvements may require better data or higher-resolution inputs

---

## Key Takeaways

- Performance improvement comes from systematic experimentation, not a single change
- Stronger augmentation is not always better
- Model architecture, training strategy, and data preprocessing must be balanced

---

## Experiment Log

### Day 1
- Built baseline CNN model
- Implemented basic training loop (Adam + CrossEntropyLoss)
- Achieved initial accuracy ~0.91

---

### Day 2
- Added BatchNorm and deeper Conv layers
- Improved feature extraction capability
- Accuracy improved to ~0.93

---

### Day 3
- Introduced Data Augmentation:
  - RandomRotation
  - RandomAffine
- Accuracy fluctuated but generalization improved

---

### Day 4
- Added RandomErasing (p=0.3)
- Observed regularization effect
- Improved robustness, accuracy ~0.94+

---

### Day 5
- Implemented StepLR scheduler
- Stabilized late-stage training
- Accuracy improved further (~0.945)

---

### Day 6
- Increased model depth (added 128 → 256 channel block)
- Performance improvement confirmed

---

### Day 7
- Compared Flatten vs Global Average Pooling (GAP)
- Flatten showed slightly better performance

---

### Day 8
- Fine-tuned augmentation parameters:
  - RandomErasing (0.3 → 0.2)
  - Rotation (8 → 5)
- Achieved best validation accuracy: **0.9473**

---

### Day 9
- Tuned Dropout (0.3 vs 0.25)
- Confirmed Dropout 0.3 performed better

---

### Final Result
- Best Validation Accuracy: **0.9473**
- Best Epoch: ~21

### Key Improvements
- Scheduler introduction → +0.01
- Augmentation tuning → +0.005
- Architecture depth → +0.005