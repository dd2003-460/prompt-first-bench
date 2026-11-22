# N137: L40S 48GB 价格约 $8000，显存带宽 864 GB/s，支持 FP8，单卡可运行 FP8 权重 (27GB) + 32K KV Cache，其功耗 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N31

## Claim

L40S 48GB 价格约 $8000，显存带宽 864 GB/s，支持 FP8，单卡可运行 FP8 权重 (27GB) + 32K KV Cache，其功耗 350W 低于 A100，但显存带宽低于 4090，decode 速度可能慢于 4090 INT4 方案，需权衡质量 (FP8 vs INT4) 与速度的取舍

## Corrected Claim

L40S 48GB 价格约 $8000，显存带宽 864 GB/s，支持 FP8，单卡可运行 FP8 权重 (27GB) + 32K KV Cache，其功耗 350W 低于 A100，但显存带宽低于 4090，decode 速度可能慢于 4090 INT4 方案，需权衡质量 (FP8 vs INT4) 与速度的取舍

## Evidence

先验知识/题面给定，逻辑校验通过：L40S 48GB 规格（864 GB/s, 350W, FP8）符合 NVIDIA 官方数据；48GB 显存足以容纳 27GB 权重及 32K KV Cache；带宽低于 4090 (1008 GB/s) 导致 Decode 速度受限符合物理直觉。
