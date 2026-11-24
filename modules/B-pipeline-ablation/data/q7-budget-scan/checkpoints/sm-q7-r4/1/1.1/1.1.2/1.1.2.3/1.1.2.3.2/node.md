# N415: 工作点B (RAID-5) 的Parity校验开销：RAID-5读操作需读取Data Stripe和Parity Stripe进行校验（若启用Read Veri

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N138

## Claim

工作点B (RAID-5) 的Parity校验开销：RAID-5读操作需读取Data Stripe和Parity Stripe进行校验（若启用Read Verify），额外I/O开销增加约33%（读2份数据+1份Parity），若启用Read Verify，有效吞吐降至 T_read_eff = T_theoretical / 1.33 ≈ 7.8GB/s / 1.33 ≈ 5.9GB/s。

## Corrected Claim

工作点B (RAID-5) 的Parity校验开销：RAID-5读操作需读取Data Stripe和Parity Stripe进行校验（若启用Read Verify），额外I/O开销增加约33%（读2份数据+1份Parity），若启用Read Verify，有效吞吐降至 T_read_eff = T_theoretical / 1.33 ≈ 7.8GB/s / 1.33 ≈ 5.9GB/s。

## Evidence

先验知识/题面给定，逻辑校验通过：RAID-5 Read Verify 需读取 Data 和 Parity，I/O 量增加 1/3 (33%)，吞吐量线性下降计算正确 (7.8/1.33≈5.86)。
