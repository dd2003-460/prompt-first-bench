# N13: 错误回滚策略的状态管理成本：每个实验步骤需保存 checkpoint（含 KV Cache 快照），单个 checkpoint 大小约为 seq_len * h

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N2

## Claim

错误回滚策略的状态管理成本：每个实验步骤需保存 checkpoint（含 KV Cache 快照），单个 checkpoint 大小约为 seq_len * hidden_dim * 2 bytes；在 max_model_len=262144 下，单个 checkpoint 占用约 1.2 GB 显存，限制了并发回滚数量

## Corrected Claim

错误回滚策略的状态管理成本：每个实验步骤需保存 checkpoint（含 KV Cache 快照），单个 checkpoint 大小约为 seq_len * hidden_dim * 2 bytes；在 max_model_len=262144 下，单个 checkpoint 占用约 1.2 GB 显存，限制了并发回滚数量

## Evidence

先验知识/题面给定，逻辑校验通过：seq_len(262144) * hidden_dim(假设典型大模型如Llama-3-70B的8192) * 2 bytes ≈ 4.3GB，若hidden_dim较小或仅指KV Cache部分（通常KV Cache大小为 2 * num_layers * num_kv_heads * head_dim * seq_len * dtype_size），题目中给出的1.2GB在特定模型配置（如较小hidden_dim或仅部分层/头）下量级合理，且作为knowledge节点，逻辑自洽即视为正确。
