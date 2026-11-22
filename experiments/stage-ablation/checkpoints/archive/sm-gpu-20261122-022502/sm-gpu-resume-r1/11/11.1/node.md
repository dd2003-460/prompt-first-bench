# N121: FP8 (E4M3) 量化导致的 Perplexity (PPL) 增加量在 Qwen3-27B 上的具体数值为 0.3% - 0.8% (基于 WikiTex

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N36

## Claim

FP8 (E4M3) 量化导致的 Perplexity (PPL) 增加量在 Qwen3-27B 上的具体数值为 0.3% - 0.8% (基于 WikiText-2 或 C4 数据集)，该数值低于 BF16 到 INT4 的 PPL 增加量 (通常 >2-5%)，确立了 FP8 作为'近无损'基线的量化事实。

## Corrected Claim

FP8 (E4M3) 量化导致的 Perplexity (PPL) 增加量通常显著低于 BF16 到 INT4 的 PPL 增加量，确立了 FP8 作为'近无损'基线的量化事实。

## Evidence

[质询]具体数值范围（0.3%-0.8%）及对比基准（INT4 >2-5%）属于特定模型（Qwen3-27B）在特定数据集上的经验测量结果，无法从第一性原理推导，且缺乏来源支持以确认其精确量级。 | 经验事实，逻辑自洽（FP8精度高于INT4，PPL损失理应更小）但缺来源支持，无法验证具体数值区间。

## Search Query

Qwen3-27B FP8 E4M3 quantization perplexity increase WikiText-2 C4 benchmark results
