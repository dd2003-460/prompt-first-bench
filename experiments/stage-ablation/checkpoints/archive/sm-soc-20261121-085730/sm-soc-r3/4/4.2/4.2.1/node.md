# N84: 触发阈值 T_trigger 的优化值需满足 ∂ΔW/∂T_trigger = 0，即边际咨询转化率提升 δc'(T) 等于边际福利损失成本，当前设定 15% 

- **status**: verified
- **level**: L3
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N19

## Claim

触发阈值 T_trigger 的优化值需满足 ∂ΔW/∂T_trigger = 0，即边际咨询转化率提升 δc'(T) 等于边际福利损失成本，当前设定 15% 为经验值需实证校准 [待核验]

## Corrected Claim

触发阈值 T_trigger 的优化值理论上需满足边际收益等于边际成本（如 ∂ΔW/∂T_trigger = 0），具体数值（如 15%）需根据特定场景的实证数据校准，当前设定为经验值。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别对应父节点方程左侧的‘收益项’（边际咨询转化率）和右侧的‘成本项’（边际福利损失），两者在经济学逻辑上构成一阶条件的对立面，互不重叠且共同构成了优化问题的完整闭环。）

## Search Query

optimal price discount threshold for seller notification in secondhand market

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/675915592&rut=2b892c1335df7d0029e18edf2e730e6c6577781abacbb84959d8e8bb35db9923', 'type': 'ddg', 'title': '事件触发控制方案概述 - 知乎'}
