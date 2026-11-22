# N278: Qwen3-27B 在 WikiText-103 基准上的 BF16 基准 Perplexity 具体数值：根据 Qwen3 官方技术报告，Qwen3-27B 

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N86

## Claim

Qwen3-27B 在 WikiText-103 基准上的 BF16 基准 Perplexity 具体数值：根据 Qwen3 官方技术报告，Qwen3-27B 在 WikiText-103 上的 Perplexity 为 5.6 (或类似值，需精确核对)。该数值是计算 BF16 与 FP32 差异的基准分母。若 BF16 PPL=5.6，则 0.1% 的差异阈值为 0.0056，即 BF16 PPL 必须 < 5.6056 才能视为与 FP32 无显著差异。

## Corrected Claim

Qwen3-27B 在 WikiText-103 基准上的 BF16 基准 Perplexity 具体数值需查阅 Qwen3 官方技术报告确认（参考值约为 5.6）。该数值是计算 BF16 与 FP32 差异的基准分母。若 BF16 PPL 为 P，则 0.1% 的差异阈值为 0.001*P，即 BF16 PPL 必须 < P * 1.001 才能视为与 FP32 无显著差异。

## Evidence

[质询]具体数值 5.6 属于经验事实（模型基准测试得分），无法从第一性原理推导，且当前无可用来源支持该具体数值的准确性，存在数值偏差风险。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

Qwen3-27B official technical report WikiText-103 perplexity
