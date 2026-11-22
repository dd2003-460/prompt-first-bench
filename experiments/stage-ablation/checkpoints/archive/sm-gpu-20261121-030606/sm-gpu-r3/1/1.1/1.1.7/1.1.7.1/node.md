# N205: RTX 4090 FP8 实际权重加载字节数修正：由于 FP8 为 1 字节/参数，27B 模型权重应为 27GB，而非 N19/N7 中可能存在的 13.5G

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N86

## Claim

RTX 4090 FP8 实际权重加载字节数修正：由于 FP8 为 1 字节/参数，27B 模型权重应为 27GB，而非 N19/N7 中可能存在的 13.5GB 误标；N86 的 32.4 tokens/s 计算基于 27GB 权重是物理正确的，但需确认是否包含 GQA 对 KV 的压缩（N130 指出 KV 仅 3.98GB 而非 4.7GB，若采用 N130 修正值，分母变为 27+3.98=30.98GB，吞吐量升至 32.5 tokens/s，差异微小但需统一口径）。

## Corrected Claim

RTX 4090 FP8 实际权重加载字节数修正：由于 FP8 为 1 字节/参数，27B 模型权重应为 27GB，而非 N19/N7 中可能存在的 13.5GB 误标；N86 的 32.4 tokens/s 计算基于 27GB 权重是物理正确的，但需确认是否包含 GQA 对 KV 的压缩（N130 指出 KV 仅 3.98GB 而非 4.7GB，若采用 N130 修正值，分母变为 27+3.98=30.98GB，吞吐量升至 32.5 tokens/s，差异微小但需统一口径）。

## Evidence

先验知识/题面给定，逻辑校验通过：FP8精度下27B模型权重确为27GB，算术推导（27+3.98=30.98GB）及吞吐量微调逻辑自洽。
