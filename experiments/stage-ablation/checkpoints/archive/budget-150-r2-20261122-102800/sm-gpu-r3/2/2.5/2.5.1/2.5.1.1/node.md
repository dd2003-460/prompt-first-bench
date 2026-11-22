# N233: 修正 N85 计算错误：Qwen3-27B BF16 权重为 54GB，TP=2 下每卡权重分片应为 27GB（非 N85 隐含的 32.65-2.15-3.5

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N85

## Claim

修正 N85 计算错误：Qwen3-27B BF16 权重为 54GB，TP=2 下每卡权重分片应为 27GB（非 N85 隐含的 32.65-2.15-3.5=27GB，此处确认 27GB 正确，但 N85 结论‘物理不可行’需结合 Offload 修正）；若启用 CPU Offload，可将部分权重（如 8GB）移至内存，每卡显存需求降至 24.65GB，仍超 24GB 上限 0.65GB (2.7%)，需进一步量化或增加卡数。

## Corrected Claim

Qwen3-27B BF16 权重约为 54GB，TP=2 下每卡权重分片约为 27GB；若启用 CPU Offload 移出 8GB 权重，每卡显存需求降至约 24.65GB，若硬件显存上限为 24GB，则仍超出约 0.65GB，需进一步量化或增加卡数。

## Evidence

[质询]Qwen3-27B 的具体参数量及 BF16 权重体积（54GB）属于经验事实，且不同版本或量化方式下数值可能略有差异，缺乏来源直接确认该精确数值；此外，'24GB 上限'的具体硬件型号未指明，存在口径模糊风险。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，无法验证 54GB 权重体积及 24GB 硬件上限的具体对应关系）

## Search Query

Qwen3-27B BF16 weight size GB TP=2 offload memory requirement
