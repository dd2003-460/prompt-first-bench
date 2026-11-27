# N361: 双RTX 4090在PCIe 5.0 x16下，AllReduce通信的有效单向带宽理论上限为64 GB/s，实测有效带宽约为40-50 GB/s（受协议开销和

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N154

## Claim

双RTX 4090在PCIe 5.0 x16下，AllReduce通信的有效单向带宽理论上限为64 GB/s，实测有效带宽约为40-50 GB/s（受协议开销和驱动影响），远低于H100 NVLink的900 GB/s

## Corrected Claim

双RTX 4090在PCIe 5.0 x16下，AllReduce通信的有效单向带宽理论上限约为63-64 GB/s，实测有效带宽通常低于理论值（受协议开销和驱动影响），远低于H100 NVLink的900 GB/s。

## Evidence

[质询]实测有效带宽40-50 GB/s属于经验数据，参考来源仅提供了理论上限（约63 GB/s）和定性描述，未提供具体的实测数值范围，无法直接证实该具体区间。 | 来源[1]直接支持理论上限（单向约63 GB/s，与64 GB/s量级一致），但实测带宽40-50 GB/s为经验事实，缺乏来源直接支持，仅逻辑自洽（协议开销导致低于理论值）。

## Search Query

RTX 4090 PCIe 5.0 x16 effective bandwidth AllReduce benchmark vs H100 NVLink

## Retrieval Sources

- {'url': 'https://blog.csdn.net/weixin_31220401/article/details/164531290&rut=236857488d674f8f21481a0f7b8759e188b1e9b400492cd6c086d15c6ca9247f', 'type': 'ddg', 'title': 'RTX 4090多卡互联带宽解析：PCIe 5.0与NVLink实战对比-CSDN博客'}
- {'url': 'https://blog.csdn.net/weixin_29164843/article/details/165141223&rut=a53563dbd4547415c14890470be06763bb18c045d1f80750138c3b1a449141a2', 'type': 'ddg', 'title': 'RTX 4090多卡互联：PCIe 5.0与NVLink带宽之争实测解析-CSDN博客'}
- {'url': 'https://harrychen.xyz/2026/03/22/enable-pcie-p2p-on-rtx-5090/&rut=45e220aae84ad1df46df3713e737c98bcc3b4f7c1fe54c7d7aaa59a154ffcd94', 'type': 'ddg', 'title': "在 RTX 5090 上启用 PCIe P2P 通信支持 - Harry Chen's Blog"}
