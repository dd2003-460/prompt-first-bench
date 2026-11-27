# N174: 二手 H100 PCIe 版本的市场价格与性能折损：H100 PCIe 版本 (80GB) 二手价格约为 $18000-$22000，其显存带宽 (2039 G

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

二手 H100 PCIe 版本的市场价格与性能折损：H100 PCIe 版本 (80GB) 二手价格约为 $18000-$22000，其显存带宽 (2039 GB/s HBM3) 低于 SXM 版本 (3352 GB/s)，导致解码吞吐量仅为 SXM 版的 ~60%。在 TCO 对比中，H100 PCIe 的性价比介于 A100 80GB 和 H100 SXM 之间，但需扣除 PCIe 版本通常缺乏 NVLink 互联（仅支持 PCIe P2P）带来的多卡通信劣势。

## Corrected Claim

二手 H100 PCIe 版本 (80GB) 市场价格较高（约为原价的75%以上），其显存带宽 (2039 GB/s HBM3) 低于 SXM 版本 (3352 GB/s)，导致解码吞吐量显著低于 SXM 版。在 TCO 对比中，H100 PCIe 的性价比介于 A100 80GB 和 H100 SXM 之间，且缺乏 NVLink 互联。

## Evidence

[质询]具体二手价格区间（$18000-$22000）及解码吞吐量折损比例（~60%）属于高度波动的市场经验数据与特定负载下的性能指标，参考来源仅提及保值率（原价3/4以上）但未提供具体美元价格或精确的吞吐量对比数值，无法直接验证具体数值。 | 来源[3]间接支持H100二手保值率高（原价3/4以上），来源[2]确认H100 PCIe存在，但均无具体价格区间和60%吞吐量数据；逻辑上PCIe带宽低于SXM导致性能折损符合物理直觉，但具体数值缺乏直接来源支持。

## Retrieval Sources

- {'url': 'https://www.zouic.com/articles/used-gpu-48h-inspection-checklist/&rut=ec3e877f271cc092cee065806d624db96ab6d50d27d883d1a50450540af07e5d', 'type': 'ddg', 'title': '二手 H100 验卡：把「能不能用」变成一张可复核的清单 - ZouIC'}
- {'url': 'https://anchorgpu.com/zh/used-gpus/nvidia-h100-pcie&rut=d660be8c70e15a7771d53bdcfb4af1f0536c0430fad64d02fffa01e46ecc784e', 'type': 'ddg', 'title': '二手 H100 PCIe：规格与销售信息 — AnchorGPU'}
- {'url': 'https://mirrorfrog.com/blog/used-h100-resale-value-phenomenon/&rut=093bb71472a161ba9723afc2d0d092898b81084a8800a0a8bdd0af58d6f5b2f0', 'type': 'ddg', 'title': '二手 H100 保值之谜：Ai 芯片为何成了"硬通货" | Ai 算力卡百科 | 252 款 Ai 芯片规格对比'}
