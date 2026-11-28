# N44: 调用本地文献搜索 API（基于 N30/N31 的检索后端）的单次平均延迟（P50/P95），受限于 V100 推理吞吐，预计 <1s（P50）和 <3s（P9

- **status**: pending
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N10, N11, N12

## Claim

调用本地文献搜索 API（基于 N30/N31 的检索后端）的单次平均延迟（P50/P95），受限于 V100 推理吞吐，预计 <1s（P50）和 <3s（P95）

## Corrected Claim

调用本地文献搜索 API 的单次平均延迟预计较低，受限于 V100 推理吞吐及系统 I/O，P50 可能在秒级以内，P95 可能在数秒以内，具体数值需实测确定。

## Evidence

父节点级核验未通过：不完备（父节点描述的是‘本地文献搜索API’的整体延迟（含检索后端N30/N31），而子节点仅描述了‘Hybrid Search融合与重排序’这一特定阶段（基于N89/N90）。首先，ID不一致暗示子节点可能属于不同的系统组件或版本；其次，子节点未覆盖父节点中提到的‘检索后端（N30/N31）’本身的检索延迟，只覆盖了后续的融合与重排，导致对父节点整体延迟构成的解释不完整。）

## Search Query

Vector database search latency HNSW top-k query time milliseconds
