# N315: NVIDIA A100 80GB SXM 运行 Qwen3-27B BF16 在 32K 上下文下的理论 Decode TPS 上限 = 2039 GB/s (

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N103

## Claim

NVIDIA A100 80GB SXM 运行 Qwen3-27B BF16 在 32K 上下文下的理论 Decode TPS 上限 = 2039 GB/s (HBM2e 带宽) / (54GB 权重 + 3.86GB KV + 2GB 开销) ≈ 35.4 tokens/s，实际效率系数 η_a100 通常为 0.6-0.8，故预期实测 TPS 为 21.2-28.3 tokens/s [待核验]。

## Corrected Claim

NVIDIA A100 80GB SXM 运行 Qwen3-27B BF16 在 32K 上下文下的理论 Decode TPS 上限约为 34-35 tokens/s（基于 2039 GB/s 带宽及约 60GB 总内存占用估算），实际效率系数 η_a100 通常为 0.6-0.8，故预期实测 TPS 约为 20.4-28.0 tokens/s。

## Evidence

[质询]KV Cache 大小估算可能存在偏差：Qwen3-27B 的具体架构参数（如层数、头数、头维度）未明确给出，3.86GB 的 KV 占用量依赖于具体的模型配置假设，若实际 KV 更大或更小，分母变化将直接影响 TPS 上限计算。 | 先验知识/题面给定，逻辑校验通过：A100 80GB SXM 带宽 2039 GB/s 为公认规格，BF16 权重 54GB 符合 27B 参数规模，算术推导 2039/59.86 ≈ 34.06 与 35.4 存在微小差异（可能源于权重或 KV 估算的细微差别或四舍五入），但量级和逻辑自洽；因无外部来源直接支持具体 KV 数值及最终 TPS 结论，且属于经验性工程估算，依据规则降级。

## Search Query

A100 80GB SXM Qwen3-27B BF16 32k context decode tokens per second benchmark
