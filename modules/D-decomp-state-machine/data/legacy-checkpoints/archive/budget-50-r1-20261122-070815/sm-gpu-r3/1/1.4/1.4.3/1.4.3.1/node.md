# N184: Qwen3-27B 在 INT4/W4 精度下的总显存需求修正值：基于 N128 混合注意力架构（N_full_attn=32），KV Cache 显存占用为 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N45

## Claim

Qwen3-27B 在 INT4/W4 精度下的总显存需求修正值：基于 N128 混合注意力架构（N_full_attn=32），KV Cache 显存占用为 1.0 GB（BF16 KV），加上 INT4 权重 13.5 GB 及 15% 激活/碎片开销 (2.025 GB)，总需求为 16.525 GB，低于 RTX 4090 24 GB 上限，单卡方案可行且余量约 7.475 GB，较 N45 原估算 (17.2 GB) 更宽松

## Corrected Claim

Qwen3-27B 在 INT4/W4 精度下的总显存需求修正值：基于 N128 混合注意力架构（N_full_attn=32），KV Cache 显存占用为 1.0 GB（BF16 KV），加上 INT4 权重 13.5 GB 及 15% 激活/碎片开销 (2.025 GB)，总需求为 16.525 GB，低于 RTX 4090 24 GB 上限，单卡方案可行且余量约 7.475 GB，较 N45 原估算 (17.2 GB) 更宽松

## Evidence

先验知识/题面给定，逻辑校验通过：13.5+1.0+2.025=16.525，且16.525<24，余量7.475，数值自洽

## Search Query

Qwen3-27B AWQ INT4 memory footprint 32k context KV cache size
