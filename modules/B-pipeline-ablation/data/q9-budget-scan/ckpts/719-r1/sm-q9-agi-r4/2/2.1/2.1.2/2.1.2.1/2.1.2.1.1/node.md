# N430: BGE-large-en-v1.5 在 MTEB Retrieval 子集上的 nDCG@10 = 0.57：基于 MTEB v1.0 公开基准，数据集为 BE

- **status**: degraded
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N145

## Claim

BGE-large-en-v1.5 在 MTEB Retrieval 子集上的 nDCG@10 = 0.57：基于 MTEB v1.0 公开基准，数据集为 BEIR 中的 ScienceQA，查询数 1000，文档库 10,000，nDCG@10 均值 0.57，标准差 0.03

## Corrected Claim

BGE-large-en-v1.5 在 MTEB Retrieval 子集（如 SciQ 或 Scifact）上的 nDCG@10 约为 0.57（具体数值需以官方 MTEB 榜单为准，数据集名称需核实是否为 SciQ/Scifact 而非 ScienceQA）。

## Evidence

[质询]数据集名称疑似错误：MTEB Retrieval 子集中通常包含 'SciQ' (Science Questions) 而非 'ScienceQA'，且 BEIR 中对应的数据集通常称为 'scifact' 或 'sciq'，'ScienceQA' 并非 BEIR 标准数据集名称，存在口径混淆或名称张冠李戴的风险。 | source=knowledge，逻辑量级合理（nDCG@10 0.57 符合 BGE-large 在检索任务上的典型表现），但数据集名称 'ScienceQA' 与 BEIR/MTEB 标准命名存在潜在冲突，且无外部来源验证具体数值，故降级。
