# N196: Qwen3-27B FP8-E4M3 量化模型在 MT-Bench 上的平均得分为 8.4 分，AlpacaEval 2.0 LC Win Rate 为 54.

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N53

## Claim

Qwen3-27B FP8-E4M3 量化模型在 MT-Bench 上的平均得分为 8.4 分，AlpacaEval 2.0 LC Win Rate 为 54.5%；相对于 BF16 基线，任务通过率下降幅度为 0.5% (55.0% - 54.5%)，满足 < 1% 的可接受阈值，但 ΔPPL 需单独通过困惑度测试验证。

## Corrected Claim

Qwen3-27B FP8-E4M3 量化模型在 MT-Bench 和 AlpacaEval 2.0 上的表现与 BF16 基线相比存在微小差异，任务通过率下降幅度通常小于 1%，具体数值需参考官方技术报告或最新评测数据。

## Evidence

[质询]具体数值（8.4分、54.5%、55.0%）属于特定模型版本的经验事实，缺乏来源支持，且不同量化实现或评测批次可能导致数值波动，无法仅凭逻辑推导确认精确值。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）

## Search Query

Qwen3-27B FP8 quantization MT-Bench score AlpacaEval evaluation results
