# N218: 阶梯计费的加权平均单价 $P_{weighted}$ 计算：若 $B_{reserved}$ 跨越多个阶梯，$P_{weighted} = \sum (B_i 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N74

## Claim

阶梯计费的加权平均单价 $P_{weighted}$ 计算：若 $B_{reserved}$ 跨越多个阶梯，$P_{weighted} = \sum (B_i \times R_i) / B_{reserved}$，其中 $B_i$ 为第 $i$ 阶梯的带宽量，$R_i$ 为对应单价，需精确计算各阶梯占比。

## Corrected Claim

阶梯计费的加权平均单价 $P_{weighted}$ 计算：若 $B_{reserved}$ 跨越多个阶梯，$P_{weighted} = \sum (B_i \times R_i) / B_{reserved}$，其中 $B_i$ 为第 $i$ 阶梯的带宽量，$R_i$ 为对应单价，需精确计算各阶梯占比。

## Evidence

先验知识/题面给定，逻辑校验通过：加权平均单价的定义即为各部分数值与其对应权重的乘积之和除以总权重，公式 $P_{weighted} = \sum (B_i \times R_i) / B_{reserved}$ 符合数学定义及经济学直觉，量纲一致（带宽×单价/带宽=单价）。
