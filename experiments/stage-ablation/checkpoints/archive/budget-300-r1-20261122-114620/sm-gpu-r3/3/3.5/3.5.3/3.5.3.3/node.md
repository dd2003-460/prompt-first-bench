# N311: 误判风险量化：若未修正阈值，在 32K 上下文下使用 INT8 量化，实际 Acc_drop 为 4.5%，而短文本基准显示 2.5%，导致误判概率 P_mis

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N100

## Claim

误判风险量化：若未修正阈值，在 32K 上下文下使用 INT8 量化，实际 Acc_drop 为 4.5%，而短文本基准显示 2.5%，导致误判概率 P_misjudge = P(Acc_drop_short < 3% | Acc_drop_long > 5%)，需基于历史量化实验分布计算该条件概率。

## Corrected Claim

误判风险量化：若未修正阈值，在长上下文（如 32K）下使用 INT8 量化，实际精度下降（Acc_drop）通常高于短文本基准，导致基于短文本基准设定的阈值可能失效，需基于历史量化实验分布计算条件概率以评估误判风险。

## Evidence

[质询]该陈述包含具体的经验数值（Acc_drop 4.5% 和 2.5%）以及特定的条件概率定义，这些属于经验事实而非第一性原理可推导内容，且缺乏来源支持以验证其准确性或通用性。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

LLM quantization short vs long context benchmark discrepancy misjudgment probability
