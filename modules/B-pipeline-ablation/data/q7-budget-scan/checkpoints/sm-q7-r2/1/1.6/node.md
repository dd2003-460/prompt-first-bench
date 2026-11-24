# N10: 预留空间率：为防止碎片化和保证写入性能，预留10%空间，公式：有效容量 = 文件系统容量 × (1 - 0.10)

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1

## Claim

预留空间率：为防止碎片化和保证写入性能，预留10%空间，公式：有效容量 = 文件系统容量 × (1 - 0.10)

## Corrected Claim

预留空间率：为防止碎片化和保证写入性能，预留10%空间，公式：有效容量 = 文件系统容量 × (1 - 0.10)

## Evidence

父节点级核验未通过：不完备（子节点按存储介质（NVMe SSD、HDD、云对象存储）划分，彼此正交且无冗余。但父节点泛指'文件系统容量'，通常指本地磁盘文件系统，子节点引入了'云对象存储'这一非文件系统概念，且未涵盖通用SSD（非NVMe）或特定文件系统（如ext4/xfs）的默认行为，导致覆盖范围逻辑上不一致且不完备。）

## Search Query

storage reserved space percentage best practice
