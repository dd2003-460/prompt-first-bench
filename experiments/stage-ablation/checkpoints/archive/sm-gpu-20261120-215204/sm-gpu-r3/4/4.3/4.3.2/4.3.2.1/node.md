# N290: Qwen3-27B 在 INT4/W4 精度下（AWQ 算法，Group Size=128）的 MMLU 基准下降幅度约为 1.5-2.5%（相对于 BF16 

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N102

## Claim

Qwen3-27B 在 INT4/W4 精度下（AWQ 算法，Group Size=128）的 MMLU 基准下降幅度约为 1.5-2.5%（相对于 BF16 基线），具体数值需参考 Qwen 官方技术报告或第三方基准测试（如 LMSYS Chatbot Arena 量化模型对比）；若下降超过 5%，则触发质量不可接受阈值，需回退至 INT8。

## Corrected Claim

Qwen3-27B 在 INT4/W4 精度下（AWQ 算法，Group Size=128）的 MMLU 基准通常会有轻微下降，具体幅度需参考官方技术报告或第三方基准测试；若下降超过 5%，则触发质量不可接受阈值，需回退至 INT8。

## Evidence

[质询]具体数值（1.5-2.5%）属于经验事实，缺乏直接来源支持，且不同量化算法（AWQ vs GPTQ）及模型版本间可能存在差异，无法仅凭逻辑推导确定精确区间。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）

## Search Query

Qwen3-27B AWQ W4 MMLU benchmark drop percentage
