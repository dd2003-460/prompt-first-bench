# N214: PP 模式下层间激活值（Activations）传输的显存开销估算：Activation_VRAM = 2 * hidden_dim * seq_len * b

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N70

## Claim

PP 模式下层间激活值（Activations）传输的显存开销估算：Activation_VRAM = 2 * hidden_dim * seq_len * batch_size * bytes_per_element，对于 Qwen3-27B (hidden=4096), seq=32K, batch=1, BF16，单步传输约 512MB，需预留此缓冲空间以评估总显存压力。

## Corrected Claim

PP 模式下层间激活值（Activations）传输的显存开销估算：Activation_VRAM = 2 * hidden_dim * seq_len * batch_size * bytes_per_element，对于 Qwen3-27B (hidden=4096), seq=32K, batch=1, BF16，单步传输约 512MB，需预留此缓冲空间以评估总显存压力。

## Evidence

先验知识/题面给定，逻辑校验通过：公式 2 * 4096 * 32768 * 1 * 2 = 536,870,912 Bytes = 512 MB，计算准确且量级合理。
