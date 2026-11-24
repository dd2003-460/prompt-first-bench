# N198: RAID6重建时的实际写带宽受限于HDD的寻道时间与写入合并（Write Coalescing）效率，实际有效写带宽通常为标称顺序写的80%-90%，即120-

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N69

## Claim

RAID6重建时的实际写带宽受限于HDD的寻道时间与写入合并（Write Coalescing）效率，实际有效写带宽通常为标称顺序写的80%-90%，即120-180 MB/s/盘。

## Corrected Claim

RAID6重建时的实际写带宽受限于HDD的寻道时间与写入合并（Write Coalescing）效率，实际有效写带宽通常为标称顺序写的80%-90%，即120-180 MB/s/盘。

## Evidence

先验知识/题面给定，逻辑校验通过
