# N279: 激活值 (Activations) 峰值显存计算的批次依赖性：在 batch_size=1, seq_len=32K, hidden_size=4096, BF

- **status**: pending
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N102

## Claim

激活值 (Activations) 峰值显存计算的批次依赖性：在 batch_size=1, seq_len=32K, hidden_size=4096, BF16 下，中间激活值（如 Attention 输出、FFN 中间层）峰值约为 hidden_size * seq_len * dtype_size * factor。Factor 取决于框架优化（如 Flash Attention 减少中间存储），保守估计 factor=2 (前向/反向或多次中间层)，则 4096 * 32768 * 2 * 2 / 1e9 = 0.54GB。若 batch_size=4，激活值线性增加至 2.16GB，这将显著压缩单卡 4090 的 KV Cache 余量。

## Corrected Claim

激活值 (Activations) 峰值显存计算的批次依赖性：在 batch_size=1, seq_len=32K, hidden_size=4096, BF16 下，中间激活值（如 Attention 输出、FFN 中间层）峰值约为 hidden_size * seq_len * dtype_size * factor。Factor 取决于框架优化（如 Flash Attention 减少中间存储），保守估计 factor=2 (前向/反向或多次中间层)，则 4096 * 32768 * 2 * 2 / 1e9 = 0.54GB。若 batch_size=4，激活值线性增加至 2.16GB，这将显著压缩单卡 4090 的 KV Cache 余量。

## Evidence

父节点级核验未通过：不完备（子节点仅覆盖了父节点中 batch_size=1 且特定框架优化（Flash Attention v2）下的情况，缺失了父节点明确提到的 batch_size=4 线性增长情形，也未涵盖非 Flash Attention 或不同 factor 的保守估计场景，导致对父节点‘批次依赖性’及‘不同框架优化影响’的覆盖不全。）
