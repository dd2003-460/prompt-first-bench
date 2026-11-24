# N674: N279 中使用的 Read/Write 功耗 8W 为峰值序列读功耗，对于冷数据为主的场景，实际 IO 多为小随机读，功耗更接近 Idle 水平（~4.5W）

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N278, N279, N280

## Claim

N279 中使用的 Read/Write 功耗 8W 为峰值序列读功耗，对于冷数据为主的场景，实际 IO 多为小随机读，功耗更接近 Idle 水平（~4.5W），因此 5% Read + 5% Write 的加权贡献应从 0.8W 下调至 ~0.45W，修正后 W_HDD_avg ≈ 2.9W。

## Corrected Claim

N279 中使用的 Read/Write 功耗 8W 为峰值序列读功耗，对于冷数据为主的场景，实际 IO 多为小随机读，功耗更接近 Idle 水平（~4.5W），因此 5% Read + 5% Write 的加权贡献应从 0.8W 下调至 ~0.45W，修正后 W_HDD_avg ≈ 2.9W。

## Evidence

先验知识/题面给定，逻辑校验通过：HDD空闲功耗通常低于读写峰值功耗，基于负载比例（5%+5%）和功耗水平（~4.5W vs 8W）进行的线性加权计算在数学上自洽且符合硬件功耗常识。
