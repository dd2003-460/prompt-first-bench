# N10: LFU对长尾冷对象驱逐劣势：长尾对象（bottom 50%）贡献10%请求，LFU因频率低优先驱逐，但Pareto(β=0.9)下长尾请求占比低，劣势量化为 D

- **status**: degraded
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N2

## Claim

LFU对长尾冷对象驱逐劣势：长尾对象（bottom 50%）贡献10%请求，LFU因频率低优先驱逐，但Pareto(β=0.9)下长尾请求占比低，劣势量化为 D_disadvantage ≈ (1 - L_lock) * (1 - 1/β) ≈ 0.48 * 0.111 ≈ 0.053，抵消部分锁定优势

## Corrected Claim

LFU对长尾冷对象存在驱逐劣势：长尾对象（bottom 50%）贡献约10%请求，LFU因频率低优先驱逐。在Pareto(β=0.9)分布下，该劣势量级约为5%（估算值），可部分抵消锁定优势。

## Evidence

[质询]公式 D_disadvantage ≈ (1 - L_lock) * (1 - 1/β) 缺乏明确的理论推导依据，且将 Pareto 指数 β 直接代入该线性组合公式在逻辑上显得牵强，属于经验性估算而非严格推导。 | 先验知识/题面给定，逻辑校验通过（数值量级合理，0.053 表示约 5.3% 的性能劣势，符合长尾场景下的直觉），但公式本身为经验近似，无外部来源直接支持其具体形式。
