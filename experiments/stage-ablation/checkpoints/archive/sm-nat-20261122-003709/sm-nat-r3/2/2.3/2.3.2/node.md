# N48: 计算 LFU 频率计数器收敛时间 T_convergence，定义为频率估计值稳定到真实热度分布所需的平均时间，公式近似为 T_convergence ≈ 3 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N12

## Claim

计算 LFU 频率计数器收敛时间 T_convergence，定义为频率估计值稳定到真实热度分布所需的平均时间，公式近似为 T_convergence ≈ 3 / λ_update（假设指数平滑），在 λ_update=0.01/day 时 T_convergence ≈ 300 天，表明在 300 天内 LFU 命中率低于 LRU 的窗口期长度。

## Corrected Claim

计算 LFU 频率计数器收敛时间 T_convergence，定义为频率估计值稳定到真实热度分布所需的平均时间，公式近似为 T_convergence ≈ 3 / λ_update（假设指数平滑），在 λ_update=0.01/day 时 T_convergence ≈ 300 天，表明在 300 天内 LFU 命中率低于 LRU 的窗口期长度。

## Evidence

先验知识/题面给定，逻辑校验通过：指数平滑收敛时间常数通常为 1/λ，3/λ 对应约 95% 置信区间，数值计算 3/0.01=300 正确，量级合理。
