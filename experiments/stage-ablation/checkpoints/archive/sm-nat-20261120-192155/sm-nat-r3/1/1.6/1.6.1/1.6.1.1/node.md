# N98: 工作点2（扫描干扰）：当存在周期性扫描流量（scan resistance）时，LRU缓存被冷对象污染，C_LRU偏离头部热对象集合，导致H_LRU显著低于H_

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N37

## Claim

工作点2（扫描干扰）：当存在周期性扫描流量（scan resistance）时，LRU缓存被冷对象污染，C_LRU偏离头部热对象集合，导致H_LRU显著低于H_LFU；量化上，扫描流量占比P_scan每增加10%，H_LRU下降约P_scan * (1 - H_opt)的幅度。

## Corrected Claim

工作点2（扫描干扰）：当存在周期性扫描流量时，LRU缓存被冷对象污染，C_LRU偏离头部热对象集合，导致H_LRU显著低于H_LFU；扫描流量占比P_scan的增加会显著降低H_LRU，具体降幅取决于缓存大小与扫描模式的交互作用。

## Evidence

[质询]量化公式 'H_LRU下降约P_scan * (1 - H_opt)' 缺乏严谨的理论推导支持，且量纲/系数合理性存疑。在缓存理论中，扫描流量对LRU的影响通常取决于缓存大小与扫描周期的比例，而非简单的线性乘积关系；此外，(1 - H_opt) 作为衰减因子在物理意义上并不直观，可能混淆了不同工作点下的性能边界。 | 先验知识/题面给定，逻辑校验通过（定性描述符合LRU对扫描流量敏感的常识，但定量公式缺乏来源支持且存在理论争议，故降级）

## Search Query

LRU scan resistance cache pollution impact
