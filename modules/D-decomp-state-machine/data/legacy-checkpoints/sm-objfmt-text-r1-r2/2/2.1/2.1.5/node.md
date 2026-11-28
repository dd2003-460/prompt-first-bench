# N46: FP8/INT8 精度下模型权重显存占用为 27 GB，加上 32K Context 的 KV Cache (若 KV 也量化为 FP8/INT8，占用减半至 

- **status**: degraded
- **level**: L3
- **source**: calculation
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N13, N14, N15

## Claim

FP8/INT8 精度下模型权重显存占用为 27 GB，加上 32K Context 的 KV Cache (若 KV 也量化为 FP8/INT8，占用减半至 6-9 GB)，总显存需求约为 33-36 GB，因此单张 48GB 显卡 (如 A6000/L40S) 可舒适驻留，而 24GB 显卡 (如 RTX 4090) 需依赖 Offloading 或更激进的 KV 量化

## Corrected Claim

FP8/INT8 精度下模型权重显存占用为 27 GB。对于特定中等规模模型（如 8B-14B 参数级别），加上 32K Context 的 KV Cache（量化后约 6-9 GB），总显存需求约为 33-36 GB，单张 48GB 显卡可舒适驻留；但对于更大规模模型，KV Cache 可能显著增加，24GB 显卡通常需依赖 Offloading 或更激进的量化策略。

## Evidence

[质询]KV Cache 占用估算缺乏具体模型架构参数（如层数、头数、隐藏维度），不同模型（如 Llama-3-8B vs 70B）在 32K 上下文下的 KV Cache 大小差异巨大，6-9 GB 的区间可能不适用于所有声称能装入 48GB 显存的模型（例如大参数量模型即使权重 27GB，KV Cache 也可能远超此范围导致溢出）。 | 经验事实，逻辑自洽但缺来源支持；KV Cache 计算依赖于未指定的模型结构参数，导致数值范围具有不确定性。
