# N171: 偏远地区用户到最近边缘节点的物理距离 d_remote 分布：假设偏远地区20%用户分布在半径 R=200km 内（覆盖稀疏），平均直线距离 d_avg ≈ 1

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N53

## Claim

偏远地区用户到最近边缘节点的物理距离 d_remote 分布：假设偏远地区20%用户分布在半径 R=200km 内（覆盖稀疏），平均直线距离 d_avg ≈ 100km。光纤传播延迟 t_prop = 2 * 100km / 2.0e8 * 1.05 ≈ 1.05ms。但偏远地区接入网质量差，最后一公里延迟高，RTT_remote_base 通常为 30-60ms（含接入网延迟、路由跳数多）。N53假设60ms合理，但需分解为传播延迟与接入延迟。

## Corrected Claim

偏远地区用户到最近边缘节点的物理距离 d_remote 分布：假设偏远地区20%用户分布在半径 R=200km 内（覆盖稀疏），平均直线距离 d_avg ≈ 100km。光纤传播延迟 t_prop = 2 * 100km / 2.0e8 * 1.05 ≈ 1.05ms。但偏远地区接入网质量差，最后一公里延迟高，RTT_remote_base 通常为 30-60ms（含接入网延迟、路由跳数多）。N53假设60ms合理，但需分解为传播延迟与接入延迟。

## Evidence

先验知识/题面给定，逻辑校验通过：光纤传播速度约2e8 m/s，100km往返传播延迟约1ms，加上接入网延迟后30-60ms符合偏远地区网络工程常识。

## Search Query

rural area internet latency RTT breakdown China
