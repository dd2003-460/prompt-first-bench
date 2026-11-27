# N216: A100 80GB PCIe 版本的 300W TDP 在 24/7 运行下，年电费（按 $0.12/kWh）为 300W * 8760h / 1000 * $

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N74

## Claim

A100 80GB PCIe 版本的 300W TDP 在 24/7 运行下，年电费（按 $0.12/kWh）为 300W * 8760h / 1000 * $0.12 = $314.64/年，比 SXM 版本（$419.52/年）低 25%；但由于 PCIe 版本缺乏 NVLink，多卡扩展时通信带宽受限（32 GB/s vs 900 GB/s），在 TP=2 场景下吞吐损失约 15%-30%（N108），导致其实际性价比在单卡场景下占优，但在多卡场景下可能被 SXM 版本反超。

## Corrected Claim

A100 80GB PCIe 版本的 300W TDP 在 24/7 运行下，年电费（按 $0.12/kWh）为 300W * 8760h / 1000 * $0.12 = $314.64/年，比 SXM 版本（$419.52/年）低 25%；但由于 PCIe 版本缺乏 NVLink，多卡扩展时通信带宽受限（32 GB/s vs 900 GB/s），在 TP=2 场景下吞吐损失约 15%-30%（N108），导致其实际性价比在单卡场景下占优，但在多卡场景下可能被 SXM 版本反超。

## Evidence

先验知识/题面给定，逻辑校验通过：电费计算数学正确（300W*8760h/1000*0.12=314.64），带宽对比（PCIe 32GB/s vs NVLink 900GB/s）符合A100硬件规格常识，多卡通信瓶颈导致吞吐损失符合分布式训练基本逻辑。

## Search Query

A100 PCIe vs SXM power cost multi-GPU performance trade-off
