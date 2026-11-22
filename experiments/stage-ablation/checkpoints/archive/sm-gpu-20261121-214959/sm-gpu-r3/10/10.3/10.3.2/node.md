# N333: Qwen3-27B INT4 (AWQ) 量化后在 TruthfulQA 基准测试上的幻觉率上升至 18.7% (或 17%-20% 区间)，绝对增加 3.5 

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N120

## Claim

Qwen3-27B INT4 (AWQ) 量化后在 TruthfulQA 基准测试上的幻觉率上升至 18.7% (或 17%-20% 区间)，绝对增加 3.5 个百分点，相对增加 23%，该数据需通过对比 BF16 与 INT4 模型在同一提示集上的输出一致性验证。

## Corrected Claim

Qwen3-27B 在 INT4 (AWQ) 量化后，在 TruthfulQA 基准测试上的幻觉率通常会有所上升（例如在 17%-20% 区间或绝对增加约 3-4 个百分点），具体数值需通过对比 BF16 与 INT4 模型在同一提示集上的输出一致性验证。

## Evidence

[质询]具体数值（18.7%、3.5pp、23%）缺乏来源支持，且不同量化方法（AWQ vs GPTQ）及基座模型版本（Qwen3 vs Qwen2.5）可能导致结果差异，存在将特定实验结果泛化为通用事实的风险。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）

## Search Query

Qwen3-27B INT4 AWQ TruthfulQA hallucination rate increase
