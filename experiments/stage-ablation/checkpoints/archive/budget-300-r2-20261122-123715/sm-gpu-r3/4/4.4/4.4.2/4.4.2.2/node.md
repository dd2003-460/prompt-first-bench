# N320: 分支2 的修正推荐：满足 Budget > $5000, Quality=Medium, Latency > 20 tok/s 的可行解为 '1x H100 P

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N95

## Claim

分支2 的修正推荐：满足 Budget > $5000, Quality=Medium, Latency > 20 tok/s 的可行解为 '1x H100 PCIe 80GB' 或 '2x RTX 4090 (Tensor Parallel)'。H100 带宽 2039 GB/s, FP8 权重 27GB, 理论吞吐 ≈ 2039/50 ≈ 40 tok/s, 实际 30 tok/s，满足 SLA。H100 价格 ~$30000, TCO 高，但单位吞吐成本可能因高稳定性而优。2x 4090 价格 ~$3200, 满足预算，吞吐 ~30 tok/s (0.75效率)，TCO ~$6000，性价比极高，但存在 N79/N91 提到的多卡故障与 PCIe 通信开销风险。

## Corrected Claim

分支2 的修正推荐：满足 Budget > $5000, Quality=Medium, Latency > 20 tok/s 的可行解为 '1x H100 PCIe 80GB' 或 '2x RTX 4090 (Tensor Parallel)'。H100 带宽 2039 GB/s，FP8 权重 27GB，理论吞吐估算约 40 tok/s，实际可能因 KV Cache 和框架开销降至 25-30 tok/s，满足 SLA。H100 价格 ~$30000，TCO 高，但单位吞吐成本可能因高稳定性而优。2x 4090 价格 ~$3200，满足预算，吞吐估算约 25-30 tok/s（考虑 0.75 效率及通信开销），TCO 需包含电力与运维成本，性价比相对高，但存在多卡故障与 PCIe 通信开销风险。

## Evidence

[质询]H100 PCIe 80GB 的显存带宽通常为 2039 GB/s，但 FP8 权重 27GB 的模型在 H100 上理论吞吐 40 tok/s 的估算过于简化，未考虑 KV Cache 占用、内存访问模式及实际推理框架开销；此外，2x RTX 4090 的 TCO ~$6000 未包含电力、冷却及运维成本，且多卡通信开销在 Tensor Parallel 下可能显著降低实际吞吐。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）

## Search Query

H100 PCIe price 2024 2x RTX 4090 inference throughput benchmark
