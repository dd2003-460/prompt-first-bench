# N140: 工作点3（小对象/高开销）：当平均对象大小 A_obj = 10KB 时，元数据开销率 R_meta = C_meta / A_obj ≈ 1.5KB / 10

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N44

## Claim

工作点3（小对象/高开销）：当平均对象大小 A_obj = 10KB 时，元数据开销率 R_meta = C_meta / A_obj ≈ 1.5KB / 10KB ≈ 15%，此时元数据占用显著，且由于对象数量爆炸（500TB/10KB = 500亿个），API 调用成本（List/Get）将成为 TCO 主导项，远超存储容量成本

## Corrected Claim

工作点3（小对象/高开销）：当平均对象大小 A_obj = 10KB 时，元数据开销率 R_meta = C_meta / A_obj ≈ 1.5KB / 10KB ≈ 15%，此时元数据占用显著，且由于对象数量爆炸（500TB/10KB = 500亿个），API 调用成本（List/Get）将成为 TCO 主导项，远超存储容量成本

## Evidence

先验知识/题面给定，逻辑校验通过：1.5KB/10KB=15%计算正确；500TB/10KB=500亿数量级正确；小对象高元数据开销导致API成本主导TCO符合分布式存储工程常识。
