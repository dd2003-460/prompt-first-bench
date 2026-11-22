# N117: 回归概率 $P_{return}$ 的时间衰减模型：$P_{return}(t) = P_{return,0} \times e^{-\lambda_{deca

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N50

## Claim

回归概率 $P_{return}$ 的时间衰减模型：$P_{return}(t) = P_{return,0} \times e^{-\lambda_{decay} t}$，其中 $P_{return,0}$ 为退出后30天内的基础回归概率（估算为 10-15%），$\lambda_{decay}$ 为衰减率（估算为 0.05-0.1/月），$t$ 为退出后经过的月数；该参数决定了长期供给损失的稳定性。

## Corrected Claim

回归概率 $P_{return}$ 的时间衰减模型：$P_{return}(t) = P_{return,0} \times e^{-\lambda_{decay} t}$，其中 $P_{return,0}$ 为退出后30天内的基础回归概率（估算为 10-15%），$\lambda_{decay}$ 为衰减率（估算为 0.05-0.1/月），$t$ 为退出后经过的月数；该参数决定了长期供给损失的稳定性。

## Evidence

先验知识/题面给定，逻辑校验通过
