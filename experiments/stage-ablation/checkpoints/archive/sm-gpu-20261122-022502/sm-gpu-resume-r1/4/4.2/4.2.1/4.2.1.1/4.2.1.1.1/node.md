# N792: 2x RTX 4090 在 PCIe 4.0 x16 下，单卡带宽为 64 GB/s，但双卡间通信需通过 CPU 中转或 P2P (若支持)。Qwen3-27B

- **status**: degraded
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N247

## Claim

2x RTX 4090 在 PCIe 4.0 x16 下，单卡带宽为 64 GB/s，但双卡间通信需通过 CPU 中转或 P2P (若支持)。Qwen3-27B INT4 权重约 13.5 GB，若采用张量并行 (Tensor Parallelism)，每层激活值传输量约为 32768 tokens * 4096 hidden * 2 bytes = 268 MB/层。64 层总传输量 17 GB，耗时约 17GB / 64GB/s = 0.27 秒/批次，这将显著拖慢 Decode 阶段，实际吞吐可能降至 40-50 tokens/s。

## Corrected Claim

2x RTX 4090 在 PCIe 4.0 x16 下，单卡带宽为 64 GB/s。Qwen3-27B INT4 权重约 13.5 GB。若采用张量并行 (Tensor Parallelism)，每层激活值传输量取决于 batch size（例如 batch=1 时约为 8KB/层），64 层总传输量极小，通信开销在 Decode 阶段通常可忽略。实际吞吐主要受限于计算和内存带宽，而非 PCIe 通信，40-50 tokens/s 的估计缺乏合理依据。

## Evidence

[质询]计算逻辑存在严重错误：1. 张量并行（TP）中，每层激活值传输量应为 batch_size * hidden_size * dtype_size，而非 32768 * 4096 * 2。若 batch_size 为 1，传输量仅为 8KB/层，64层总计约 0.5MB，耗时微秒级，远非 0.27秒。2. 即使按错误公式计算，17GB/64GB/s = 0.265s 是单次前向传播的通信时间，但 Decode 阶段是逐 token 生成的，每生成一个 token 需执行一次前向传播。若每 token 耗时 0.27s，则吞吐约为 3.7 tokens/s，而非 40-50 tokens/s。3. RTX 4090 支持 P2P，但 PCIe 4.0 x16 带宽为 64GB/s 是单向理论值，实际有效带宽更低，且 TP 通信通常使用 AllReduce，通信量需乘以 2 或 4（取决于实现），但核心错误在于将 batch 维度的 32768 误用为每层固定传输量，导致量级错误。 | 逻辑校验失败：激活值传输量计算错误（混淆 batch size 与固定层传输量），且吞吐推导与耗时计算矛盾（0.27s/token 对应 ~3.7 tokens/s，而非 40-50 tokens/s）。

## Search Query

Tensor parallelism PCIe bandwidth bottleneck LLM inference
