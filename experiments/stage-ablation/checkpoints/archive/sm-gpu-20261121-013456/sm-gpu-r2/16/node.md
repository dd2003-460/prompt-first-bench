# N127: 在 2×RTX 4090 (48GB) 方案中，双卡互联带宽 (PCIe 4.0 x16 双向 ~32 GB/s) 远低于单卡显存带宽 (1008 GB/s)，

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

在 2×RTX 4090 (48GB) 方案中，双卡互联带宽 (PCIe 4.0 x16 双向 ~32 GB/s) 远低于单卡显存带宽 (1008 GB/s)，导致 KV Cache 跨卡传输成为瓶颈；实测显示，当 Batch Size > 2 时，多卡并行推理的效率衰减率约为 15-25%，必须从理论吞吐量中扣除该损耗以计算真实 TCO 性价比。

## Corrected Claim

在 2×RTX 4090 (48GB) 方案中，双卡互联带宽 (PCIe 4.0 x16 双向 ~32 GB/s) 远低于单卡显存带宽 (1008 GB/s)，导致 KV Cache 跨卡传输成为瓶颈；多卡并行推理的效率会因通信开销而显著衰减，具体衰减率取决于负载特征，需通过实测评估以计算真实 TCO 性价比。

## Evidence

[质询]陈述中关于“Batch Size > 2 时效率衰减率约为 15-25%”的具体数值缺乏来源支持，且该数值高度依赖于模型架构、序列长度及具体并行策略（如是否使用张量并行或流水线并行），属于经验性实测数据，无法从第一性原理直接推导。 | 来源[3]直接支持了PCIe 4.0 x16带宽（~31.5 GB/s）远低于显存带宽（1008 GB/s）导致瓶颈的逻辑，但所有来源均未提供“15-25%效率衰减”的具体实测数据，该部分为无来源支持的经验事实。

## Retrieval Sources

- {'url': 'https://blog.csdn.net/weixin_31220401/article/details/164531290&rut=236857488d674f8f21481a0f7b8759e188b1e9b400492cd6c086d15c6ca9247f', 'type': 'ddg', 'title': 'RTX 4090多卡互联带宽解析：PCIe 5.0与NVLink实战对比-CSDN博客'}
- {'url': 'https://blog.csdn.net/weixin_29164843/article/details/165141223&rut=a53563dbd4547415c14890470be06763bb18c045d1f80750138c3b1a449141a2', 'type': 'ddg', 'title': 'RTX 4090多卡互联：PCIe 5.0与NVLink带宽之争实测解析-CSDN博客'}
- {'url': 'https://www.80aj.com/2026/04/27/pcie-bandwidth-bottleneck-4090/&rut=4f20569ad7abaf2fa5d0001d4f19e1749cc7de460ced720aace228aec1fc870c', 'type': 'ddg', 'title': '揭秘双卡4090本地大模型部署瓶颈：为何PCIe带宽是硬伤？'}
