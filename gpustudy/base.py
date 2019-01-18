import torch

print(torch)

# gpu 是否可用
print('gpu 是否可用: ' + str(torch.cuda.is_available()))
print('gpu 数量: ' + str(torch.cuda.device_count()))
print('gpu 名字: ' + str(torch.cuda.get_device_name(0)))
print('正在使用的gpu的下标: ' + str(torch.cuda.current_device()))
print('gpu 信息: ' + str(torch.cuda.get_device_properties(0)))
