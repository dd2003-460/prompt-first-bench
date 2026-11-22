# N6: 模型权重显存占用量 = 27B * 2 bytes (BF16) = 54GB; 27B * 1 byte (FP8/INT8) = 27GB; 27B * 0

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1

## Claim

模型权重显存占用量 = 27B * 2 bytes (BF16) = 54GB; 27B * 1 byte (FP8/INT8) = 27GB; 27B * 0.5 bytes (W4/INT4) = 13.5GB

## Corrected Claim

模型权重显存占用量 = 27B * 2 bytes (BF16) = 54GB; 27B * 1 byte (FP8/INT8) = 27GB; 27B * 0.5 bytes (W4/INT4) = 13.5GB

## Evidence

先验知识/题面给定，逻辑校验通过：27B参数在BF16(2字节)、FP8/INT8(1字节)、INT4(0.5字节)下的显存占用计算符合基本算术与数据格式定义。
