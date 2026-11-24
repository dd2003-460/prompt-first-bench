# N52: L_processing = L_auth + L_transform + L_encode，其中 L_auth 为鉴权延迟（<1ms），L_transform

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N11

## Claim

L_processing = L_auth + L_transform + L_encode，其中 L_auth 为鉴权延迟（<1ms），L_transform 为图片/视频转码延迟（若边缘节点执行转码，1.5MB 视频转码 50-200ms；若仅分发预转码内容，<5ms），L_encode 为响应编码延迟（<1ms）。

## Corrected Claim

L_processing = L_auth + L_transform + L_encode，其中 L_auth 为鉴权延迟（<1ms），L_transform 为图片/视频转码延迟（若边缘节点执行转码，1.5MB 视频转码 50-200ms；若仅分发预转码内容，<5ms），L_encode 为响应编码延迟（<1ms）。

## Evidence

父节点级核验通过：正交+完备+无冗余（三个子节点分别对应父节点公式中的 L_auth、L_transform 和 L_encode，概念上完全正交且无重叠。每个子节点都针对其对应的延迟组件进行了具体的条件分支分析和量化取值，覆盖了父节点中提到的所有关键方面（如鉴权机制差异、转码场景差异、编码协议开销）。虽然 L_transform 内部包含加权平均计算，但这属于对该组件内部的细化，而非跨节点的冗余。）

## Search Query

edge node object processing latency authentication transcoding encoding overhead
