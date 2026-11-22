# N154: 若坚持在 32GB 单卡 (RTX 5090) 上运行 32K 上下文，必须采用混合精度策略：权重 FP8 (27.18GB) + KV Cache INT8/

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N42

## Claim

若坚持在 32GB 单卡 (RTX 5090) 上运行 32K 上下文，必须采用混合精度策略：权重 FP8 (27.18GB) + KV Cache INT8/FP8 (12.88GB) + 激活 BF16，总占用约 43GB，仍超出 32GB；唯一可行方案是将上下文截断至 16K (KV Cache 6.44GB) 或使用 4-bit 量化权重 (13.59GB) + BF16 KV (25.76GB) = 42.79GB (仍超)，因此 32GB 单卡在 32K 上下文下几乎无法通过纯量化解决，需依赖 KV Cache 共享或外部内存卸载 (Offloading)，这将导致 TPOT 增加 50-100%。

## Corrected Claim

若坚持在 32GB 单卡 (RTX 5090) 上运行 32K 上下文，采用混合精度策略（如 FP8 权重 + INT8/FP8 KV Cache）总占用约 40GB 以上，超出 32GB 显存。即使采用 4-bit 量化权重 (约 13.6GB) + BF16 KV Cache (约 25.8GB)，总占用约 39.4GB，仍超出 32GB。因此，32GB 单卡在 32K 上下文下难以仅通过常规量化解决，通常需依赖 KV Cache 共享、外部内存卸载 (Offloading) 或更激进的 KV Cache 量化，这将导致 TPOT 显著增加。

## Evidence

[质询]数值计算存在内部矛盾：4-bit 量化权重 (13.59GB) + BF16 KV Cache (25.76GB) 的总和应为 39.35GB，而非陈述中的 42.79GB；此外，'几乎无法通过纯量化解决'的结论过于绝对，未考虑更激进的量化组合（如 4-bit 权重 + 4-bit/INT8 KV Cache）可能使总占用降至 32GB 以下。 | 先验知识/题面给定，逻辑校验发现数值加和错误（13.59+25.76≠42.79）及结论绝对化问题，故降级。

## Search Query

LLM inference 32K context 32GB VRAM hybrid precision offloading latency penalty
