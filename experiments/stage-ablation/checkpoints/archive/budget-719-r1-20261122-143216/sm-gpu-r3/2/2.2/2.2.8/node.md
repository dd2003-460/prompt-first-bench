# N69: 单卡方案 3 年电力成本公式：(GPU TDP + 100W) × 24h × 365d × 3y × $0.15/kWh，例如 RTX 4090: 550W 

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N12, N13, N14

## Claim

单卡方案 3 年电力成本公式：(GPU TDP + 100W) × 24h × 365d × 3y × $0.15/kWh，例如 RTX 4090: 550W × 26280h × 3y × $0.15 = $6,445.50

## Corrected Claim

单卡方案 3 年电力成本公式：(GPU TDP + 100W) × 24h × 365d × 3y × $0.15/kWh，例如 RTX 4090: 550W × 26280h × $0.15 = $2,168.10

## Evidence

父节点级核验未通过：非正交, 有冗余（子节点2和3是同一计算公式在不同硬件参数下的实例，属于高度冗余的重复结构；且子节点2中RTX 4090的功耗取值(450W)与父节点示例(550W)存在事实性矛盾，导致数据不一致。）

## Search Query

GPU 3 year electricity cost calculation formula
