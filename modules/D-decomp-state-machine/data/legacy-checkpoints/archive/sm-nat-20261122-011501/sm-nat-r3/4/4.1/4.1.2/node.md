# N51: 更新率对缓存失效频率的综合影响：缓存中对象的平均失效频率 f_inval = 1 / T_life * (1 - P_inval) + P_inval / T_

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N14

## Claim

更新率对缓存失效频率的综合影响：缓存中对象的平均失效频率 f_inval = 1 / T_life * (1 - P_inval) + P_inval / T_res，其中 P_inval 为失效概率，T_res 为驻留时间；该频率决定了 LRU 缓存的稳态命中率折损程度。

## Corrected Claim

更新率对缓存失效频率的综合影响：缓存中对象的平均失效频率 f_inval 可近似表示为 1 / T_life * (1 - P_inval) + P_inval / T_res，其中 P_inval 为失效概率，T_res 为与更新策略相关的特征时间常数；该频率与 LRU 缓存的稳态命中率折损程度正相关，但具体关系需结合替换策略动态建模。

## Evidence

父节点级核验未通过：不完备, 有冗余（子节点本质上是同一参数（驻留时间 T_res/更新率）在不同取值下的计算实例，属于参数扫描而非正交的概念分解，存在严重冗余。此外，父节点核心公式包含 T_life（对象自然寿命），但子节点仅关注 T_res（缓存驻留时间）导致的失效，完全忽略了 T_life 项对 f_inval 的贡献，导致对父节点定义的覆盖不完备。）
