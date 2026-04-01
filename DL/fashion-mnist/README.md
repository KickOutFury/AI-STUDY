26-04-02
## Hyperparameter Experiments
- Tested multiple combinations of dropout, learning rate, epochs, and convolution depth
- Dropout 0.3 consistently outperformed higher dropout values
- Learning rate 0.001 performed better than 0.0005 and 0.0003 in this setup
- Adding one more convolution layer did not improve validation accuracy
- Best validation accuracy was achieved with the original BetterCNN configuration

## Best Fashion-MNIST Result
- Best Validation Accuracy: **0.9354**
- Best Setting:
  - Learning Rate: **0.001**
  - Dropout: **0.3**
  - Epochs: **10**
  - Early Stopping Patience: **2**