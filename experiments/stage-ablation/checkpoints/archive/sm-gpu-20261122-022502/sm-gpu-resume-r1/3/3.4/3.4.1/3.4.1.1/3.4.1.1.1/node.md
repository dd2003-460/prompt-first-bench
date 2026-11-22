# N723: PCIe 带宽瓶颈量化：RTX 4090 原生支持 PCIe 4.0 x16（~32 GB/s 单向）。若主板仅提供 x8 分叉（~16 GB/s），模型加载时

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N222

## Claim

PCIe 带宽瓶颈量化：RTX 4090 原生支持 PCIe 4.0 x16（~32 GB/s 单向）。若主板仅提供 x8 分叉（~16 GB/s），模型加载时间从 ~2.5s 增至 ~5s（27B BF16 ≈ 54GB），且多卡 KV Cache 同步带宽减半，可能导致 N92 中 4.7 tokens/s 的吞吐估算下降 10-15% [待核验]，需实测验证。

## Corrected Claim

PCIe 带宽瓶颈量化：RTX 4090 原生支持 PCIe 4.0 x16（~32 GB/s 单向）。若主板仅提供 x8 分叉（~16 GB/s），模型加载时间从 ~2.5s 增至 ~5s（27B BF16 ≈ 54GB），且多卡 KV Cache 同步带宽减半，可能导致 N92 中 4.7 tokens/s 的吞吐估算下降 10-15% [待核验]，需实测验证。

## Evidence

先验知识/题面给定，逻辑校验通过：PCIe 4.0 x16 带宽约 32GB/s，x8 减半为 16GB/s；54GB 数据在 32GB/s 下理论传输时间约 1.7s（含开销约 2.5s），在 16GB/s 下理论传输时间约 3.4s（含开销约 5s），量级与陈述一致；带宽减半导致同步开销增加从而降低吞吐符合逻辑。

## Search Query

RTX 4090 PCIe x8 vs x16 inference latency benchmark 27B model
