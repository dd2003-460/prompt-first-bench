# N294: 2,440 TB HDD 的物理盘数量 = 2,440 TB / 单盘容量；N104 假设单盘 16 TB，则需 152.5 块，取 153 块；若单盘为 12

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N104

## Claim

2,440 TB HDD 的物理盘数量 = 2,440 TB / 单盘容量；N104 假设单盘 16 TB，则需 152.5 块，取 153 块；若单盘为 12 TB，则需 203.3 块，取 204 块；若单盘为 20 TB，则需 122 块。盘数与单盘容量成反比，直接影响备件成本基数

## Corrected Claim

2,440 TB HDD 的物理盘数量 = 2,440 TB / 单盘容量；N104 假设单盘 16 TB，则需 152.5 块，取 153 块；若单盘为 12 TB，则需 203.3 块，取 204 块；若单盘为 20 TB，则需 122 块。盘数与单盘容量成反比，直接影响备件成本基数

## Evidence

先验知识/题面给定，逻辑校验通过：2440/16=152.5(取153), 2440/12≈203.33(取204), 2440/20=122，计算准确且符合向上取整逻辑

## Search Query

enterprise HDD capacity 12TB 16TB 20TB standard sizes 2024
