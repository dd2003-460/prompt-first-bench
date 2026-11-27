# N46: 激活值显存估算：对于 Qwen3-27B (hidden_size=4096, seq_len=32K)，单次推理的激活值显存 ≈ seq_len × hidd

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N8, N9, N10

## Claim

激活值显存估算：对于 Qwen3-27B (hidden_size=4096, seq_len=32K)，单次推理的激活值显存 ≈ seq_len × hidden_size × dtype_size × (1 + 2/num_kv_heads) + 中间层缓冲，在 BF16 下约为 0.25GB - 0.5GB，在 FP8/INT8 下减半。

## Corrected Claim

激活值显存估算：对于 Qwen3-27B (hidden_size=4096, seq_len=32K)，若仅计算单层激活值，BF16 下约为 0.25GB；若考虑全模型（约 48-60 层）的激活值存储，显存占用将显著增加，通常在数 GB 量级，具体取决于是否启用激活检查点（Activation Checkpointing）等优化技术。

## Evidence

[质询]数值量级与公式推导存在矛盾：若按公式 seq_len × hidden_size × dtype_size 计算，32K × 4096 × 2 bytes ≈ 256MB (0.25GB)，这仅对应单层或极少量层的激活值。对于 27B 模型（通常有 40-60 层），若需保留所有层激活值用于反向传播或长序列推理，显存占用应远高于 0.5GB（通常为数 GB 至数十 GB）。该陈述可能混淆了'单层激活'与'全模型推理激活'，或者隐含了极端的内存优化假设（如仅保留 KV Cache 且忽略中间层缓冲），但未在公式中体现层数因子，导致公式与结论数值不匹配。 | 先验知识/题面给定，逻辑校验未通过：公式缺少层数（num_layers）因子，导致计算结果（~0.25GB）与 27B 模型全层激活值的典型量级（通常 >1GB）不符，存在内部逻辑矛盾。

## Search Query

LLM inference activation memory footprint calculation formula
