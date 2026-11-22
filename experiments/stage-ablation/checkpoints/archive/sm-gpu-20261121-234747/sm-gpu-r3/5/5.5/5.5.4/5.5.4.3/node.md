# N409: W4 量化下 Qwen3-27B 在相同 1000 条 Prompt 集下的平均困惑度 PPL_W4，用于对比 W4 与 FP8 在分布偏移上的差异，验证 W4

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N134, N135, N136

## Claim

W4 量化下 Qwen3-27B 在相同 1000 条 Prompt 集下的平均困惑度 PPL_W4，用于对比 W4 与 FP8 在分布偏移上的差异，验证 W4 是否导致不可接受的长尾分布畸变

## Corrected Claim

W4 量化下 Qwen3-27B 在相同 1000 条 Prompt 集下的平均困惑度 PPL_W4 需通过实际基准测试获取，用于对比 W4 与 FP8 在分布偏移上的差异，以验证 W4 是否导致不可接受的长尾分布畸变。

## Evidence

[质询]该陈述包含具体的经验性数值指标（PPL_W4），属于硬件/模型量化后的具体性能表现，无法从第一性原理推导，且检索无可用来源支持，存在数值不可验证的风险。 | 经验事实，逻辑自洽但缺来源支持（检索失败，无外部证据）

## Search Query

Qwen3-27B W4 AWQ GPTQ perplexity degradation benchmark
