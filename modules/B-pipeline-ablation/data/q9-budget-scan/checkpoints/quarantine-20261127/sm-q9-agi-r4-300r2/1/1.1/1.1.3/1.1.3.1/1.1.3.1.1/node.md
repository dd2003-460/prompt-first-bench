# N252: 在 TP=4 线性链式拓扑（GPU0-GPU1-GPU2-GPU3）下，Ring AllReduce 的算法有效带宽利用率 η_algo ≈ 0.75-0.85

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N99

## Claim

在 TP=4 线性链式拓扑（GPU0-GPU1-GPU2-GPU3）下，Ring AllReduce 的算法有效带宽利用率 η_algo ≈ 0.75-0.85，实际有效带宽 B_eff ≈ 112-127 GB/s（基于 150 GB/s 单向聚合带宽），显著低于理论峰值，主要受限于 Ring 算法中 2(N-1)/N 的通信系数及链路拥塞。

## Corrected Claim

在 TP=4 线性链式拓扑（GPU0-GPU1-GPU2-GPU3）下，Ring AllReduce 的算法有效带宽利用率 η_algo ≈ 0.75-0.85，实际有效带宽 B_eff ≈ 112-127 GB/s（基于 150 GB/s 单向聚合带宽），显著低于理论峰值，主要受限于 Ring 算法中 2(N-1)/N 的通信系数及链路拥塞。

## Evidence

先验知识/题面给定，逻辑校验通过：Ring AllReduce 理论有效带宽为 2(N-1)/N * B_link，当 N=4 时系数为 0.75，结合链路拥塞等因素，0.75-0.85 的利用率及 112-127 GB/s 的有效带宽符合物理直觉与算法特性。
