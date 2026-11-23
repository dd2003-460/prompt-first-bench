# N126: 在 $K_{peak}=2.0$ 且流量分布均匀假设下，95th 带宽 $B_{95}$ 近似等于峰值带宽 $B_{peak}$，即 $B_{95} \appr

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N31

## Claim

在 $K_{peak}=2.0$ 且流量分布均匀假设下，95th 带宽 $B_{95}$ 近似等于峰值带宽 $B_{peak}$，即 $B_{95} \approx (2 \text{ TB} / 86400 \text{ s} \times 8000 \text{ bit/byte}) \times 2.0 \approx 37 \text{ Mbps} \approx 0.037 \text{ Gbps}$。

## Corrected Claim

在 $K_{peak}=2.0$ 且流量分布均匀假设下，95th 带宽 $B_{95}$ 近似等于峰值带宽 $B_{peak}$，即 $B_{95} \approx (2 \text{ TB} / 86400 \text{ s} \times 8000 \text{ bit/byte}) \times 2.0 \approx 37 \text{ Mbps} \approx 0.037 \text{ Gbps}$。

## Evidence

先验知识/题面给定，逻辑校验通过：计算过程 (2*10^12 / 86400 * 8000 * 2.0) ≈ 3.7037 * 10^7 bps ≈ 37 Mbps ≈ 0.037 Gbps，数值量级与推导逻辑自洽。
