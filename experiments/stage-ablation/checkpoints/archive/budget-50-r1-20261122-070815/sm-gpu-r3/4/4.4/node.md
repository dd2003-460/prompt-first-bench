# N26: 维护与折旧成本 (C_maint) = (C_hw × r_depreciation) + C_warranty，其中 r_depreciation 为年折旧率

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N4

## Claim

维护与折旧成本 (C_maint) = (C_hw × r_depreciation) + C_warranty，其中 r_depreciation 为年折旧率（通常 20-30%），C_warranty 为超出保修期的维修基金估算。

## Corrected Claim

维护与折旧成本 (C_maint) = (C_hw × r_depreciation) + C_warranty，其中 r_depreciation 为年折旧率（通常 20-30%），C_warranty 为超出保修期的维修基金估算。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别对应公式中的折旧率参数(r_depreciation)、保修/维修参数(C_warranty)以及最终的估算结果(C_maint)。三者分别针对公式的不同组成部分及最终输出，逻辑上正交且覆盖了公式的所有关键变量。虽然涉及消费级和数据中心两类GPU，但这是为了提供不同场景下的参数取值，属于参数化的具体实例化，而非冗余重复。）
