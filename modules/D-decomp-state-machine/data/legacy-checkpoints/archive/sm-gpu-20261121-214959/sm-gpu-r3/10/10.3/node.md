# N120: INT4 量化对幻觉率 (Hallucination Rate) 的影响：在 TruthfulQA 基准测试中，Qwen3-27B INT4 的幻觉率从 BF1

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N35

## Claim

INT4 量化对幻觉率 (Hallucination Rate) 的影响：在 TruthfulQA 基准测试中，Qwen3-27B INT4 的幻觉率从 BF16 的 15.2% 上升至 18.7%，绝对增加 3.5 个百分点，相对增加 23%，表明 INT4 量化会显著增加模型生成事实性错误的风险，这在医疗/法律场景中不可接受。

## Corrected Claim

INT4 量化通常会导致模型性能轻微下降，在 TruthfulQA 等事实性基准测试中，量化模型的幻觉率可能高于 BF16 基线，但具体增幅需依据特定模型版本的官方评测数据确定。

## Evidence

[质询]具体数值（15.2% 和 18.7%）及特定模型（Qwen3-27B）在 TruthfulQA 上的表现属于经验事实，且 Qwen3 系列目前尚未正式发布或广泛公开该特定基准测试的官方数据，存在数据虚构或张冠李戴的风险。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且具体数值无法从第一性原理推导）。

## Search Query

Qwen3-27B INT4 quantization hallucination rate TruthfulQA
