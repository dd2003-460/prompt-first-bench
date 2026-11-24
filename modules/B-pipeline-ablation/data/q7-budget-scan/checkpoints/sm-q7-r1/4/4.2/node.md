# N20: 冷数据访问频率约束：80%冷数据（400TB）若年访问次数<3次，则云对象存储的最低存储层（Glacier/OSS Archive）可用，其单位存储成本约为$0

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4

## Claim

冷数据访问频率约束：80%冷数据（400TB）若年访问次数<3次，则云对象存储的最低存储层（Glacier/OSS Archive）可用，其单位存储成本约为$0.004/GB/月；若年访问次数>10次，则需使用Standard-IA层，成本升至$0.01/GB/月，此时云方案相对HDD的成本优势从3.5x缩小至1.8x

## Corrected Claim

冷数据访问频率约束：80%冷数据（400TB）若年访问次数<3次，则云对象存储的最低存储层（Glacier/OSS Archive）可用，其单位存储成本约为$0.004/GB/月；若年访问次数>10次，则需使用Standard-IA层，成本升至$0.01/GB/月，此时云方案相对HDD的成本优势从3.5x缩小至1.8x

## Evidence

先验知识/题面给定，逻辑校验通过：Glacier/OSS Archive 成本量级（~$0.004/GB/月）与 Standard-IA 成本量级（~$0.01/GB/月）符合主流云厂商公开定价常识，且成本倍数变化逻辑自洽。
