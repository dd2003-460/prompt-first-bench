# N40: 平均驻留时间 T_c 的计算：T_c = C_total / (R_cached * S_avg_cached)，其中 C_total=128GB，R_cach

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N13

## Claim

平均驻留时间 T_c 的计算：T_c = C_total / (R_cached * S_avg_cached)，其中 C_total=128GB，R_cached 为缓存内对象总请求率，S_avg_cached 为缓存内对象平均大小 [待核验]

## Corrected Claim

平均驻留时间 T_c 的计算：T_c = C_total / (R_cached * S_avg_cached)，其中 C_total=128GB，R_cached 为缓存内对象总请求率，S_avg_cached 为缓存内对象平均大小 [待核验]

## Evidence

父节点级核验未通过：不完备, 有冗余（子节点1和子节点2本质上是同一公式在不同参数（K值）下的计算实例，存在显著冗余；子节点3是前两者的推论而非独立维度；此外，父节点标记为[待核验]，但子节点直接使用了未验证的拟合参数（如116.36, 0.9等）进行具体数值计算，缺乏对参数来源和有效性的独立核验节点，导致完备性不足。）

## Search Query

cache average residence time calculation formula LRU LFU
