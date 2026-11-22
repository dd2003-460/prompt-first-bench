# N309: 量化校准样本量 N_cal 对 Q_score 的影响存在阈值效应：当 N_cal < 128 时，Qwen3-27B INT4 的 MMLU 准确率波动标准差

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N95

## Claim

量化校准样本量 N_cal 对 Q_score 的影响存在阈值效应：当 N_cal < 128 时，Qwen3-27B INT4 的 MMLU 准确率波动标准差增大至 ±2.5%，而 N_cal >= 512 时波动收敛至 ±0.5% 以内；因此为保证 Q_score 稳定性，最小推荐校准集大小为 512 条。

## Corrected Claim

量化校准样本量 N_cal 对 Q_score 的影响可能存在阈值效应，通常较大的校准集有助于降低量化误差波动，但具体阈值（如512条）及波动幅度需依据具体模型和量化方法的实验数据确定。

## Evidence

[质询]该陈述包含具体的经验性数值（如阈值128/512、波动标准差±2.5%/±0.5%），属于特定模型（Qwen3-27B）在特定量化方案下的实证结果，无法从第一性原理推导，且缺乏来源支持。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

AWQ quantization calibration dataset size threshold 128 512 samples MMLU accuracy variance LLM
