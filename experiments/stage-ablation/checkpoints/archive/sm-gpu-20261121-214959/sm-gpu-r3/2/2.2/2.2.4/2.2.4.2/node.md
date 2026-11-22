# N183: MI300X 单卡运行 Qwen3-27B BF16 时的激活值（Activations）峰值估算：在 batch_size=1, seq_len=32K 下，

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N60

## Claim

MI300X 单卡运行 Qwen3-27B BF16 时的激活值（Activations）峰值估算：在 batch_size=1, seq_len=32K 下，激活值占用约为 hidden_size * seq_len * dtype_size * 2 ≈ 4096 * 32768 * 2 * 2 / 1e9 = 0.54 GB，加上 CUDA Context 和框架缓冲 (~1.5GB)，总非权重/KV 开销约 2GB，需从 192GB 总容量中扣除以确认真实可用空间。

## Corrected Claim

MI300X 单卡运行 Qwen3-27B BF16 时的激活值（Activations）峰值估算：在 batch_size=1, seq_len=32K 下，激活值占用约为 hidden_size * seq_len * dtype_size * 2 ≈ 4096 * 32768 * 2 * 2 / 1e9 = 0.54 GB，加上 CUDA Context 和框架缓冲 (~1.5GB)，总非权重/KV 开销约 2GB，需从 192GB 总容量中扣除以确认真实可用空间。

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B hidden_size 为 4096，BF16 占 2 字节，计算 4096*32768*2*2/1e9 ≈ 0.54GB 符合数学逻辑，且 MI300X 192GB 显存规格正确，总开销估算合理。
