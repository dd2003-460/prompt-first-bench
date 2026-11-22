# N272: Qwen3-27B INT4 (AWQ) 量化在 HumanEval (Pass@1) 基准测试上的准确率绝对值及相对于 BF16 基线的具体下降百分比 (ΔH

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N87

## Claim

Qwen3-27B INT4 (AWQ) 量化在 HumanEval (Pass@1) 基准测试上的准确率绝对值及相对于 BF16 基线的具体下降百分比 (ΔHumanEval)，需引用官方 AWQ 模型卡或第三方代码评测数据。

## Corrected Claim

Qwen3-27B INT4 (AWQ) 量化在 HumanEval (Pass@1) 基准测试上的准确率通常略低于 BF16 基线，具体下降幅度需参考官方模型卡或第三方评测数据。

## Evidence

[质询]具体数值（绝对准确率及下降百分比）属于经验事实，且不同量化实现（如AWQ vs GPTQ）或评测环境可能导致结果差异，缺乏来源支持无法确认具体数值。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

Qwen3-27B AWQ INT4 HumanEval Pass@1 accuracy
