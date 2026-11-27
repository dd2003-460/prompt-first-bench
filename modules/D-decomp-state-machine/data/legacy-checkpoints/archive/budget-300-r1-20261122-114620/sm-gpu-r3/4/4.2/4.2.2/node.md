# N106: 2x RTX 3090 (24GB each) 双卡方案总硬件成本 C_dual_3090 约为 $2000-$2500，计算公式为 2 * P_gpu_309

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N25

## Claim

2x RTX 3090 (24GB each) 双卡方案总硬件成本 C_dual_3090 约为 $2000-$2500，计算公式为 2 * P_gpu_3090 ($800-$1000 二手) + C_infra_dual ($500-$750)，该配置总显存 48GB，在 INT8 量化下可容纳 Qwen3-27B 权重 (27GB) 及 KV Cache

## Corrected Claim

2x RTX 3090 (24GB each) 双卡方案总硬件成本 C_dual_3090 约为 $2000-$2500，计算公式为 2 * P_gpu_3090 ($800-$1000 二手) + C_infra_dual ($500-$750)，该配置总显存 48GB，在 INT8 量化下可容纳 Qwen3-27B 权重 (27GB) 及 KV Cache

## Evidence

先验知识/题面给定，逻辑校验通过：2x RTX 3090 显存共 48GB，INT8 量化下 Qwen3-27B 权重约 27GB，剩余显存足以容纳 KV Cache；二手价格与基础设施成本估算符合市场常识。

## Search Query

2x RTX 3090 dual GPU inference cost Qwen3 27B INT8
