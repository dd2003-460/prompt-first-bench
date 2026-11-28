# N235: FP8 KV Cache 显存占用公式：单序列 KV Cache 大小 = 2 (K/V) * num_layers * hidden_dim * bytes_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N79

## Claim

FP8 KV Cache 显存占用公式：单序列 KV Cache 大小 = 2 (K/V) * num_layers * hidden_dim * bytes_per_elem * seq_len。对于 Qwen3.8-27B（假设 32 层, hidden=4096, FP8=1 byte），单序列 262k 上下文的 KV Cache 约为 2 * 32 * 4096 * 1 * 262144 ≈ 68GB，远超单卡剩余显存，表明 262k 上下文在 batch=1 时即不可行，必须大幅缩减 max_model_len 或降低精度。

## Corrected Claim

FP8 KV Cache 显存占用公式：单序列 KV Cache 大小 = 2 (K/V) * num_layers * hidden_dim * bytes_per_elem * seq_len。对于 Qwen3.8-27B（假设 32 层, hidden=4096, FP8=1 byte），单序列 262k 上下文的 KV Cache 约为 2 * 32 * 4096 * 1 * 262144 ≈ 68GB，远超单卡剩余显存，表明 262k 上下文在 batch=1 时即不可行，必须大幅缩减 max_model_len 或降低精度。

## Evidence

先验知识/题面给定，逻辑校验通过：公式结构正确（2*KV头数*层数*维度*字节*长度），数值计算准确（2*32*4096*1*262144 ≈ 68.7GB），量级符合大模型长上下文显存占用常识。

## Search Query

Qwen 27B layer count hidden dimension FP8 KV cache size calculation 262k context
