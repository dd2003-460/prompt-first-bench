# N284: HumanEval 代码生成基准测试中，Qwen3-27B 在 W4 (INT4) 量化下的 Pass@1 通过率与 BF16 基线的差值，以评估极端量化对代码

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N96

## Claim

HumanEval 代码生成基准测试中，Qwen3-27B 在 W4 (INT4) 量化下的 Pass@1 通过率与 BF16 基线的差值，以评估极端量化对代码能力这一高敏感维度的具体影响。

## Corrected Claim

Qwen3-27B 在 W4 (INT4) 量化下的 HumanEval Pass@1 通过率相较于 BF16 基线存在一定程度的下降，具体差值需参考官方技术报告或独立评测数据。

## Evidence

[质询]该陈述涉及特定模型（Qwen3-27B）在特定量化配置（W4 INT4）下的具体性能指标（Pass@1差值），属于经验事实。由于缺乏具体数值，无法验证其量级是否合理（例如，INT4量化通常会导致显著的性能下降，但具体差值需依赖实验数据），且当前无可用来源支持该具体结论。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源）

## Search Query

Qwen3-27B W4 INT4 quantization HumanEval Pass@1 accuracy comparison BF16
