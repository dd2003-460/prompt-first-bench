# N140: 2×RTX 4090 的 PCIe 拓扑配置中，若两卡均挂载在同一 CPU 的 PCIe 根复合体下，跨卡通信无需经过 CPU 内存中转，延迟可控制在 10 微

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N36

## Claim

2×RTX 4090 的 PCIe 拓扑配置中，若两卡均挂载在同一 CPU 的 PCIe 根复合体下，跨卡通信无需经过 CPU 内存中转，延迟可控制在 10 微秒以内；若挂载在不同 CPU 下，则需经过 UPI/QPI 互联，延迟增加 2-3 倍。

## Corrected Claim

2×RTX 4090 的 PCIe 拓扑配置中，若两卡均挂载在同一 CPU 的 PCIe 根复合体下，跨卡通信通常无需经过 CPU 内存中转（支持 P2P），延迟显著低于挂载在不同 CPU 下需经过 UPI/QPI 互联的情况。

## Evidence

[质询]具体延迟数值（10微秒、2-3倍）属于经验事实，缺乏通用基准测试支持，且受具体主板拓扑、PCIe版本及驱动影响极大，单一来源未提供数据支持。 | 逻辑自洽（同CPU下P2P通信确实优于跨CPU UPI/QPI通信），但参考来源[1]仅涉及搭建指南概述，未提供具体延迟数值或拓扑对比数据，属于经验事实缺来源支持。

## Search Query

dual GPU PCIe topology CPU UPI latency interconnect overhead

## Retrieval Sources

- {'url': 'https://wenku.baidu.com/view/d3606a4c826fb84ae45c3b3567ec102de2bddf20.html&rut=b3b14044d8920256459fb098dd6287c7dec9dbd75f9bf2895ba48d710e22ae64', 'type': 'ddg', 'title': '双rtx 4090显卡终极搭建指南：从硬件兼容、安装到应用优化全解析'}
