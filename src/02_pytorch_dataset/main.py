from torch.utils.data import DataLoader
from tqdm import tqdm

from data import TrainSet


def forward(x):
    print(x)


if __name__ == '__main__':
    train_set = TrainSet(lambda x: x)
    train_loader = DataLoader(train_set, batch_size=4, shuffle=True)
    for x in tqdm(train_loader):
        forward(x)
