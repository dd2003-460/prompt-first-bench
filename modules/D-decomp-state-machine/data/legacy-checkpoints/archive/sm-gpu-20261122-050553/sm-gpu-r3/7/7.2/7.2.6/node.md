# N307: AMD Radeon PRO W7900 在 BF16 精度下运行 Qwen3-27B 的显存容量验证：BF16 权重 54GB 超过 48GB 物理显存，必须

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N103, N104, N105

## Claim

AMD Radeon PRO W7900 在 BF16 精度下运行 Qwen3-27B 的显存容量验证：BF16 权重 54GB 超过 48GB 物理显存，必须启用 Offloading 或量化，若强制使用 BF16 且启用 PagedAttention，需将上下文限制至 ~16K tokens 以避免 OOM，这与 32K 容量下限冲突。

## Corrected Claim

AMD Radeon PRO W7900 (48GB) 在 BF16 精度下运行 Qwen3-27B (权重约 54GB) 时，因权重超出物理显存，必须启用 Offloading 或量化。若启用 Offloading，剩余显存用于 KV Cache，具体可支持的上下文长度取决于模型架构参数及显存分配策略，而非固定由 PagedAttention 限制为 16K tokens。

## Evidence

[质询]数值量级与逻辑推导存在潜在偏差：1. Qwen3-27B 的 BF16 权重约为 54GB (27B * 2 bytes)，确实超过 48GB 显存，但通常 27B 模型在 BF16 下无法直接装入 48GB 卡，必须量化或 Offload，这点陈述正确。2. 然而，陈述中关于 'PagedAttention 需将上下文限制至 ~16K tokens 以避免 OOM' 的推导逻辑不严谨。PagedAttention 本身是显存管理技术，旨在提高显存利用率，而非通过限制上下文长度来避免 OOM（OOM 通常由权重+KV Cache 总大小超过物理显存引起）。若权重已 Offload，KV Cache 占用显存，16K tokens 的 KV Cache 大小取决于层数和头数，对于 27B 模型，16K 上下文的 KV Cache 可能仅需几 GB，远小于 48GB 剩余空间（假设权重 Offload 后显存空闲）。因此，'必须限制至 16K' 这一具体数值缺乏严谨推导，且与 '32K 容量下限冲突' 的结论可能基于错误的显存占用估算。 | 先验知识/题面给定，逻辑校验发现 PagedAttention 与上下文长度限制避免 OOM 的因果关系描述不准确，且 16K 的具体阈值缺乏通用推导支持，属于经验性估算且可能存在量级误判。

## Search Query

AMD Radeon PRO W7900 48GB BF16 Qwen3-27B memory overflow context limit
