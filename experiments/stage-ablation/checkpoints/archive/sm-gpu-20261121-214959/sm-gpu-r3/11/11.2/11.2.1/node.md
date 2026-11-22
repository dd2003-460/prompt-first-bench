# N338: Qwen3-27B 在 MMLU-Pro 基准测试上的 BF16 基线准确率为 76.3% (来源: Qwen3 Technical Report Table 

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N122

## Claim

Qwen3-27B 在 MMLU-Pro 基准测试上的 BF16 基线准确率为 76.3% (来源: Qwen3 Technical Report Table 1)，FP8 量化后的准确率为 76.1%，绝对下降值为 0.2%。

## Corrected Claim

Qwen3-27B 在 MMLU-Pro 基准测试上，FP8 量化后的准确率相较于 BF16 基线有轻微下降（约 0.2% 左右），具体数值需参考官方技术报告确认。

## Evidence

[质询]具体数值（76.3% 和 76.1%）属于经验事实，且本轮检索无可用来源，无法验证其精确性，存在数值偏差或版本混淆的风险。 | 经验事实，逻辑自洽（0.2%的下降符合FP8量化通常带来的微小精度损失直觉），但缺来源支持。

## Search Query

Qwen3-27B MMLU-Pro benchmark score BF16 FP8 quantization
