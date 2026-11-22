# N68: NVIDIA RTX 3090 单卡运行 Qwen3-27B (INT4) 的 CAPEX 构成：P_gpu ≈ $800 [时效待核] + P_chassis

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N13

## Claim

NVIDIA RTX 3090 单卡运行 Qwen3-27B (INT4) 的 CAPEX 构成：P_gpu ≈ $800 [时效待核] + P_chassis ≈ $200 + P_psu (850W+) ≈ $120 + P_network (无) + P_cooling (风冷) ≈ $50，总计 ≈ $1170。

## Corrected Claim

NVIDIA RTX 3090 单卡运行 Qwen3-27B (INT4) 的 CAPEX 构成：P_gpu ≈ $800 [时效待核] + P_chassis ≈ $200 + P_psu (850W+) ≈ $120 + P_network (无) + P_cooling (风冷) ≈ $50，总计 ≈ $1170。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 3090 单卡运行 27B INT4 模型在显存（24GB > ~14GB）和算力上可行，各组件价格量级符合市场常识，总成本计算逻辑自洽。
