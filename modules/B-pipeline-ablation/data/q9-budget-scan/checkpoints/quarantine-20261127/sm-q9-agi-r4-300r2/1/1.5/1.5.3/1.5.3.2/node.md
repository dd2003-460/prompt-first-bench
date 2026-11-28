# N116: Compute-Bound 潜在工作点（不可达）：若要进入 Compute-Bound 区域（AI > 17.4），需要极大的 Batch Size 使得计算量

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N44

## Claim

Compute-Bound 潜在工作点（不可达）：若要进入 Compute-Bound 区域（AI > 17.4），需要极大的 Batch Size 使得计算量远超内存读取量。但在 16GB 显存限制下，27B 模型的权重和 KV Cache 已占满大部分显存，无法容纳足够大的 Batch Size 以提升 AI 至 Ridge Point 以上，因此在当前硬件配置下，系统永远处于 Memory-Bound 状态，优化方向应聚焦于内存带宽利用率和减少冗余读取。

## Corrected Claim

Compute-Bound 潜在工作点（不可达）：若要进入 Compute-Bound 区域（AI > 17.4），需要极大的 Batch Size 使得计算量远超内存读取量。但在 16GB 显存限制下，27B 模型的权重和 KV Cache 已占满大部分显存，无法容纳足够大的 Batch Size 以提升 AI 至 Ridge Point 以上，因此在当前硬件配置下，系统永远处于 Memory-Bound 状态，优化方向应聚焦于内存带宽利用率和减少冗余读取。

## Evidence

先验知识/题面给定，逻辑校验通过：27B模型FP16权重约54GB，远超16GB显存，即使量化后KV Cache与权重也占据绝大部分显存，导致Batch Size受限，算术强度(AI)难以突破Ridge Point，符合Memory-Bound特征。
