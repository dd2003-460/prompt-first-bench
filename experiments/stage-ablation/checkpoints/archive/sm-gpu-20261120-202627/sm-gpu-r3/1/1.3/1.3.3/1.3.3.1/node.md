# N182: FP8/INT8 精度下 32K 上下文 KV Cache 显存占用精确计算：若 KV Cache 保持 BF16（常见做法，因量化 KV 易导致精度损失），占

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N43

## Claim

FP8/INT8 精度下 32K 上下文 KV Cache 显存占用精确计算：若 KV Cache 保持 BF16（常见做法，因量化 KV 易导致精度损失），占用同 N153 = 8.59 GB (GQA)。若 KV Cache 也量化为 INT8/FP8，占用减半 = 4.3 GB。通常推荐 KV Cache 保留 BF16，故取 8.59 GB。

## Corrected Claim

FP8/INT8 精度下 32K 上下文 KV Cache 显存占用精确计算：若 KV Cache 保持 BF16（常见做法，因量化 KV 易导致精度损失），占用同 N153 = 8.59 GB (GQA)。若 KV Cache 也量化为 INT8/FP8，占用减半 = 4.3 GB。通常推荐 KV Cache 保留 BF16，故取 8.59 GB。

## Evidence

先验知识/题面给定，逻辑校验通过：KV Cache 显存占用与精度线性相关，BF16 减半为 INT8/FP8 符合基本算术逻辑，且 8.59GB 与 4.3GB 的数值关系自洽。

## Search Query

KV cache quantization INT8 FP8 accuracy impact LLM
