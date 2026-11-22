# N368: Qwen3-27B INT8/AWQ 量化模型在 HuggingFace (如 Qwen/Qwen3-27B-Int8-AWQ) 的 README 中报告的 W

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N114

## Claim

Qwen3-27B INT8/AWQ 量化模型在 HuggingFace (如 Qwen/Qwen3-27B-Int8-AWQ) 的 README 中报告的 WikiText-2 困惑度 (PPL) 具体数值，以及对应的 BF16 基线 PPL 数值，用于计算 ΔPPL。

## Corrected Claim

Qwen3-27B INT8/AWQ 量化模型在 HuggingFace 的 README 中报告了 WikiText-2 困惑度 (PPL) 及对应的 BF16 基线 PPL 数值，用于计算 ΔPPL，但具体数值需查阅官方文档确认。

## Evidence

[质询]具体数值属于经验事实，且不同量化实现（如 GPTQ, AWQ, SmoothQuant）及不同评测脚本（如 lm-eval-harness 版本、数据预处理方式）会导致 PPL 数值存在微小差异，无法仅凭逻辑推导确定唯一精确值。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，无法验证具体数值）

## Search Query

Qwen3-27B INT8 AWQ HuggingFace perplexity benchmark WikiText-2
