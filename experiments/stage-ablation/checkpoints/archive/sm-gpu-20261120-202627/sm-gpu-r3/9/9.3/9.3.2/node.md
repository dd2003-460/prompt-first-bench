# N440: INT8 AWQ 量化下 Qwen3-27B 在 GSM8K 基准测试上的准确率绝对值及相对于 BF16 基线的下降幅度（Delta_GSM8K_AWQ），用于

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N142

## Claim

INT8 AWQ 量化下 Qwen3-27B 在 GSM8K 基准测试上的准确率绝对值及相对于 BF16 基线的下降幅度（Delta_GSM8K_AWQ），用于计算特定算法下的 QF_GSM8K = Acc_AWQ / Acc_BF16，以验证数学推理任务上的质量保持率。

## Corrected Claim

INT8 AWQ 量化下 Qwen3-27B 在 GSM8K 基准测试上的准确率通常接近 BF16 基线，下降幅度较小（具体数值需查阅官方技术报告或第三方评测数据以确认 QF_GSM8K 的精确值）。

## Evidence

[质询]该陈述涉及特定模型（Qwen3-27B）在特定量化方案（INT8 AWQ）下的具体基准测试数值（GSM8K准确率及Delta），属于经验事实。由于缺乏具体数值，无法验证其量级合理性或具体数值准确性，且不同量化实现或评测设置可能导致结果差异。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源，无法提供直接支持或矛盾证据，依据经验事实排除条款降级）

## Search Query

Qwen3-27B INT8 AWQ GSM8K accuracy benchmark comparison BF16
