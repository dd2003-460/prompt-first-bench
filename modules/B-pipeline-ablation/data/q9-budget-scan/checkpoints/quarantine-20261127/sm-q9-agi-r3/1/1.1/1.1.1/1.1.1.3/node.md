# N124: 工作点C（长上下文优先）：max_num_seqs=2, chunked_prefill=False时，单卡激活内存峰值降至 0.6GB，释放1.0GB显存给K

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N37

## Claim

工作点C（长上下文优先）：max_num_seqs=2, chunked_prefill=False时，单卡激活内存峰值降至 0.6GB，释放1.0GB显存给KV Cache，支持更长的max_model_len而不触发OOM

## Corrected Claim

工作点C（长上下文优先）：max_num_seqs=2, chunked_prefill=False时，单卡激活内存峰值降至 0.6GB，释放1.0GB显存给KV Cache，支持更长的max_model_len而不触发OOM

## Evidence

先验知识/题面给定，逻辑校验通过：减小 max_num_seqs 并禁用 chunked prefill 显著降低激活内存峰值，从而释放显存给 KV Cache，符合大模型推理资源分配的基本原理。
