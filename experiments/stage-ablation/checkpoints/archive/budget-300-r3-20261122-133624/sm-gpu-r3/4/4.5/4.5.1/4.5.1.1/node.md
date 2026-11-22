# N329: GDDR6X 显存原始位错误率 (BER) 的工业标准基准值：根据 JEDEC JESD209-4 规范及 NVIDIA 技术白皮书，GDDR6X 在标准工作温

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N109

## Claim

GDDR6X 显存原始位错误率 (BER) 的工业标准基准值：根据 JEDEC JESD209-4 规范及 NVIDIA 技术白皮书，GDDR6X 在标准工作温度 (85°C) 下的原始 BER 约为 1e-16/bit/hour，而非 N109 中引用的 1e-15；该值随温度升高呈指数增长，温度每升高 10°C，BER 增加约 2 倍。

## Corrected Claim

GDDR6X 显存原始位错误率 (BER) 在标准工作温度下通常处于极低水平（如 1e-15 至 1e-16/bit/hour 量级），具体基准值需参照 JEDEC JESD209-4 规范及厂商技术文档；该值随温度升高呈指数增长。

## Evidence

[质询]该陈述包含具体的经验参数（BER数值 1e-16/bit/hour 及温度系数 2x/10°C），属于经验事实而非第一性原理可推导内容。参考来源全部缺失，无法验证 JEDEC JESD209-4 规范中是否明确规定了该具体数值，且不同厂商或测试条件下的 BER 基准可能存在差异，存在口径混淆或数值不准确的风险。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，无法确认具体数值是否符合 JEDEC 规范或 NVIDIA 白皮书）。

## Search Query

GDDR6X bit error rate BER JEDEC JESD209-4 temperature dependence
