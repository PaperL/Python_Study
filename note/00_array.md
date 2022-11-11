# array

## tensor

```python
# code.shape = (16, 16, 1, 1)
# target.shape = (16, 16, 256, 256)
target = code.expand(-1, -1, 256, 256)
```

```python
# mask.shape = (16, 1, 256, 256)
# img.shape = (16, 3, 256, 256)
input_tensor = torch.cat((mask, img), dim=1)
```

## np.array

```python
# n = 32
# np_array.shape = [32, 64, 3]
np_array = np_array.reshape(n, -1)
# np_array.shape = [32, 192]
```

