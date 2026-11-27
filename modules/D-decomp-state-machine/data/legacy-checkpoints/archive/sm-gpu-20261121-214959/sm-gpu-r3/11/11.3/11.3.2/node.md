# N342: Qwen3-27B 在 GSM8K (数学推理) 基准测试上的 BF16 基线 Pass@1 为 92.5% (来源: Qwen3 Technical Repo

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N123

## Claim

Qwen3-27B 在 GSM8K (数学推理) 基准测试上的 BF16 基线 Pass@1 为 92.5% (来源: Qwen3 Technical Report Table 1)，FP8 量化后的 Pass@1 为 92.3%，绝对下降值为 0.2% (约 0.2 个测试用例)。

## Corrected Claim

Qwen3-27B 在 GSM8K 基准测试上，FP8 量化后的 Pass@1 相比 BF16 基线有轻微下降（约 0.2%），具体数值需参考官方技术报告确认。

## Evidence

[质询]具体数值（92.5% 和 92.3%）属于经验事实，且检索无可用来源，无法验证具体数值的准确性，存在数值偏差或口径混淆的风险。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

Qwen3-27B GSM8K Pass@1 score BF16 FP8 quantization
