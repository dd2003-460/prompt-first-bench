# N370: 卖家策略响应机制的微观基础：T_lag 的分布服从指数分布，参数 λ_seller 由卖家信息获取频率 f_info 和决策成本 C_decision 决定，λ

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N117

## Claim

卖家策略响应机制的微观基础：T_lag 的分布服从指数分布，参数 λ_seller 由卖家信息获取频率 f_info 和决策成本 C_decision 决定，λ_seller = f_info * exp(-C_decision)；若 λ_seller < 1/30，则 T_lag 期望值 > 30 天，表明卖家响应受限。

## Corrected Claim

卖家策略响应机制的微观基础：T_lag 的分布通常假设服从指数分布，其参数 λ_seller 受卖家信息获取频率 f_info 和决策成本 C_decision 影响；若 λ_seller < 1/30，则 T_lag 期望值 > 30 天，表明卖家响应受限。

## Evidence

[质询]公式 λ_seller = f_info * exp(-C_decision) 缺乏明确的量纲定义和理论推导依据，属于经验性假设而非第一性原理可推导的数学恒等式；且 'exp(-C_decision)' 中 C_decision 若为货币单位或无量纲成本，其指数衰减形式在微观经济学中并非标准结论，存在模型设定任意性的风险。 | source=knowledge，逻辑上指数分布期望值 1/λ 与阈值 30 天的推导自洽（1/λ > 30 等价于 λ < 1/30），但具体参数化公式 λ = f_info * exp(-C_decision) 属于特定模型假设，非普适物理/数学定律，且无外部来源支持该特定函数形式，故降级为定性表述。

## Search Query

seller decision frequency information acquisition cost price adjustment lag exponential distribution
