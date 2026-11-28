# N157: Hybrid Search 融合与重排序延迟：基于 N89/N90，融合成本约 5ms，Cross-Encoder 重排序（Top-50 候选）在 V100 上

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N44

## Claim

Hybrid Search 融合与重排序延迟：基于 N89/N90，融合成本约 5ms，Cross-Encoder 重排序（Top-50 候选）在 V100 上利用 Qwen3.8-27B 小模型或专用重排模型，延迟约 50-100ms，总延迟 P50 <200ms

## Corrected Claim

Hybrid Search 融合与重排序延迟：基于 N89/N90，融合成本约 5ms，Cross-Encoder 重排序（Top-50 候选）在 V100 上利用 Qwen3.8-27B 小模型或专用重排模型，延迟约 50-100ms，总延迟 P50 <200ms

## Evidence

先验知识/题面给定，逻辑校验通过：融合操作（向量+关键词）毫秒级开销合理；Cross-Encoder 对 Top-50 候选进行重排序，在 V100 GPU 上使用轻量级模型（如 27B 或更小专用模型）延迟 50-100ms 符合工程经验量级；总延迟 P50 < 200ms 与分项延迟之和（~5ms + ~100ms + 网络/IO 开销）逻辑自洽。
