from os import close
import numpy as np
import matplotlib.pyplot as plt
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader

train_size = 10000
test_size = 100
x_train = np.random.rand(train_size)*10
y_train = np.random.rand() * x_train**2 + np.random.rand() * x_train + np.random.rand(train_size)
x_test = np.random.rand(test_size)*10
y_test = np.random.rand() * x_test**2 + np.random.rand() * x_test + np.random.rand(test_size)
plt.figure()
plt.plot(x_test, y_test, 'b.')

class Mydataset(Dataset):
    def __init__(self, x, y) -> None:
        super().__init__()
        self.x = x
        self.y = y
    
    def __getitem__(self, index):
        return np.array(self.x[index], dtype=np.float32).reshape(-1), np.array(self.y[index], dtype=np.float32)
    
    def __len__(self):
        return len(self.x)

ds = Mydataset(x_train, y_train)
dl = DataLoader(ds, batch_size=100)
for x, y in dl:
    print(x.shape, y.shape)
    break


class Mymodel(nn.Module):
    def __init__(self) -> None:
        super().__init__()
        self.nns = nn.Sequential(
            nn.Linear(1, 32),
            nn.ReLU(),
            nn.Linear(32, 1)
        )
    def forward(self, x):
        return self.nns(x)
model = Mymodel()
with torch.no_grad():
    y_test = model(torch.tensor(x_test).unsqueeze(1).to(torch.float))
y_test = y_test.numpy()
plt.plot(x_test, y_test, 'r.')

loss_fn = nn.MSELoss()
optimizer = optim.Adam(model.parameters())
epochs = 50
for i in range(epochs):
    for x, y in dl:
        y_pred = model(x)
        loss = loss_fn(y_pred, y)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    if i % 10==0:
        print(loss)

with torch.no_grad():
    y_test = model(torch.tensor(x_test).unsqueeze(1).to(torch.float))
y_test = y_test.numpy()
plt.plot(x_test, y_test, 'g.')
plt.show()