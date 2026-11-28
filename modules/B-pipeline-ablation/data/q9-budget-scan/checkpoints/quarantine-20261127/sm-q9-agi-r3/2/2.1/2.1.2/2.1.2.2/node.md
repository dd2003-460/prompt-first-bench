# N124: 滑动窗口策略（Window Size = 8192 tokens, Step = 4096）在处理 128k 上下文时，相比全量上下文推理，可将 KV Cach

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N40

## Claim

滑动窗口策略（Window Size = 8192 tokens, Step = 4096）在处理 128k 上下文时，相比全量上下文推理，可将 KV Cache 峰值显存占用降低约 60%（从 ~12GB 降至 ~4.8GB），从而允许 Batch Size 从 2 提升至 8，整体吞吐量提升 3-4 倍，但需额外 0.5-1 秒的窗口拼接与去重处理时间。

## Corrected Claim

滑动窗口策略在处理长上下文时，通过限制KV Cache的有效长度或复用机制，可显著降低峰值显存占用（具体比例依模型而定），从而允许更大的Batch Size并提升整体吞吐量，但会引入额外的窗口管理开销。

## Evidence

[质询]数值量级与因果关系存疑：KV Cache 显存占用主要取决于序列长度和模型架构，滑动窗口通常限制的是注意力计算范围或存储的历史长度，但‘降低60%’这一具体比例以及由此带来的‘Batch Size 2->8’和‘吞吐量3-4倍’的提升缺乏通用理论支撑，高度依赖特定模型（如LLaMA-2 7B vs 70B）和硬件配置，属于特定实验数据而非普适规律。 | 先验知识/题面给定，逻辑校验通过（显存减少确实允许更大Batch，进而提升吞吐，逻辑链条自洽），但具体数值（60%, 12GB->4.8GB, 3-4x）为经验事实，无外部来源支持，故降级。

## Search Query

sliding window inference KV cache memory reduction throughput boost LLM
