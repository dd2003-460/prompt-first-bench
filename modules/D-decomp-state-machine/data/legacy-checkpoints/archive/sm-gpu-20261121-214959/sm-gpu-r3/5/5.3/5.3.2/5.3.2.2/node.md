# N279: 激活值 (Activations) 峰值显存计算的批次依赖性：在 batch_size=1, seq_len=32K, hidden_size=4096, BF

- **status**: verified
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

先验知识/题面给定，逻辑校验通过：数值计算 4096 * 32768 * 2 * 2 / 1e9 ≈ 0.54GB 正确，batch_size 线性扩展逻辑自洽，符合 Transformer 激活值显存估算的基本原理。
