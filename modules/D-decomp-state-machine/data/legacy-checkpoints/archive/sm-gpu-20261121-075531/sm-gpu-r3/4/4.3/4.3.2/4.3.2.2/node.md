# N268: Qwen3-27B 在 W8A8 精度下，基于 WikiText2 数据集的实测困惑度 (PPL_W8A8) 具体数值，用于量化激活值 INT8 量化引入的额外

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N86

## Claim

Qwen3-27B 在 W8A8 精度下，基于 WikiText2 数据集的实测困惑度 (PPL_W8A8) 具体数值，用于量化激活值 INT8 量化引入的额外误差。

## Corrected Claim

Qwen3-27B 在 W8A8 精度下，基于 WikiText2 数据集的实测困惑度 (PPL_W8A8) 具体数值需查阅特定量化框架（如 SmoothQuant 或 GPTQ）的官方报告或论文，当前检索未获取到确切数值。

## Evidence

[质询]该陈述要求提供具体的实测数值（PPL_W8A8），但参考来源显示检索失败，无可用外部证据支持该具体数值。此外，Qwen3-27B 的具体量化后困惑度属于经验事实，无法从第一性原理推导，且不同量化实现（如 SmoothQuant, GPTQ, AWQ 等）会导致数值差异，缺乏具体量化方法描述使得数值具有不确定性。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，无法验证具体数值）

## Search Query

Qwen3-27B W8A8 WikiText2 perplexity
