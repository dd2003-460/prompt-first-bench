# N152: 方案 B（FP8 KV + 中等上下文）：维持 FP8 KV Cache（1 byte/element，假设当前部署已启用），设置 max_model_len=

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N43

## Claim

方案 B（FP8 KV + 中等上下文）：维持 FP8 KV Cache（1 byte/element，假设当前部署已启用），设置 max_model_len=65536, max_num_seqs=4。单序列 KV 占用 65536 * 128KB = 8GB，总需求 32GB，低于 48.5GB。此方案保持较高精度，支持中等长度推理，是精度与并发的折中点。

## Corrected Claim

方案 B（FP8 KV + 中等上下文）：维持 FP8 KV Cache（1 byte/element，假设当前部署已启用），设置 max_model_len=65536, max_num_seqs=4。单序列 KV 占用 65536 * 128KB = 8GB，总需求 32GB，低于 48.5GB。此方案保持较高精度，支持中等长度推理，是精度与并发的折中点。
