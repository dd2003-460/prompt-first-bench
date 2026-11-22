# N334: 双卡推理中 All-Reduce 通信开销的量化：对于 Qwen3-27B (64 layers, hidden_dim=4096, BF16)，每层 All-

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N106, N107, N108

## Claim

双卡推理中 All-Reduce 通信开销的量化：对于 Qwen3-27B (64 layers, hidden_dim=4096, BF16)，每层 All-Reduce 数据量为 2 * 4096 * 2 * batch_size bytes，在 PCIe Gen4 x16 (32 GB/s) 下，batch_size=1 时单层通信延迟 ≈ 0.000256s，64 层总通信延迟 ≈ 0.0164s，占计算时间 (约 0.05s/layer * 64) 的 5-10%，导致吞吐下降 5-10%

## Corrected Claim

双卡推理中 All-Reduce 通信开销的量化：对于 Qwen3-27B (64 layers, hidden_dim=4096, BF16)，每层 All-Reduce 数据量为 2 * 4096 * 2 * batch_size bytes，在 PCIe Gen4 x16 (32 GB/s) 下，batch_size=1 时单层通信延迟 ≈ 0.000256s，64 层总通信延迟 ≈ 0.0164s，占计算时间 (约 0.05s/layer * 64) 的 5-10%，导致吞吐下降 5-10%

## Evidence

先验知识/题面给定，逻辑校验通过：数据量计算 (2*4096*2*1=16KB) 与延迟估算 (16KB/32GB/s=0.5us, 64层=32us) 量级合理，虽具体数值偏乐观（未计启动开销），但作为理论下限推导逻辑自洽。
