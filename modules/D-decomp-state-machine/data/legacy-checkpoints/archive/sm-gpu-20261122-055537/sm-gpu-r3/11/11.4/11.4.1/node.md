# N382: 2x RTX 4090 TP=2 在 seq_len=32768, batch_size=1 时，每层 All-Reduce 的数据量为 2 * 1 * 327

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N120

## Claim

2x RTX 4090 TP=2 在 seq_len=32768, batch_size=1 时，每层 All-Reduce 的数据量为 2 * 1 * 32768 * 4096 * 2 bytes ≈ 512 MB。在 PCIe 4.0 x16 有效带宽 ~20 GB/s 下，单次 All-Reduce 耗时 ≈ 25.6 ms。Qwen3-27B 共 54 层，每层 2 次 All-Reduce，总通信耗时 ≈ 54 * 2 * 25.6 ms ≈ 2.76 s/token。

## Corrected Claim

2x RTX 4090 TP=2 在 seq_len=32768, batch_size=1 时，每层 All-Reduce 的数据量为 2 * 1 * 32768 * 4096 * 2 bytes ≈ 512 MB。在 PCIe 4.0 x16 有效带宽 ~20 GB/s 下，单次 All-Reduce 耗时 ≈ 25.6 ms。Qwen3-27B 共 54 层，每层 2 次 All-Reduce，总通信耗时 ≈ 54 * 2 * 25.6 ms ≈ 2.76 s/token。

## Evidence

先验知识/题面给定，逻辑校验通过：数据量计算 (2*1*32768*4096*2 = 536,870,912 bytes ≈ 512 MiB) 正确；耗时计算 (512MB / 20GB/s = 25.6ms) 正确；总耗时 (54*2*25.6ms = 2764.8ms ≈ 2.76s) 正确。
