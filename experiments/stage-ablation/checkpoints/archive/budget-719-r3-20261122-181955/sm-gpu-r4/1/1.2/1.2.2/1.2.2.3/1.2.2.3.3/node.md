# N458: INT8 KV Cache 相比 BF16 KV Cache 的精度损失量化：在 MMLU 基准测试中，Qwen3-27B 使用 INT8 KV Cache 通

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N155

## Claim

INT8 KV Cache 相比 BF16 KV Cache 的精度损失量化：在 MMLU 基准测试中，Qwen3-27B 使用 INT8 KV Cache 通常导致 0.5%-1.5% 的准确率下降，需对比 BF16 基准分（如 75.2%）得出具体阈值（如 74.0%-74.9%）。

## Corrected Claim

INT8 KV Cache 相比 BF16 KV Cache 通常会导致一定的精度损失，具体在 MMLU 基准测试中 Qwen3-27B 的准确率下降幅度需参考具体实验数据，一般认为在 0.5%-1.5% 左右，需对比 BF16 基准分得出具体阈值。

## Evidence

[质询]该陈述包含具体的经验性数值（0.5%-1.5% 的精度损失范围、75.2% 的基准分、74.0%-74.9% 的阈值），这些属于特定模型（Qwen3-27B）在特定基准（MMLU）下的实测数据，无法从第一性原理或数学公理推导得出，且缺乏来源支持。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且具体数值无法通过逻辑推导验证）。

## Search Query

Qwen3-27B INT8 KV Cache accuracy loss MMLU benchmark
