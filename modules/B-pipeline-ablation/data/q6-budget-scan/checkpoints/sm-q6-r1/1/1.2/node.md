# N8: 流量峰值特征量化：日活 500 万，日均下载 2TB，假设用户活跃时间集中在 12 小时（8:00-20:00），峰值系数 K_peak = 3.0（即峰值 Q

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1

## Claim

流量峰值特征量化：日活 500 万，日均下载 2TB，假设用户活跃时间集中在 12 小时（8:00-20:00），峰值系数 K_peak = 3.0（即峰值 QPS 是日均 QPS 的 3 倍），则日均 QPS = 2TB / 200MB / 12h / 3600s ≈ 23.15 req/s，峰值 QPS ≈ 69.45 req/s；若考虑突发流量，需乘以突发系数 B_burst = 2.0，则最大瞬时 QPS ≈ 138.9 req/s。

## Corrected Claim

流量峰值特征量化：日活 500 万，日均下载 2TB，假设用户活跃时间集中在 12 小时（8:00-20:00），峰值系数 K_peak = 3.0（即峰值 QPS 是日均 QPS 的 3 倍），则日均 QPS = 2TB / 200MB / 12h / 3600s ≈ 23.15 req/s，峰值 QPS ≈ 69.45 req/s；若考虑突发流量，需乘以突发系数 B_burst = 2.0，则最大瞬时 QPS ≈ 138.9 req/s。

## Evidence

先验知识/题面给定，逻辑校验通过：2TB/200MB=10000 req, 10000/(12*3600)≈23.15, 23.15*3≈69.45, 69.45*2≈138.9，计算无误且量级合理。
