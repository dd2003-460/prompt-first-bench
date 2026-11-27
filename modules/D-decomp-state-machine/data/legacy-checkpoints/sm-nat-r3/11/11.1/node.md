# N298: S_thresh = 128GB / 100,000 = 1.31MB，而非 2.04KB，修正了父节点中的计算错误；若按大小排序保留，LRU 能完整保留的对象

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N106

## Claim

S_thresh = 128GB / 100,000 = 1.31MB，而非 2.04KB，修正了父节点中的计算错误；若按大小排序保留，LRU 能完整保留的对象大小上限为 1.31MB，即所有对象均可被缓存。

## Corrected Claim

S_thresh = 128GB / 100,000 = 1.31MB，而非 2.04KB，修正了父节点中的计算错误；若按大小排序保留，LRU 能完整保留的对象大小上限为 1.31MB，即所有对象均可被缓存。

## Evidence

先验知识/题面给定，逻辑校验通过：128GB / 100,000 = 1.31MB 计算正确，且若最大对象小于该阈值，则所有对象均可被缓存，逻辑自洽。
