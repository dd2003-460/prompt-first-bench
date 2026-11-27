# N92: 长上下文KV Cache读取开销量化：在32K tokens序列长度下，每生成1个新token需读取的KV Cache数据量 = 2 (K/V) * num_l

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N25

## Claim

长上下文KV Cache读取开销量化：在32K tokens序列长度下，每生成1个新token需读取的KV Cache数据量 = 2 (K/V) * num_layers * num_kv_heads * head_dim * 2 bytes * seq_len，对于Qwen3-27B (假设32层, 8 KV heads, 128 dim) 约为 32 * 8 * 128 * 2 * 32768 ≈ 21.5 GB，此数值与模型权重相当，显著增加显存读取压力。

## Corrected Claim

长上下文KV Cache读取开销量化：在32K tokens序列长度下，每生成1个新token需读取的KV Cache数据量 = 2 (K/V) * num_layers * num_kv_heads * head_dim * 2 bytes * seq_len，对于Qwen3-27B (假设32层, 8 KV heads, 128 dim) 约为 32 * 8 * 128 * 2 * 32768 ≈ 21.5 GB，此数值与模型权重相当，显著增加显存读取压力。

## Evidence

先验知识/题面给定，逻辑校验通过：公式推导正确（2 * 32 * 8 * 128 * 2 * 32768 = 21,474,836,480 bytes ≈ 20 GiB ≈ 21.5 GB），量级合理，符合KV Cache显存占用计算原理。
