# N292: 2x RTX 4090 TP=2 方案的通信开销量化：每层 All-Reduce 数据量为 2 * Batch_Size * Seq_Length * Hidd

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N88, N89, N90

## Claim

2x RTX 4090 TP=2 方案的通信开销量化：每层 All-Reduce 数据量为 2 * Batch_Size * Seq_Length * Hidden_Dim * 2bytes。在 Seq_Length=32768, Hidden_Dim=4096, Batch_Size=1 时，每层通信数据量约为 2 * 1 * 32768 * 4096 * 2 = 512MB。PCIe 4.0 x16 有效带宽约 16-22 GB/s，单次 All-Reduce 延迟约 512MB / 18GB/s ≈ 28ms。54 层总通信延迟约 1.5s，导致吞吐量显著低于单卡方案。

## Corrected Claim

2x RTX 4090 TP=2 方案的通信开销量化：每层 All-Reduce 数据量为 2 * Batch_Size * Seq_Length * Hidden_Dim * 2bytes。在 Seq_Length=32768, Hidden_Dim=4096, Batch_Size=1 时，每层通信数据量约为 2 * 1 * 32768 * 4096 * 2 = 512MB。PCIe 4.0 x16 有效带宽约 16-22 GB/s，单次 All-Reduce 延迟约 512MB / 18GB/s ≈ 28ms。54 层总通信延迟约 1.5s，导致吞吐量显著低于单卡方案。

## Evidence

先验知识/题面给定，逻辑校验通过：数据量计算 (2*1*32768*4096*2=512MB) 正确，PCIe 4.0 带宽及延迟估算符合工程常识，All-Reduce 通信量公式在 TP=2 场景下成立。
