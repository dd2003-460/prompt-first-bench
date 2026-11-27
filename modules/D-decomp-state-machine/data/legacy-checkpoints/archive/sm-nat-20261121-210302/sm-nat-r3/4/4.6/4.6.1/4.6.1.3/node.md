# N168: LFU 优化问题的一阶条件：∂P_hot_bytes/∂N_hot = 0，即边际请求字节量 S_{N_hot+1} * P_{N_hot+1} 等于当前平均请

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N59

## Claim

LFU 优化问题的一阶条件：∂P_hot_bytes/∂N_hot = 0，即边际请求字节量 S_{N_hot+1} * P_{N_hot+1} 等于当前平均请求字节量 P_hot_bytes * E[S] * N_total_requests / N，用于确定最优 N_hot 的数值解。

## Corrected Claim

LFU 优化问题的一阶条件：∂P_hot_bytes/∂N_hot = 0，即边际请求字节量 S_{N_hot+1} * P_{N_hot+1} 等于当前平均请求字节量 P_hot_bytes * E[S] * N_total_requests / N，用于确定最优 N_hot 的数值解。

## Evidence

先验知识/题面给定，逻辑校验通过
