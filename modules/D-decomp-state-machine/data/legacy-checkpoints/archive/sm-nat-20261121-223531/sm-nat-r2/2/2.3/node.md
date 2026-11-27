# N12: LRU 工作点 2（中性价比最优）：引入负相关修正项 ΔH_corr = ∂H/∂ρ * ρ，其中 ∂H/∂ρ 通过蒙特卡洛模拟 10,000 次样本估计，ρ=

- **status**: verified
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N2

## Claim

LRU 工作点 2（中性价比最优）：引入负相关修正项 ΔH_corr = ∂H/∂ρ * ρ，其中 ∂H/∂ρ 通过蒙特卡洛模拟 10,000 次样本估计，ρ=-0.3 时命中率提升约 [待核验] 2-4 个百分点，因为小对象更热，LRU 保留更多小热对象，字节命中率增加。

## Corrected Claim

引入负相关修正项以优化LRU工作点，理论上因小对象更热且被LRU保留，可提升字节命中率，具体提升幅度需通过蒙特卡洛模拟估计（通常可能在2-4个百分点范围内，但需具体实验验证）。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点逻辑链条清晰且互斥：子节点1确定基准状态（饱和/100%），子节点2推导在基准下修正项为0，子节点3界定父节点中'2-4%提升'适用的特定约束条件（容量受限）。三者分别回答了'基准是什么'、'当前条件下结果如何'、'父节点声称的数值在何种条件下成立'，无重叠或矛盾，且完整覆盖了父节点中关于命中率、修正项及数值核验的关键点。）

## Search Query

LRU cache hit rate correlation size popularity negative effect simulation

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/679259506&rut=19df410703929c4d853a409a4ba9798b9fefec372da4683f721bfbe30792f6db', 'type': 'ddg', 'title': 'Lru Lfu 自适应算法设计纲要 - 知乎'}
- {'url': 'https://zhuanlan.zhihu.com/p/161269766&rut=4b65747551d00092c5dbd88d992ba281c50022ca3546f5a50543d7af1c7fc47e', 'type': 'ddg', 'title': 'Lru原理与算法实现 - 知乎专栏'}
