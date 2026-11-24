# N50: NVMe SSD预留空间率（Over-Provisioning, OP）通常为20%-30%以维持写入性能，而非通用的10%；若系统层预留10%则总OP为30%

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N10

## Claim

NVMe SSD预留空间率（Over-Provisioning, OP）通常为20%-30%以维持写入性能，而非通用的10%；若系统层预留10%则总OP为30%-40%，导致有效容量进一步降低至物理容量的60%-70%

## Corrected Claim

NVMe SSD预留空间率（Over-Provisioning, OP）通常为20%-30%以维持写入性能，而非通用的10%；若系统层预留10%则总OP为30%-40%，导致有效容量进一步降低至物理容量的60%-70%

## Evidence

先验知识/题面给定，逻辑校验通过
