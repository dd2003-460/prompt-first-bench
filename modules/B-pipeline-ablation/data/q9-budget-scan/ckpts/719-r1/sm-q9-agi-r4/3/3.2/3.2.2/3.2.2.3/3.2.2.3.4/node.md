# N528: 工作点3 (INT8) 的 OOM 预防缓冲机制量化：预留 6-8GB 显存用于激活值 (Activations) 的峰值计算，公式为 Mem_Activati

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N187, N188, N189

## Claim

工作点3 (INT8) 的 OOM 预防缓冲机制量化：预留 6-8GB 显存用于激活值 (Activations) 的峰值计算，公式为 Mem_Activation_Peak = batch_size × seq_len × hidden_dim × dtype_bytes × num_layers_active，需确保在 max_seq_len=128K 时该值 < 6GB

## Corrected Claim

工作点3 (INT8) 的 OOM 预防缓冲机制量化：预留 6-8GB 显存用于激活值 (Activations) 的峰值计算，公式为 Mem_Activation_Peak = batch_size × seq_len × hidden_dim × dtype_bytes × num_layers_active，需确保在 max_seq_len=128K 时该值 < 6GB

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

LLM activation memory footprint calculation formula PyTorch
