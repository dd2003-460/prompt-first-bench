# N105: 回源带宽成本公式：C_origin_bw = V_download_total * R_origin * p_origin_bw，其中V_download_to

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N28

## Claim

回源带宽成本公式：C_origin_bw = V_download_total * R_origin * p_origin_bw，其中V_download_total为日均下载流量（2TB/天），p_origin_bw为回源带宽单价（自建骨干网约¥0.05-0.1/GB，公有云回源约¥0.2-0.5/GB）

## Corrected Claim

回源带宽成本公式：C_origin_bw = V_download_total * R_origin * p_origin_bw，其中V_download_total为日均下载流量（2TB/天），p_origin_bw为回源带宽单价（自建骨干网约¥0.05-0.1/GB，公有云回源约¥0.2-0.5/GB）

## Evidence

父节点级核验未通过：有冗余（子节点在逻辑上是正交的（不同命中率区间）且覆盖了父节点公式的主要变量场景，但存在严重的结构冗余。三个子节点本质上是同一公式 C = V * R * p * 30 在 R 取不同值时的线性计算结果，并未提供新的独立知识点或机制，而是重复了计算过程。）
