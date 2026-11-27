# N35: LRU驻留集合的驱逐边界条件：当对象i的访问间隔Δt_i > T_res（缓存平均驻留时间）时，该对象被驱逐；T_res = 128GB / (Miss_Byt

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N9

## Claim

LRU驻留集合的驱逐边界条件：当对象i的访问间隔Δt_i > T_res（缓存平均驻留时间）时，该对象被驱逐；T_res = 128GB / (Miss_Bytes_Rate)，其中Miss_Bytes_Rate为未命中请求带来的字节写入速率，需迭代求解以闭合命中率方程。

## Corrected Claim

LRU驻留集合的驱逐边界条件：当对象i的访问间隔Δt_i > T_res（缓存平均驻留时间）时，该对象被驱逐；T_res = 128GB / (Miss_Bytes_Rate)，其中Miss_Bytes_Rate为未命中请求带来的字节写入速率，需迭代求解以闭合命中率方程。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别对应父节点中的三个关键逻辑环节：1. 定义迭代方程中的速率项（Miss_Bytes_Rate）；2. 定义速率项中的统计参数（E[S|Miss]）；3. 展示迭代求解的最终结果及一致性校验。三者层层递进，无重叠，且完整覆盖了从公式定义到数值求解的全过程。）
