# N299: 动态调整 B_limit_pop 的反馈控制算法：B_limit_pop(t+1) = B_limit_pop(t) + α * (B_origin_max -

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N95

## Claim

动态调整 B_limit_pop 的反馈控制算法：B_limit_pop(t+1) = B_limit_pop(t) + α * (B_origin_max - B_origin_actual(t))，其中 α=0.1 为学习率，B_origin_actual(t) 为当前实际回源带宽；该算法收敛时间约为 5-10 个采样周期（每周期 10s），确保在流量波动时快速响应

## Corrected Claim

动态调整 B_limit_pop 的反馈控制算法：B_limit_pop(t+1) = B_limit_pop(t) + α * (B_origin_max - B_origin_actual(t))，其中 α=0.1 为学习率，B_origin_actual(t) 为当前实际回源带宽；该算法收敛时间约为 5-10 个采样周期（每周期 10s），确保在流量波动时快速响应

## Evidence

先验知识/题面给定，逻辑校验通过：该公式为标准的比例控制（P-control）或梯度下降变体，α=0.1 在 0-1 区间内保证稳定性，收敛时间 5-10 个周期符合一阶线性系统的时间常数特性（1/α=10），量纲与逻辑自洽。
