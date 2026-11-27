# N195: Apple M2 Ultra 的 192GB 统一内存允许在不使用量化 (BF16) 的情况下完整加载 27B 模型并保留约 138GB 用于 KV Cache

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N60

## Claim

Apple M2 Ultra 的 192GB 统一内存允许在不使用量化 (BF16) 的情况下完整加载 27B 模型并保留约 138GB 用于 KV Cache，支持理论最大上下文长度远超 32K tokens (受限于注意力计算复杂度而非显存)，这是其相对于 24GB/48GB 显存 GPU 方案的核心优势，适合长文档分析场景。

## Corrected Claim

Apple M2 Ultra 的 192GB 统一内存允许在不使用量化 (BF16) 的情况下完整加载 27B 模型并保留约 138GB 用于 KV Cache，支持理论最大上下文长度远超 32K tokens (受限于注意力计算复杂度而非显存)，这是其相对于 24GB/48GB 显存 GPU 方案的核心优势，适合长文档分析场景。

## Evidence

先验知识/题面给定，逻辑校验通过：27B模型BF16权重约54GB，192GB-54GB=138GB，数值量级与逻辑自洽。
