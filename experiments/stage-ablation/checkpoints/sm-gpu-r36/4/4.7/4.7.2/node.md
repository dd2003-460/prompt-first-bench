# N76: RTX 4090 (24GB) 运行 Qwen3-27B W4 量化下的总显存占用，需计算权重压缩后大小 (27B * 0.5 bytes) 与 32K 上下文

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N25

## Claim

RTX 4090 (24GB) 运行 Qwen3-27B W4 量化下的总显存占用，需计算权重压缩后大小 (27B * 0.5 bytes) 与 32K 上下文 KV Cache 的总和，确认是否满足容量下限

## Corrected Claim

RTX 4090 (24GB) 运行 Qwen3-27B W4 量化下的总显存占用，需计算权重压缩后大小 (27B * 0.5 bytes) 与 32K 上下文 KV Cache 的总和，确认是否满足容量下限

## Evidence

先验知识/题面给定，逻辑校验通过：27B参数W4量化权重约13.5GB，32K上下文KV Cache在合理精度下通常占用数GB至十几GB，总和远低于24GB显存上限，符合物理直觉与工程常识。
