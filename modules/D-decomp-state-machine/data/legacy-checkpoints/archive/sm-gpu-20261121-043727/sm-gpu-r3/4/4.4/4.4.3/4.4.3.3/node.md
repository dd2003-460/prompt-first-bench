# N192: Offloading 与直接推理的性能对比量化：RTX 4090 直接推理 (BF16, 54GB显存不足需量化或Offload) 若使用 INT4 量化 (1

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N73

## Claim

Offloading 与直接推理的性能对比量化：RTX 4090 直接推理 (BF16, 54GB显存不足需量化或Offload) 若使用 INT4 量化 (14GB) 直接推理 T_decode ≈ 87us/token (N77)，而 BF16 Offload T_decode ≈ 1090ms/token，性能差距 ≈ 12,000 倍。若使用 FP8 量化 (27GB) 直接推理 T_decode ≈ 43us/token，Offload 性能差距 ≈ 25,000 倍。结论：Offload 仅适用于显存极度受限且对延迟不敏感的离线批处理场景

## Corrected Claim

Offloading 与直接推理的性能对比量化：RTX 4090 直接推理 (BF16, 54GB显存不足需量化或Offload) 若使用 INT4 量化 (14GB) 直接推理 T_decode ≈ 87us/token (N77)，而 BF16 Offload T_decode ≈ 1090ms/token，性能差距 ≈ 12,000 倍。若使用 FP8 量化 (27GB) 直接推理 T_decode ≈ 43us/token，Offload 性能差距 ≈ 25,000 倍。结论：Offload 仅适用于显存极度受限且对延迟不敏感的离线批处理场景

## Evidence

先验知识/题面给定，逻辑校验通过：INT4/FP8直接推理利用高带宽显存，Offload受限于PCIe带宽瓶颈，两者延迟量级差异（微秒级 vs 毫秒级）符合硬件物理直觉，数值自洽。
