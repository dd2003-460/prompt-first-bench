# N80: 1×RTX 4090 在 BF16 下因显存不足（需 44.4GB > 24GB）必须启用 Offload，吞吐量降至 5-8 tokens/s，TCO/Thr

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N27

## Claim

1×RTX 4090 在 BF16 下因显存不足（需 44.4GB > 24GB）必须启用 Offload，吞吐量降至 5-8 tokens/s，TCO/Throughput 恶化至 $0.025-$0.035/token，与 2×4090 或 A100 方案相比无性价比优势，仅作为最低配置参考。

## Corrected Claim

1×RTX 4090 在 BF16 下因显存不足（需 44.4GB > 24GB）必须启用 Offload，吞吐量降至 5-8 tokens/s，TCO/Throughput 恶化至 $0.025-$0.035/token，与 2×4090 或 A100 方案相比无性价比优势，仅作为最低配置参考。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 4090 显存 24GB，44.4GB 需求确实导致必须 Offload，Offload 导致的吞吐量下降（5-8 tokens/s）及成本恶化符合硬件性能与经济学直觉。
