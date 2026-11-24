# N103: 隐性运维成本规模效应：若 POP 数量从 10 增加到 20，总隐性运维成本并非线性翻倍，而是约为 105k × 20^(1/10) ≈ 116k 元/月，因为

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N26

## Claim

隐性运维成本规模效应：若 POP 数量从 10 增加到 20，总隐性运维成本并非线性翻倍，而是约为 105k × 20^(1/10) ≈ 116k 元/月，因为固定成本（工具链、部分人力）可分摊，但变动成本（监控、安全）随节点数线性增长。

## Corrected Claim

隐性运维成本规模效应：若 POP 数量从 10 增加到 20，总隐性运维成本并非线性翻倍，而是约为 105k × 20^(1/10) ≈ 116k 元/月，因为固定成本（工具链、部分人力）可分摊，但变动成本（监控、安全）随节点数线性增长。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别对应成本模型中的固定项（C_fixed）、变动项（C_var）以及整体规模效应指数（β）的验证逻辑。三者分别定义了模型的输入参数和输出验证，概念上相互独立且无重叠，共同构成了父节点中成本估算公式的完整分解。）

## Search Query

Operational cost scale effect POP nodes fixed variable cost amortization
