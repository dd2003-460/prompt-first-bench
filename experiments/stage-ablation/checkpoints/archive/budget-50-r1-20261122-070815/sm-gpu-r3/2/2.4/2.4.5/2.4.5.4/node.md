# N239: Qwen3-27B 在 W4 (INT4/AWQ) 量化下的 C-Eval 基准测试得分，需查找实测数据，计算相对于 BF16 的下降幅度 (Delta %)，

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N69

## Claim

Qwen3-27B 在 W4 (INT4/AWQ) 量化下的 C-Eval 基准测试得分，需查找实测数据，计算相对于 BF16 的下降幅度 (Delta %)，以验证中文知识能力是否受量化影响更大（通常中文模型在低比特量化下对词表映射更敏感）。

## Corrected Claim

Qwen3-27B 在 W4 (INT4/AWQ) 量化下的 C-Eval 基准测试得分需查找实测数据以计算相对于 BF16 的下降幅度，通常中文模型在低比特量化下对词表映射更敏感，但具体数值需依赖外部实测报告。

## Evidence

[质询]该陈述包含具体的经验性数值（C-Eval得分及Delta %），属于硬件/模型性能指标，无法从第一性原理推导，且检索无可用来源支持具体数值。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

Qwen3-27B INT4 AWQ C-Eval score degradation
