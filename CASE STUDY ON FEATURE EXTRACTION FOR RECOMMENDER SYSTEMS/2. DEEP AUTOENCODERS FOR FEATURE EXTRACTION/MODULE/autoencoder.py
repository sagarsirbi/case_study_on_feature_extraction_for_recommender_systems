# import required libraries
import torch
from torch.utils.data import Dataset

# define dataset subclass to load dataset
class modeldata (Dataset):
    def __init__(self, dfX, dfXv):
        self.dfX, self.dfXv = dfX, dfXv
        
    def __len__ (self):
        return self.dfX.shape[0]
    
    def __getitem__ (self, idx):
        return torch.FloatTensor(self.dfX[idx].todense().getA1()),torch.FloatTensor(self.dfXv[idx].todense().getA1())