# N44: 调用本地文献搜索 API（基于 N30/N31 的检索后端）的单次平均延迟（P50/P95），受限于 V100 推理吞吐，预计 <1s（P50）和 <3s（P9

- **status**: degraded
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

[质询]缺乏具体的系统架构细节（如并发数、索引大小、网络开销）来支撑具体的 P50/P95 延迟数值，且 V100 推理吞吐并非唯一瓶颈，I/O 和预处理也可能影响延迟，导致具体数值预测缺乏严谨依据。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且具体延迟数值属于经验性能指标，无法从第一性原理严格推出）

## Search Query

Vector database search latency HNSW top-k query time milliseconds
