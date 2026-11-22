# N161: 2x RTX 4090 通过 PCIe 4.0 x16 互联时，单向理论带宽为 32 GB/s (1576 MB/s * 20 ≈ 31.5 GB/s)，双向全

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N52

## Claim

2x RTX 4090 通过 PCIe 4.0 x16 互联时，单向理论带宽为 32 GB/s (1576 MB/s * 20 ≈ 31.5 GB/s)，双向全双工约 63 GB/s。对于 BF16 模型 (54GB)，若采用 Tensor Parallelism (TP)，每层 Attention 输出需跨卡 All-Reduce，每次 All-Reduce 传输数据量为 batch_size * seq_len * hidden_size * 2 bytes。在 batch_size=1, seq_len=32K, hidden_size=4096 下，单次通信量 ≈ 1 * 32768 * 4096 * 2 = 268 MB。

## Corrected Claim

2x RTX 4090 通过 PCIe 4.0 x16 互联时，单向理论带宽为 32 GB/s (1576 MB/s * 20 ≈ 31.5 GB/s)，双向全双工约 63 GB/s。对于 BF16 模型 (54GB)，若采用 Tensor Parallelism (TP)，每层 Attention 输出需跨卡 All-Reduce，每次 All-Reduce 传输数据量为 batch_size * seq_len * hidden_size * 2 bytes。在 batch_size=1, seq_len=32K, hidden_size=4096 下，单次通信量 ≈ 1 * 32768 * 4096 * 2 = 268 MB。

## Evidence

先验知识/题面给定，逻辑校验通过：PCIe 4.0 x16 单向带宽约 32 GB/s 符合标准规格；All-Reduce 通信量计算 1 * 32768 * 4096 * 2 bytes = 268,435,456 bytes ≈ 268 MB 数学推导正确。
