26-04-07
# CIFAR-10 Image Classification (CNN)

## Overview
This project implements a Convolutional Neural Network (CNN) using PyTorch to classify images from the CIFAR-10 dataset.

## Dataset
- CIFAR-10
- 60,000 images (32x32 RGB)
- 10 classes

## Model Architecture
- Conv Blocks:
  - Conv → BatchNorm → ReLU
  - MaxPooling for downsampling
- Classifier:
  - Flatten → Linear → ReLU → Dropout → Linear

## Data Augmentation
- RandomHorizontalFlip
- RandomCrop (padding=4)

## Training Setup
- Loss: CrossEntropyLoss
- Optimizer: Adam (lr=0.001)
- Scheduler: StepLR (step_size=10, gamma=0.5)
- Batch size: 128
- Epochs: 3 (initial test)

## Results

| Epoch | Train Loss | Accuracy |
|------|-----------|----------|
| 1 | 1.4879 | 0.5490 |
| 2 | 1.0658 | 0.6164 |
| 3 | 0.9135 | 0.7113 |

## Insight
- Model shows stable learning progression
- Significant performance improvement across epochs
- Indicates strong baseline for further tuning

## Next Steps
- Increase epochs for better convergence
- Apply Global Average Pooling (GAP)
- Add deeper convolution layers (128 → 256)
- Tune augmentation and regularization