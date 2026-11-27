# N414: 精度敏感性阈值量化：当 Qwen3-27B 的 MMLU 准确率下降超过 3% 或 WikiText2 PPL 增加超过 5% 时，性价比得分 Score 下降

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

精度敏感性阈值量化：当 Qwen3-27B 的 MMLU 准确率下降超过 3% 或 WikiText2 PPL 增加超过 5% 时，性价比得分 Score 下降幅度超过硬件成本节省带来的增益，此时应放弃低精度方案（如 W4）选择高精度方案（如 INT8/BF16），尽管 TCO 增加 20-30%

## Corrected Claim

精度敏感性阈值量化：当 Qwen3-27B 的 MMLU 准确率下降超过 3% 或 WikiText2 PPL 增加超过 5% 时，性价比得分 Score 下降幅度超过硬件成本节省带来的增益，此时应放弃低精度方案（如 W4）选择高精度方案（如 INT8/BF16），尽管 TCO 增加 20-30%

## Evidence

检索失败: no sources from any channel (all 5 failed)
