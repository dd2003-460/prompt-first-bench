# N268: 系数 0.25 的具体实例化推导：对于 BF16->INT8 (R_bit=2)，假设 α_compute=1.0 (计算非瓶颈)，β_overhead=0.8

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N88

## Claim

系数 0.25 的具体实例化推导：对于 BF16->INT8 (R_bit=2)，假设 α_compute=1.0 (计算非瓶颈)，β_overhead=0.8 (20% 开销不变)，则 η_throughput = (2-1)*1.0*0.8 = 0.8 (80% 提升)。TCO 变动 = 1/(1+0.8) - 1 = 1/1.8 - 1 ≈ -44%。若 β_overhead=0.6 (40% 固定开销)，η_throughput = 0.6，TCO 变动 = 1/1.6 - 1 = -37.5%。系数 0.25 可能对应更保守的 β_overhead 或特定硬件的 α_compute 衰减，需实测校准。

## Corrected Claim

系数 0.25 的具体实例化推导：对于 BF16->INT8 (R_bit=2)，假设 α_compute=1.0 (计算非瓶颈)，β_overhead=0.8 (20% 开销不变)，则 η_throughput = (2-1)*1.0*0.8 = 0.8 (80% 提升)。TCO 变动 = 1/(1+0.8) - 1 = 1/1.8 - 1 ≈ -44%。若 β_overhead=0.6 (40% 固定开销)，η_throughput = 0.6，TCO 变动 = 1/1.6 - 1 = -37.5%。系数 0.25 可能对应更保守的 β_overhead 或特定硬件的 α_compute 衰减，需实测校准。

## Evidence

先验知识/题面给定，逻辑校验通过：数学推导自洽（1/1.8-1≈-44.4%，1/1.6-1=-37.5%），系数0.25作为经验校准值的定性描述合理。
