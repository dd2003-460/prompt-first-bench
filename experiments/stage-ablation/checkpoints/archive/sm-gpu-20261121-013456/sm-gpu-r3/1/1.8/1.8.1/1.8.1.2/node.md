# N178: 工作点 B（中性价比最优）：标准 Attention + Batch Size=1 + 32K 上下文 + 启用 Gradient Checkpointing（

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N71

## Claim

工作点 B（中性价比最优）：标准 Attention + Batch Size=1 + 32K 上下文 + 启用 Gradient Checkpointing（若微调）或仅推理模式，激活值显存占用稳定在 2.0-3.0 GB，主要开销来自 LayerNorm 残差连接和 FFN 中间层 (4×27B/3≈36B 参数激活)；此配置为多数推理框架（如 vLLM 默认）的基准，TCO 模型中建议采用 2.5 GB 作为保守估计值

## Corrected Claim

工作点 B（中性价比最优）：标准 Attention + Batch Size=1 + 32K 上下文 + 启用 Gradient Checkpointing（若微调）或仅推理模式，激活值显存占用需根据具体模型架构和精度估算，通常显著高于2.0-3.0 GB；主要开销来自FFN中间层和Attention KV Cache；此配置为多数推理框架（如 vLLM 默认）的基准，TCO 模型中建议采用更保守的估计值（如5-10 GB，具体视模型而定）。

## Evidence

[质询]数值量级存疑：对于27B参数模型，即使仅推理（Batch=1），激活值显存占用通常远高于2.0-3.0 GB（取决于具体架构和精度，通常需数GB至十几GB），且'4×27B/3≈36B'的计算逻辑混淆了参数量与激活值大小，FFN中间层激活值大小与参数量无直接线性关系，且LayerNorm残差连接并非主要显存开销来源。 | 经验事实，逻辑自洽但缺来源支持；且数值量级与常规大模型推理显存占用经验不符，存在内部逻辑矛盾（激活值显存与参数量的关系描述错误）。
