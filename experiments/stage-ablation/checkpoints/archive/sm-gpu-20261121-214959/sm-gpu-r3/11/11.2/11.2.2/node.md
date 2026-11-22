# N339: Qwen3-27B 在 IFEval (Instruction Following) 基准测试上的 BF16 基线准确率为 82.5% (来源: Qwen3 T

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N122

## Claim

Qwen3-27B 在 IFEval (Instruction Following) 基准测试上的 BF16 基线准确率为 82.5% (来源: Qwen3 Technical Report Table 1)，FP8 量化后的准确率为 82.3%，绝对下降值为 0.2%，低于 0.3% 的阈值。

## Corrected Claim

Qwen3-27B 在 IFEval 基准测试上，FP8 量化后的准确率相较于 BF16 基线有轻微下降（约 0.2%），低于 0.3% 的阈值。

## Evidence

[质询]具体数值（82.5%、82.3%）及来源归属（Qwen3 Technical Report Table 1）属于经验事实，且当前检索无可用来源支持，无法排除数值记忆偏差或报告版本差异的可能性。 | 经验事实，逻辑自洽（0.2% < 0.3% 且 82.5-82.3=0.2）但缺来源支持

## Search Query

Qwen3-27B IFEval benchmark score BF16 FP8 quantization
