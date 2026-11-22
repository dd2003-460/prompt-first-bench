# N290: Qwen3-27B FP8 (E4M3) 量化模型在 HumanEval 上的 Pass@1 准确率为 63.5%（假设值，需核验），相对 BF16 下降 1.

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N91

## Claim

Qwen3-27B FP8 (E4M3) 量化模型在 HumanEval 上的 Pass@1 准确率为 63.5%（假设值，需核验），相对 BF16 下降 1.5 个百分点（绝对值），满足 N99 定义的 <2 个百分点可接受阈值。

## Corrected Claim

Qwen3-27B FP8 (E4M3) 量化模型在 HumanEval 上的 Pass@1 准确率相对 BF16 下降幅度预计小于 2 个百分点（具体数值需实测验证）。

## Evidence

[质询]该陈述包含具体的经验性数值（63.5% 和 1.5 个百分点），属于特定模型在特定基准上的实测性能数据，无法从第一性原理或数学公理推导得出，且当前无可用外部来源支持。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

Qwen3-27B FP8 E4M3 quantization HumanEval Pass@1 benchmark result
