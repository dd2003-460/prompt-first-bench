# N229: 自建带宽边际成本 C_marginal_bw ≈ 0，因为 10 Gbps/点 的带宽已包干，实际出网流量 400 GB/day ≈ 3.5 Gbps 平均带宽

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N72

## Claim

自建带宽边际成本 C_marginal_bw ≈ 0，因为 10 Gbps/点 的带宽已包干，实际出网流量 400 GB/day ≈ 3.5 Gbps 平均带宽，远低于 10 Gbps 上限，未产生超额费用；但若流量峰值超过 10 Gbps，需额外购买带宽或扩容，边际成本跃升至 ¥5,000-10,000/Gbps/月。

## Corrected Claim

自建带宽边际成本 C_marginal_bw ≈ 0，因为 10 Gbps/点 的带宽已包干，实际出网流量 400 GB/day ≈ 3.5 Gbps 平均带宽，远低于 10 Gbps 上限，未产生超额费用；但若流量峰值超过 10 Gbps，需额外购买带宽或扩容，边际成本跃升至 ¥5,000-10,000/Gbps/月。

## Evidence

先验知识/题面给定，逻辑校验通过：400GB/day 换算为平均带宽约 3.47 Gbps，确实低于 10 Gbps 上限，符合包干制下边际成本为零的逻辑；峰值超限时需扩容导致边际成本跃升符合云计算/IDC 计费常识。
