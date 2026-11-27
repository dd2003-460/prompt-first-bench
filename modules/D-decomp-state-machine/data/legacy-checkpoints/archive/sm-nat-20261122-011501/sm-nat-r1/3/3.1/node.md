# N11: LFU 理论最优驻留集合 S_LFU：在相同内存限制下，LFU 驻留频率最高的对象；由于热度分布 Pareto(β=0.9) 比大小分布 Pareto(α=1.

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N3

## Claim

LFU 理论最优驻留集合 S_LFU：在相同内存限制下，LFU 驻留频率最高的对象；由于热度分布 Pareto(β=0.9) 比大小分布 Pareto(α=1.1) 更陡峭，LFU 集合偏向极小且极热的对象，其字节命中率上界为 sum_{i in S_LFU} (request_rate_i * size_i) / total_bytes_requested_per_day。

## Corrected Claim

LFU 理论最优驻留集合 S_LFU：在相同内存限制下，LFU 驻留频率最高的对象；由于热度分布 Pareto(β=0.9) 比大小分布 Pareto(α=1.1) 更陡峭，LFU 集合偏向极小且极热的对象，其字节命中率上界为 sum_{i in S_LFU} (request_rate_i * size_i) / total_bytes_requested_per_day。

## Evidence

先验知识/题面给定，逻辑校验通过：LFU 定义驻留频率最高对象，Pareto 分布陡峭度对比符合直觉，字节命中率公式量纲正确（字节/字节）。
