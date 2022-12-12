from torch.utils.data import Dataset


class TrainSet(Dataset):
    def __init__(self, loader):
        self.input_list = [x for x in range(0,100)]
        self.gt_list = [x for x in range(100,200)]
        assert len(self.input_list) == len(self.gt_list)
        self.loader_func = loader

    def __getitem__(self, index):
        return self.loader_func(index)

    def __len__(self):
        return len(self.input_list)
