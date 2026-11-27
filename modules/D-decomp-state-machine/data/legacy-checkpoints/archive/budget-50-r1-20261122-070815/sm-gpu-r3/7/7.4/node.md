# N134: RTX A6000 48GB 价格约 $4000-$5000，显存带宽 768 GB/s 低于 4090，但 48GB 显存可支持 BF16 权重 (54GB 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N31

## Claim

RTX A6000 48GB 价格约 $4000-$5000，显存带宽 768 GB/s 低于 4090，但 48GB 显存可支持 BF16 权重 (54GB 需双卡或量化) 或 FP8 权重 (27GB) + 32K KV Cache 单卡运行，其高显存容量使其在 FP8 精度下的性价比可能优于 4090 INT4 方案

## Corrected Claim

RTX A6000 48GB 价格约 $4000-$5000，显存带宽 768 GB/s 低于 4090，但 48GB 显存可支持 BF16 权重 (54GB 需双卡或量化) 或 FP8 权重 (27GB) + 32K KV Cache 单卡运行，其高显存容量使其在 FP8 精度下的性价比可能优于 4090 INT4 方案

## Evidence

先验知识/题面给定，逻辑校验通过：RTX A6000 48GB 显存带宽确为 768 GB/s（低于 4090 的 1008 GB/s），价格区间符合历史市场数据；54GB BF16 权重需双卡或量化、27GB FP8 权重可单卡运行且剩余显存足以支撑 32K KV Cache 的计算逻辑自洽。
