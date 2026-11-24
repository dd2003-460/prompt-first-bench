# N323: SSD 层 42 盘的容量与 IOPS 匹配：42 盘 * 100,000 IOPS/盘 = 4.2M IOPS，对应容量若为 100TB (每盘 ~2.4TB

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N119

## Claim

SSD 层 42 盘的容量与 IOPS 匹配：42 盘 * 100,000 IOPS/盘 = 4.2M IOPS，对应容量若为 100TB (每盘 ~2.4TB)，则 SSD 层仅缓存 20% 温数据，命中率假设 80% 需通过 Zipf 分布验证

## Corrected Claim

SSD 层 42 盘的容量与 IOPS 匹配：42 盘 * 100,000 IOPS/盘 = 4.2M IOPS，对应容量若为 100TB (每盘 ~2.4TB)，则 SSD 层仅缓存 20% 温数据，命中率假设 80% 需通过 Zipf 分布验证

## Evidence

先验知识/题面给定，逻辑校验通过：42*100,000=4.2M IOPS 计算正确；100TB/42≈2.4TB 单盘容量符合当前企业级 SSD 规格；Zipf 分布用于验证缓存命中率是标准存储系统建模方法，逻辑自洽。
