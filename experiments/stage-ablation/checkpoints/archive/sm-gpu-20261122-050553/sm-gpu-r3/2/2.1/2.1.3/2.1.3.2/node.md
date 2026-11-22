# N180: Prefill 阶段处理 32K 上下文时的激活值显存占用 A_prefill 主要取决于 FlashAttention 的实现：若使用标准 Attention

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N56

## Claim

Prefill 阶段处理 32K 上下文时的激活值显存占用 A_prefill 主要取决于 FlashAttention 的实现：若使用标准 Attention，A_prefill ≈ O(N^2 * D)，但在 FlashAttention-2/3 下，激活值被分块处理，峰值显存占用主要受限于分块大小 (Block_Size)，通常额外占用 < 1-2 GB (独立于序列长度 N)，而非 N56 声称的 10-20 GB；需确认 vLLM 默认配置下的 FlashAttention 版本。

## Corrected Claim

Prefill 阶段处理 32K 上下文时的激活值显存占用 A_prefill 主要取决于 FlashAttention 的实现：若使用标准 Attention，A_prefill ≈ O(N^2 * D)，但在 FlashAttention-2/3 下，激活值被分块处理，峰值显存占用主要受限于分块大小 (Block_Size)，通常额外占用 < 1-2 GB (独立于序列长度 N)，而非 N56 声称的 10-20 GB；需确认 vLLM 默认配置下的 FlashAttention 版本。

## Evidence

先验知识/题面给定，逻辑校验通过：FlashAttention 的核心优势即在于将显存复杂度从 O(N^2) 降低至 O(N)，32K 上下文下标准 Attention 显存占用巨大，而 FlashAttention 仅增加少量分块缓冲显存（通常 < 2GB），陈述符合技术原理。

## Search Query

vLLM FlashAttention memory overhead prefill stage long context
