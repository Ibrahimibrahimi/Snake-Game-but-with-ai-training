import os
import torch.nn as nn
import torch.nn.functional as Funcs


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
            model_folder_path = './model'
            if not os.path.exists(model_folder_path):
                os.makedirs(model_folder_path)

            file_name = os.path.join(model_folder_path, file_name)
            torch.save(self.state_dict(), file_name)