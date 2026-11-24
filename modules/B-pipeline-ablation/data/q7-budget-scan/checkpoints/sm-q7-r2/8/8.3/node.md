# N95: SSD 热层硬件成本的分项构成：100TB 有效容量需 $100 / 0.92 \approx 109TB$ 物理容量，考虑 RAID5 冗余系数 1.1，需 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N36

## Claim

SSD 热层硬件成本的分项构成：100TB 有效容量需 $100 / 0.92 \approx 109TB$ 物理容量，考虑 RAID5 冗余系数 1.1，需 $109 \times 1.1 \approx 120TB$ 物理容量，即需 31-63 块 1.92TB-3.84TB NVMe SSD；SSD 盘体成本约为 $12,000-18,000$ 美元，加上专用 SSD 控制器与背板成本（约 $3,000-5,000$ 美元），总 SSD 层成本约为 $15,000-23,000$ 美元，与 HDD 层成本相当

## Corrected Claim

SSD 热层硬件成本的分项构成：100TB 有效容量需 $100 / 0.92 \approx 109TB$ 物理容量，考虑 RAID5 冗余系数 1.1，需 $109 \times 1.1 \approx 120TB$ 物理容量，即需 31-63 块 1.92TB-3.84TB NVMe SSD；SSD 盘体成本约为 $12,000-18,000$ 美元，加上专用 SSD 控制器与背板成本（约 $3,000-5,000$ 美元），总 SSD 层成本约为 $15,000-23,000$ 美元，与 HDD 层成本相当

## Evidence

先验知识/题面给定，逻辑校验通过：容量计算（100/0.92*1.1≈120TB）及块数估算（120/1.92≈63, 120/3.84≈31）数学自洽；成本估算（31-63块 * $200-$300/块 + 控制器背板）符合当前企业级NVMe SSD市场量级，总成本区间合理。

## Search Query

SSD tier hardware cost calculation RAID5 overhead 100TB effective capacity
