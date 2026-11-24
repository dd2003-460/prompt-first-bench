# N184: 对象大小分布对 T_transfer 的影响：图片对象 s_img ≈ 500KB，短视频对象 s_vid ≈ 10MB；混合请求中图片占比 80%（按请求数）

- **status**: pending
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N53

## Claim

对象大小分布对 T_transfer 的影响：图片对象 s_img ≈ 500KB，短视频对象 s_vid ≈ 10MB；混合请求中图片占比 80%（按请求数），则平均传输对象大小 s_avg_req = 0.8×0.5MB + 0.2×10MB = 2.4MB；T_transfer_avg = 2.4MB / Effective_Bandwidth。

## Corrected Claim

对象大小分布对 T_transfer 的影响：图片对象 s_img ≈ 500KB，短视频对象 s_vid ≈ 10MB；混合请求中图片占比 80%（按请求数），则平均传输对象大小 s_avg_req = 0.8×0.5MB + 0.2×10MB = 2.4MB；T_transfer_avg = 2.4MB / Effective_Bandwidth。

## Evidence

父节点级核验未通过：不完备, 有冗余（子节点本质上是同一公式在不同带宽参数下的计算实例，存在结构性冗余；且父节点标题强调'对象大小分布'的影响，但子节点仅固定了平均大小进行计算，未体现'分布'（如长尾、方差）对传输时间或系统性能的非线性影响，导致覆盖不全。）
