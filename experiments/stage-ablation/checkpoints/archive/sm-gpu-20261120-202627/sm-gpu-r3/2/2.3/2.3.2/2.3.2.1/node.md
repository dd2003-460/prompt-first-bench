# N222: Qwen3-27B 在 AWQ-INT8 量化下，于 WikiText-2 基准测试上的困惑度 (PPL) 绝对增加量，需对比 BF16 基线值与量化后值以验证

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N56, N57, N58

## Claim

Qwen3-27B 在 AWQ-INT8 量化下，于 WikiText-2 基准测试上的困惑度 (PPL) 绝对增加量，需对比 BF16 基线值与量化后值以验证是否落在 0.2-0.5 个百分点区间

## Corrected Claim

Qwen3-27B 在 AWQ-INT8 量化下，于 WikiText-2 基准测试上的困惑度 (PPL) 会有所增加，具体增量需查阅官方技术报告或基准测试数据以确认是否落在 0.2-0.5 个百分点区间。

## Evidence

[质询]该陈述包含具体的经验性数值区间（0.2-0.5），属于硬件/模型性能指标，无法从第一性原理推导，且缺乏来源支持以确认该特定量化方案下的具体PPL增量是否严格落在该区间。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，无法验证具体数值区间）

## Search Query

Qwen3-27B AWQ INT8 perplexity WikiText-2 vs BF16 benchmark
