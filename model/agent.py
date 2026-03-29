import os
import random
import torch
import torch.nn as nn
import torch.nn.functional as Funcs
import torch.optim as optim
from collections import deque # deque = double ended queque
from main import redrawWindow

# define constants
MAX_MEMORY = 100_000 # 100_000 elements
BATCH_SIZE = 1000
LR = 0.001


class Qnet(nn.Module) :
    def __init__(self,input_size,hidden_size ,output_size):
        super().__init__()
        # nns
        self.l1 = nn.Linear(input_size,hidden_size)
        self.l2 = nn.Linear(hidden_size,output_size)
    def forward(self,x):
        x = Funcs.relu(self.l1(x))
        x = self.l2(x)
        return x
    def save(self, file_name='model.pth'):
            model_folder_path = './saved'
            if not os.path.exists(model_folder_path):
                os.makedirs(model_folder_path)

            file_name = os.path.join(model_folder_path, file_name)
            torch.save(self.state_dict(), file_name)
    
class QTrainer :
    def __init__(self,model,lr,gamma):
        self.lr = lr
        self.model = model
        self.gamma = gamma
        
        # optimiser
        self.optimizer = optim.Adam(model.parameters() , lr=self.lr)
        self.criterion = nn.MSELoss()
    