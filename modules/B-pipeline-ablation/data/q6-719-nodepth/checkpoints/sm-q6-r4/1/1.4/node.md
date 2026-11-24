# N9: 缓存命中率估算：Hit_Rate ≈ 1 - (Unique Objects / Total Requests)，其中 Unique Objects 由日均上传

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N1

## Claim

缓存命中率估算：Hit_Rate ≈ 1 - (Unique Objects / Total Requests)，其中 Unique Objects 由日均上传 200GB 和对象大小 s 决定，Total Requests 由日活 500 万和人均请求数决定。

## Corrected Claim

缓存命中率估算：Hit_Rate ≈ 1 - (Unique Objects / Total Requests)，其中 Unique Objects 由日均上传 200GB 和对象大小 s 决定，Total Requests 由日活 500 万和人均请求数决定。

## Evidence

父节点级核验未通过：不完备（子节点分别定义了公式中的两个变量（U和R）以及最终计算逻辑，彼此正交且不重复。但是，父节点中明确提到的‘缓存容量约束’在子节点3中仅作为边界条件提及，并未将其作为独立的计算维度或修正项进行分解，导致对于‘缓存容量不足’这一关键场景的量化估算缺失，未完全覆盖父节点隐含的复杂约束条件。）

## Search Query

CDN cache hit rate estimation formula unique objects
