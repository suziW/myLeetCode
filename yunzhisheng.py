from __future__ import with_statement
import numpy as np
from numpy.testing._private.utils import rand
import torch
from torch import nn
import torch.nn.functional as F
import matplotlib.pyplot as plt

dim = 1000
x = np.random.rand(dim)*10
a = 2.4
b = 1.7
c = 4.6
y = a*x**2 + b*x + c + np.random.rand(dim)
plt.figure()
plt.plot(x, y, 'b.')

zipped = zip(x, y)
print(next(zipped))

class Model(nn.Module):
    def __init__(self) -> None:
        super().__init__()
        self.layer1 = nn.Linear(1, 32)
        self.layer2 = nn.Linear(32, 1)

    def forward(self, x):
        x = self.layer1(x)
        x = F.relu(x)
        x = self.layer2(x)
        return x

model = Model()
loss_fn = nn.MSELoss()
opt_fn = torch.optim.Adam(model.parameters())
print(model)

x_test = np.random.rand(dim)*10
with torch.no_grad():
    y_test = model(torch.tensor(x_test).unsqueeze(1).to(torch.float))
plt.plot(x_test, y_test.squeeze().numpy(), 'r.')

epochs = 10000
x_input = torch.tensor(x).unsqueeze(1).to(torch.float)
y_input = torch.tensor(y).unsqueeze(1).to(torch.float)
for i in range(epochs):
    y_pred = model(x_input)
    loss = loss_fn(y_pred, y_input)
    if i % (epochs//10) == 0:
        print(loss)
    opt_fn.zero_grad()
    loss.backward()
    opt_fn.step()

with torch.no_grad():
    y_test = model(torch.tensor(x_test).unsqueeze(1).to(torch.float))
plt.plot(x_test, y_test.squeeze().numpy(), 'g.')
plt.show()