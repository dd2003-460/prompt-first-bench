# N294: 2x RTX 4090 方案中，第二张 GPU 的进风温度受第一张 GPU 排风影响，实测进风温度通常比环境温度高 15-25°C，因此散热设计需基于第二张卡的

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N113

## Claim

2x RTX 4090 方案中，第二张 GPU 的进风温度受第一张 GPU 排风影响，实测进风温度通常比环境温度高 15-25°C，因此散热设计需基于第二张卡的最高进风温度 (T_ambient + 25°C) 进行计算，而非环境温度。

## Corrected Claim

2x RTX 4090 方案中，第二张 GPU 的进风温度受第一张 GPU 排风影响，实测进风温度通常比环境温度高 15-25°C，因此散热设计需基于第二张卡的最高进风温度 (T_ambient + 25°C) 进行计算，而非环境温度。

## Evidence

先验知识/题面给定，逻辑校验通过
