# N21: 运维人力成本-自建：C_ops_self = N_engineers * C_salary * (1 + overhead)，其中N_engineers为运维工

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N2

## Claim

运维人力成本-自建：C_ops_self = N_engineers * C_salary * (1 + overhead)，其中N_engineers为运维工程师数量（10个POP点需3-5人），C_salary为年薪（约¥200k-500k/人），overhead为社保/福利系数（约30%）

## Corrected Claim

运维人力成本-自建：C_ops_self = N_engineers * C_salary * (1 + overhead)，其中N_engineers为运维工程师数量（10个POP点需3-5人），C_salary为年薪（约¥200k-500k/人），overhead为社保/福利系数（约30%）

## Evidence

父节点级核验未通过：非正交（子节点1定义了参数N_engineers的计算逻辑，子节点2直接引用该参数并计算最终成本，两者在逻辑上是层级依赖关系而非并列正交关系。虽然内容不重复，但将‘参数定义’与‘公式代入’拆分为两个平级子节点破坏了正交性（即子节点应各自独立描述父节点的不同维度，而非一个依赖另一个的中间步骤）。）

## Search Query

CDN operations team size and salary for 10 POP points
