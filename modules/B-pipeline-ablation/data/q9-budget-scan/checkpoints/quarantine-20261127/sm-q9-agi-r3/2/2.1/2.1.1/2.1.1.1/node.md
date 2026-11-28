# N120: Qwen3.8-27B 采用 GQA (Grouped Query Attention)，n_layers=32, n_kv_heads=4, head_dim

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N39

## Claim

Qwen3.8-27B 采用 GQA (Grouped Query Attention)，n_layers=32, n_kv_heads=4, head_dim=128；FP16 下每 1k tokens 的 KV Cache 增量计算为 2 (K+V) * 32 * 4 * 128 * 1024 * 2 bytes ≈ 8.4 MB；64k tokens 总 KV Cache 占用约为 537 MB (单序列)，而非 2.5-3.5 GB，表明显存瓶颈主要在于 Batch Size 累积而非单序列长度，max_num_seqs=8 时总 KV Cache 约为 4.3 GB，在 16GB 显存中可容纳权重 (14GB INT4) 但余量极小。

## Corrected Claim

Qwen3.8-27B 采用 GQA，n_layers=32, n_kv_heads=4, head_dim=128；FP16 下每 1k tokens 的 KV Cache 增量计算为 2 * 32 * 4 * 128 * 1024 * 2 bytes = 64 MB；64k tokens 总 KV Cache 占用约为 4 GB (单序列)。

## Evidence

先验知识/题面给定，逻辑校验通过：KV Cache 计算公式 2 * 32 * 4 * 128 * 2 bytes/token = 65,536 bytes/token = 64 KB/token。1k tokens 为 64 MB? 等等，重新计算：2(K+V) * 32(layers) * 4(kv_heads) * 128(head_dim) * 2(bytes per fp16) = 65,536 bytes = 64 KB per token. 1k tokens = 64 MB. 原文说 8.4 MB，这里可能有误？让我们仔细检查原文数值。原文：2 * 32 * 4 * 128 * 1024 * 2 bytes。这里的 1024 是什么？如果是 1k tokens，那么应该是 * 1024 tokens。2*32*4*128*2 = 65536 bytes/token. 65536 * 1024 = 67,108,864 bytes = 64 MB. 原文写的是 8.4 MB。这相差约 7.6 倍。难道 n_kv_heads 不是 4？或者 head_dim 不同？或者 FP16 是 1 byte? 不可能。或者 n_layers 不同？如果 n_layers=4, 则 8MB。但 Qwen3.8-27B 通常层数较多。让我们看 64k tokens 总占用 537 MB。537 MB / 64k = 8.4 KB/token. 这意味着每 token 8.4 KB。8.4 KB = 8400 bytes. 2 * L * H_kv * D * 2 = 8400. L*H_kv*D = 2100. 如果 D=128, L*H_kv = 16.4. 如果 L=32, H_kv=0.5? 不合理。如果 L=16, H_kv=1? 也不合理。如果 H_kv=4, L=4.125? 不合理。如果 H_kv=2, L=8.25? 不合理。如果 H_kv=1, L=16.4? 不合理。看来原文的数值计算存在严重错误。8.4 MB per 1k tokens 意味着 8.4 KB per token。而标准计算 2*32*4*128*2 = 64 KB per token。64 KB * 1024 = 64 MB per 1k tokens。64 MB * 64 = 4096 MB = 4 GB per 64k tokens. 原文说 537 MB per 64k tokens，这与 8.4 MB/1k 一致 (8.4*64=537.6)。但是 8.4 MB/1k 这个数值本身对于 32层 4头 128维 的模型是错误的。正确的应该是 64 MB/1k。因此，原文的数值计算是错误的。虽然 source 是 knowledge，但 challenge 指出数值量级错误（差了近 8 倍），这是一个硬逻辑/计算错误。根据规则，若存在硬逻辑错误（量纲错/内部矛盾），应判 failed。这里的内部矛盾在于：给定的参数 (32, 4, 128) 推导出的结果 (64MB/1k) 与陈述的结果 (8.4MB/1k) 不符。

## Search Query

Qwen 27B GQA configuration layers kv heads head dim
