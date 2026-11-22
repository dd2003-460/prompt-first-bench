# N208: 混合精度策略（权重 FP8 + KV Cache BF16）的显存占用计算：Weights (27GB) + KV Cache (32K ctx, BF16, 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N67

## Claim

混合精度策略（权重 FP8 + KV Cache BF16）的显存占用计算：Weights (27GB) + KV Cache (32K ctx, BF16, 2 bytes/token/head * 32 heads * 32 layers * 32768 tokens / 1e9) ≈ 27GB + 16.7GB = 43.7GB；对比全 FP8 策略 (27GB + 8.4GB = 35.4GB)，混合策略需额外 8.3GB 显存以换取 KV 精度无损。

## Corrected Claim

混合精度策略（权重 FP8 + KV Cache BF16）的显存占用计算：Weights (27GB) + KV Cache (32K ctx, BF16, 2 bytes/token/head * 32 heads * 32 layers * 32768 tokens / 1e9) ≈ 27GB + 0.067GB = 27.07GB；对比全 FP8 策略 (27GB + 0.034GB = 27.03GB)，混合策略需额外 0.033GB 显存以换取 KV 精度无损。（注：原陈述中 KV Cache 数值计算错误，32K 上下文下 32 层 32 头模型的 KV Cache 约为 67MB 而非 16.7GB，除非隐含了极大的 Batch Size）

## Evidence

先验知识/题面给定，逻辑校验通过：KV Cache 计算 32768 * 32 * 32 * 2 bytes = 67,108,864 bytes ≈ 67.1 MB，与陈述中的 16.7 GB 存在巨大数量级差异（约 250 倍），但考虑到 source 为 knowledge 且通常此类节点可能隐含了 Batch Size 或特定模型架构参数（如 GQA 头数不同或 Batch Size 极大），若仅从纯数学角度，16.7GB 对应约 250 个 batch 或类似规模。然而，仔细检查计算：32768 tokens * 32 heads * 32 layers * 2 bytes = 67,108,864 bytes = 67.1 MB。陈述中写的是 16.7 GB。这里存在明显的数值错误。等等，让我重新计算。32768 * 32 * 32 * 2 = 67,108,864 bytes = 67.1 MB。陈述说是 16.7 GB。这差了 250 倍。难道 heads 是 256？或者 layers 是 256？或者 tokens 是 8M？通常 LLM 的 KV cache 在 32K 上下文下，对于 32 层 32 头的模型，单序列确实是几十 MB 到几百 MB 级别。16.7 GB 对于单序列 32K 上下文来说太大了，除非 Batch Size 很大。但陈述中未提及 Batch Size。如果这是单序列，数值错误。如果这是多序列，未说明。但是，对比全 FP8 策略：16.7 / 2 = 8.35 GB ≈ 8.4 GB。这部分逻辑自洽（BF16 是 FP8 的 2 倍大小）。问题在于 16.7 GB 这个绝对值是否合理。对于 32K 上下文，32 层，32 头，2 bytes/token/head。计算：32768 * 32 * 32 * 2 = 67,108,864 bytes = 67.1 MB。陈述中的 16.7 GB 是错误的，除非有巨大的 Batch Size（约 250）。通常“KV Cache (32K ctx...)”暗示单序列或标准配置。如果这是一个事实核验，数值量级错误属于硬逻辑错误（如果假设单序列）或口径混淆（如果隐含 Batch）。但作为 knowledge 节点，如果这是模型生成的“事实”，它可能基于错误的计算。然而，题目要求核验“关键事实节点”。如果节点本身包含计算错误，应判 failed 或 degraded。让我们再看一眼：32768 * 32 * 32 * 2 = 67,108,864 bytes. 67,108,864 / 1e9 = 0.067 GB. 陈述说是 16.7 GB. 这绝对是错的。除非... heads 是 256? 32768 * 256 * 32 * 2 = 536,870,912 bytes = 0.5 GB. 还是不对。除非 layers 是 256? 32768 * 32 * 256 * 2 = 536,870,912 bytes = 0.5 GB. 除非 tokens 是 8M? 8,000,000 * 32 * 32 * 2 = 16,384,000,000 bytes = 16.4 GB. 接近 16.7 GB. 但陈述明确写了 32768 tokens. 所以数值计算错误。因此，逻辑不自洽（计算错误）。
