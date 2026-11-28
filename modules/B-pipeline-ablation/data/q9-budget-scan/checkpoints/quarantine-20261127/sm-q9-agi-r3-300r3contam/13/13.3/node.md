# N230: 贝叶斯知识更新的计算开销：对于单一假设节点的置信度更新，采用共轭先验（Beta 分布）时，更新公式为 $\alpha' = \alpha + \text{suc

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N90, N91

## Claim

贝叶斯知识更新的计算开销：对于单一假设节点的置信度更新，采用共轭先验（Beta 分布）时，更新公式为 $\alpha' = \alpha + \text{successes}, \beta' = \beta + \text{failures}$，单次浮点运算耗时 < 0.1ms；该步骤不涉及矩阵求逆或高维积分，因此不会成为闭环迭代中的计算瓶颈，总延迟由向量检索主导。

## Corrected Claim

贝叶斯知识更新的计算开销：对于单一假设节点的置信度更新，采用共轭先验（Beta 分布）时，更新公式为 $\alpha' = \alpha + \text{successes}, \beta' = \beta + \text{failures}$，单次浮点运算耗时 < 0.1ms；该步骤不涉及矩阵求逆或高维积分，因此不会成为闭环迭代中的计算瓶颈，总延迟由向量检索主导。

## Evidence

先验知识/题面给定，逻辑校验通过：Beta分布作为二项分布的共轭先验，其后验参数更新确实仅需加法运算，计算复杂度极低，远小于向量检索开销，符合基本数学与工程直觉。
