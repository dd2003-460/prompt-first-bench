# N77: Qwen3-27B 在 BF16 精度下的基线困惑度（PPL）：在 WikiText-2 数据集上约为 6.5-7.0（需查阅 Qwen3 技术报告或 Hugg

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N19

## Claim

Qwen3-27B 在 BF16 精度下的基线困惑度（PPL）：在 WikiText-2 数据集上约为 6.5-7.0（需查阅 Qwen3 技术报告或 HuggingFace 官方模型卡片获取精确值）

## Corrected Claim

Qwen3-27B 在 BF16 精度下的基线困惑度（PPL）在 WikiText-2 数据集上预计处于 6.5-7.0 区间，但需查阅 Qwen3 官方技术报告或 HuggingFace 模型卡片以获取确切数值，当前参考来源未提供直接证据。

## Evidence

[质询]参考来源均讨论的是 Qwen3.5/3.8 等后续版本或部署性能，未提供 Qwen3-27B 在 WikiText-2 上的具体 PPL 数值，且 Qwen3 系列通常报告的是多基准平均分或特定子集，直接引用 6.5-7.0 这一具体区间缺乏直接来源支持，存在版本混淆或数值记忆偏差的风险。 | 经验事实，逻辑自洽（27B 模型 PPL 在此量级合理）但缺来源支持（来源 [1]-[3] 均涉及 Qwen3.5/3.8 或部署性能，未覆盖 Qwen3-27B 的 WikiText-2 PPL 具体数值）。

## Search Query

Qwen3-27B baseline perplexity WikiText-2 BF16 official benchmark

## Retrieval Sources

- {'url': 'https://blog.csdn.net/weixin_30218749/article/details/159560741&rut=835dfb608d57d6c3bfc0c6ffb1ac71d378386a9b61ffc661db7c7ad3b427a7ba', 'type': 'ddg', 'title': 'Qwen3.5-27B GPU算力优化：4090D下FP16 vs BF16推理延迟与显存对比-CSDN博客'}
- {'url': 'https://blog.csdn.net/weixin_28222493/article/details/166045357&rut=6221ed9fad4b3957fcf68b6cb5edd34dd5225c9fee24644f47cd1ffe3142d5de', 'type': 'ddg', 'title': 'Qwen3.8-27B与Qwen3.6-35B-A3B实测：FP8/BF16部署与选型指南'}
- {'url': 'https://aishare.jizhiku.net/archives/52380&rut=9a7a27555c300b3f7308bf93d4ca1c6bb1711e5779280e612774e669596a5a71', 'type': 'ddg', 'title': 'Qwen3.8-27B 实测：BF16/FP8/NVFP4 精度对比与部署优化指南 - AI技能智慧站'}
