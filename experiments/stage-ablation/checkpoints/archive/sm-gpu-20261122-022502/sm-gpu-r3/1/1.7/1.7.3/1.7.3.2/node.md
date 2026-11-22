# N163: 长尾 Token 预测平滑度的量化指标：计算 BF16 与 INT8 模型在 Top-1 预测中，概率质量从头部 Token 向长尾 Token 迁移的比例（S

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N52

## Claim

长尾 Token 预测平滑度的量化指标：计算 BF16 与 INT8 模型在 Top-1 预测中，概率质量从头部 Token 向长尾 Token 迁移的比例（Shift Ratio），公式为 (Sum(P_INT8[long_tail]) - Sum(P_BF16[long_tail])) / Sum(P_BF16[long_tail])，需通过导出 Logits 进行实证计算。

## Corrected Claim

长尾 Token 预测平滑度的量化指标可定义为：计算 BF16 与 INT8 模型在 Top-1 预测中，概率质量从头部 Token 向长尾 Token 迁移的比例（Shift Ratio），公式为 (Sum(P_INT8[long_tail]) - Sum(P_BF16[long_tail])) / Sum(P_BF16[long_tail])，其中 long_tail 需明确定义（如非 Top-K Token），需通过导出 Logits 进行实证计算。

## Evidence

[质询]该陈述定义了一个具体的量化指标（Shift Ratio）及其计算公式，属于经验性/方法论层面的定义，无法从第一性原理或数学公理中严格推导出来。此外，'长尾 Token'的具体定义（如 Top-K 之外的部分）未在公式中明确界定，存在口径模糊的风险。 | 经验事实/方法论定义，逻辑自洽（分子分母量纲一致，比例计算合理），但检索无可用来源支持，且不属于第一性原理可推导范畴，故降级。

## Search Query

LLM quantization long tail token probability distribution shift logits analysis
