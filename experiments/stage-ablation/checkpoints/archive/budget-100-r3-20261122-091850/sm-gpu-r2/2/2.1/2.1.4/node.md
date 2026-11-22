# N48: Qwen3-27B FP8 量化（E4M3 格式）的实测 Perplexity 增量，计算公式：ΔPPL = PPL_FP8 - PPL_BF16，预期值在 0

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N10, N11, N12

## Claim

Qwen3-27B FP8 量化（E4M3 格式）的实测 Perplexity 增量，计算公式：ΔPPL = PPL_FP8 - PPL_BF16，预期值在 0.05-0.15 之间 [待核验]。

## Corrected Claim

Qwen3-27B FP8 量化（E4M3 格式）的实测 Perplexity 增量（ΔPPL = PPL_FP8 - PPL_BF16）通常较小，具体数值需依据实际基准测试确定，预期在 0.05-0.15 之间仅为参考估计。

## Evidence

[质询]该陈述包含具体的经验数值范围（0.05-0.15），属于经验事实而非第一性原理可推导内容，且缺乏实测数据支持，不同模型或数据集下该增量可能波动较大。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）

## Search Query

Qwen3-27B FP8 E4M3 perplexity degradation benchmark
