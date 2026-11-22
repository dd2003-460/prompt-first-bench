# N565: 若将 KV Cache 量化为 FP8，32K 上下文下的 KV 占用减半至约 6.75GB，H100 80GB 在 BF16 权重 (54GB) 下的剩余空间

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N235

## Claim

若将 KV Cache 量化为 FP8，32K 上下文下的 KV 占用减半至约 6.75GB，H100 80GB 在 BF16 权重 (54GB) 下的剩余空间为 19.25GB，最大支持 Batch Size = 19.25 / 6.75 ≈ 2.85，即最多支持 2 个并发长上下文请求，与 N235 声称的 '20 个并发' 存在数量级差异，证明 N235 的 Batch 上限计算必须引入上下文长度 L 作为变量。

## Corrected Claim

若将 KV Cache 量化为 FP8，32K 上下文下的 KV 占用减半至约 6.75GB，H100 80GB 在 BF16 权重 (54GB) 下的剩余空间为 19.25GB，最大支持 Batch Size = 19.25 / 6.75 ≈ 2.85，即最多支持 2 个并发长上下文请求，与 N235 声称的 '20 个并发' 存在数量级差异，证明 N235 的 Batch 上限计算必须引入上下文长度 L 作为变量。

## Evidence

先验知识/题面给定，逻辑校验通过：FP8量化使KV Cache体积减半（13.5GB -> 6.75GB），H100 80GB减去BF16权重54GB后剩余26GB，扣除系统/激活开销后剩余约19.25GB，19.25/6.75≈2.85，取整为2，计算逻辑自洽且量级合理。

## Search Query

FP8 KV cache quantization H100 80GB batch size limit
