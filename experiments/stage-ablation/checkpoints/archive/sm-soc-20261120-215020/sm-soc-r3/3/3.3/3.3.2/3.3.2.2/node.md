# N142: GMV 贡献占比 $G_{share}$ 需按成交概率加权计算：$G_{share} = \frac{\int_{0.02}^{\infty} P(\text{

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N49

## Claim

GMV 贡献占比 $G_{share}$ 需按成交概率加权计算：$G_{share} = \frac{\int_{0.02}^{\infty} P(\text{Sale}|\delta) \times V(\delta) \times f(\delta) d\delta}{\int_{0}^{\infty} P(\text{Sale}|\delta) \times V(\delta) \times f(\delta) d\delta}$，其中 $P(\text{Sale}|\delta)$ 为条件成交概率。

## Corrected Claim

GMV 贡献占比 $G_{share}$ 需按成交概率加权计算：$G_{share} = \frac{\int_{0.02}^{\infty} P(\text{Sale}|\delta) \times V(\delta) \times f(\delta) d\delta}{\int_{0}^{\infty} P(\text{Sale}|\delta) \times V(\delta) \times f(\delta) d\delta}$，其中 $P(\text{Sale}|\delta)$ 为条件成交概率。

## Evidence

先验知识/题面给定，逻辑校验通过：GMV贡献占比定义为特定区间GMV期望值与总GMV期望值之比，公式中分子分母均包含成交概率、价值及分布密度，量纲与逻辑自洽。
