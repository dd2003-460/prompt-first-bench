# N14: 量化精度选择对显存占用的线性影响系数：BF16=1.0x, FP8/INT8=0.5x, NVFP4/W4=0.25x，该系数直接决定能否在单卡 24GB/48

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N2

## Claim

量化精度选择对显存占用的线性影响系数：BF16=1.0x, FP8/INT8=0.5x, NVFP4/W4=0.25x，该系数直接决定能否在单卡 24GB/48GB 内驻留 27B 模型

## Corrected Claim

量化精度选择对显存占用的线性影响系数：BF16=1.0x, FP8/INT8=0.5x, NVFP4/W4=0.25x，该系数直接决定能否在单卡 24GB/48GB 内驻留 27B 模型

## Evidence

先验知识/题面给定，逻辑校验通过：BF16(16bit)为基准1.0x，FP8/INT8(8bit)减半为0.5x，NVFP4/W4(4bit)减至四分之一为0.25x，符合位宽与显存占用线性关系的物理事实。
