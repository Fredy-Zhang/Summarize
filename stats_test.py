import torch
import torch.nn as nn
from utils.statistic import analyze_model


class MyModel(nn.Module):
    def __init__(self):
        super(MyModel, self).__init__()
        self.conv1 = nn.Conv2d(1, 20, 5)
        self.conv2 = nn.Conv2d(20, 50, 5)
        self.fc1 = nn.Linear(50 * 4 * 4, 500)
        self.fc2 = nn.Linear(500, 10)

    def forward(self, x):
        x = torch.relu(self.conv1(x))
        x = torch.max_pool2d(x, 2, 2)
        x = torch.relu(self.conv2(x))
        x = torch.max_pool2d(x, 2, 2)
        x = x.view(-1, 50 * 4 * 4)
        x = torch.relu(self.fc1(x))
        x = self.fc2(x)
        return x


@analyze_model("cnn.log")
def train_step(model, input_tensor):
    # Dummy training logic (simply calls the forward pass)
    output = model(input_tensor)
    print("Output shape:", output.shape)


if __name__ == "__main__":
    # Example usage
    model = MyModel()
    input_tensor = torch.randn(1, 1, 28, 28)  # Example input
    train_step(model=model, input_tensor=input_tensor)
