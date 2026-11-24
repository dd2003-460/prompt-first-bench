# N27: 温数据IOPS需求：每日扫描1-2次，假设每次扫描并行度16，每次读取块大小1MB，总IOPS ≈ (100TB / 1MB) × (1-2) / (24h×3

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N5

## Claim

温数据IOPS需求：每日扫描1-2次，假设每次扫描并行度16，每次读取块大小1MB，总IOPS ≈ (100TB / 1MB) × (1-2) / (24h×3600s) ≈ 11-22 IOPS（极低）[待核验：需确认扫描并行度和块大小]

## Corrected Claim

温数据IOPS需求：每日扫描1-2次，假设每次扫描并行度16，每次读取块大小1MB，总IOPS ≈ (100TB / 1MB) × (1-2) / (24h×3600s) ≈ 11-22 IOPS（极低）[待核验：需确认扫描并行度和块大小]

## Evidence

父节点级核验未通过：不完备（子节点正交且无冗余，但存在严重逻辑矛盾与不完备。父节点基于24小时窗口计算得出极低IOPS（11-22），而子节点B引入4小时窗口假设，这将导致实际IOPS需求提升至约300-600，直接推翻父节点‘极低’的结论；此外，子节点未覆盖父节点中‘待核验’的块大小参数。）

## Search Query

data lake scan IOPS requirement parallelism block size
