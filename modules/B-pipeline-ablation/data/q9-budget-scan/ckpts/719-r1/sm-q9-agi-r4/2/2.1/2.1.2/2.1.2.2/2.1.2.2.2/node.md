# N434: efSearch 参数对 Recall@5 的边际递减效应公式：d(Recall)/d(efSearch) ≈ k * (1 - Recall)^2，在 efS

- **status**: degraded
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N146, N147, N150

## Claim

efSearch 参数对 Recall@5 的边际递减效应公式：d(Recall)/d(efSearch) ≈ k * (1 - Recall)^2，在 efSearch=32 时 Recall@5≈0.78，提升至 efSearch=64 时 Recall@5≈0.88，边际增益 0.10；若追求 Recall@5≥0.95，需 efSearch≥128，但延迟将线性增加至 200ms+，超出实时交互阈值

## Corrected Claim

efSearch 参数通常对 Recall@k 呈现边际递减效应，具体数值（如 Recall 从 0.78 提升至 0.88 所需的 efSearch 增量及对应的延迟开销）取决于数据集特征与系统配置，需通过实际基准测试确定，而非固定公式推导。

## Evidence

[质询]该陈述包含具体的经验参数（如 efSearch=32 对应 Recall 0.78，efSearch=64 对应 0.88，以及特定的边际递减公式系数 k 和延迟阈值 200ms），这些数值高度依赖于具体的数据集规模、向量维度、索引构建参数（如 M, efConstruction）及硬件环境，并非普适的物理定律或数学恒等式，无法从第一性原理严格推出。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

HNSW efSearch recall@5 marginal gain curve threshold 0.95
