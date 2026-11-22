# N398: 在 32K 上下文长度下，Qwen3-27B 使用 FP8 量化 KV Cache 时的下游任务准确率 (如 LongBench 或 RULER 基准) 与 2

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N127

## Claim

在 32K 上下文长度下，Qwen3-27B 使用 FP8 量化 KV Cache 时的下游任务准确率 (如 LongBench 或 RULER 基准) 与 2K 上下文长度下的准确率差异，用于验证长文本生成质量是否随序列长度线性或非线性下降。

## Corrected Claim

在 32K 上下文长度下，Qwen3-27B 使用 FP8 量化 KV Cache 时的下游任务准确率与 2K 上下文长度下的准确率存在差异，具体数值需参考官方基准测试报告。

## Evidence

[质询]该陈述包含具体的经验性数值对比（32K vs 2K 上下文下的准确率差异），属于硬件/模型性能经验事实，无法从第一性原理推导，且当前无可用来源支持具体数值或趋势。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

LongBench RULER FP8 KV cache accuracy drop long context 32k vs 2k
