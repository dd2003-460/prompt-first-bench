# N163: 工作点3（低频大对象/低QPS高带宽）：基于 s_avg=1.4MB，日均请求量 N_total = 2TB / 1.4MB ≈ 1,522,000 次，此工作

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N50

## Claim

工作点3（低频大对象/低QPS高带宽）：基于 s_avg=1.4MB，日均请求量 N_total = 2TB / 1.4MB ≈ 1,522,000 次，此工作点下请求数计费成本最低，但带宽峰值压力最大，自建节点的带宽瓶颈风险最高。

## Corrected Claim

工作点3（低频大对象/低QPS高带宽）：基于 s_avg=1.4MB，日均请求量 N_total = 2TB / 1.4MB ≈ 1,522,000 次，此工作点下请求数计费成本最低，但带宽峰值压力最大，自建节点的带宽瓶颈风险最高。

## Evidence

先验知识/题面给定，逻辑校验通过：2TB / 1.4MB ≈ 1,522,000 次计算正确，低频大对象导致高带宽峰值的逻辑符合物理直觉
