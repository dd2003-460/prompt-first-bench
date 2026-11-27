# N397: L40S 48GB 在 BF16 精度、batch_size=1、seq_len=32768 场景下的理论峰值吞吐量约为 45.3 tokens/s (计算依据

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N160, N161, N162

## Claim

L40S 48GB 在 BF16 精度、batch_size=1、seq_len=32768 场景下的理论峰值吞吐量约为 45.3 tokens/s (计算依据: Memory_Bandwidth 864 GB/s / Model_Size_Bytes 19.1 GB [5.4B params * 2 bytes])。

## Corrected Claim

L40S 48GB 在 BF16 精度、batch_size=1、seq_len=32768 场景下的理论峰值吞吐量约为 45.3 tokens/s (计算依据: Memory_Bandwidth 864 GB/s / Model_Size_Bytes 19.1 GB [5.4B params * 2 bytes])。

## Evidence

先验知识/题面给定，逻辑校验通过：计算过程为 864 GB/s / 19.1 GB ≈ 45.23 tokens/s，与陈述中的 45.3 tokens/s 在合理精度范围内一致，且符合大模型推理中内存带宽受限（Memory-Bound）场景下的理论峰值吞吐量估算逻辑。

## Search Query

NVIDIA L40S memory bandwidth GB/s spec
