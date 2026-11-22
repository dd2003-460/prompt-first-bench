# N85: 数据中心级方案 (1×H100/H200 SXM) 的散热硬件成本：SXM模组通常依赖服务器级液冷背板或强制风冷机箱，单节点散热基础设施增量成本约 $500-$

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N13

## Claim

数据中心级方案 (1×H100/H200 SXM) 的散热硬件成本：SXM模组通常依赖服务器级液冷背板或强制风冷机箱，单节点散热基础设施增量成本约 $500-$2,000 (含风扇模块/液冷接头)，远高于消费级风冷。

## Corrected Claim

数据中心级方案 (1×H100/H200 SXM) 的散热硬件成本：SXM模组通常依赖服务器级液冷背板或强制风冷机箱，单节点散热基础设施增量成本显著高于消费级风冷，具体金额视服务器型号及冷却方案而定（通常数百至数千美元）。

## Evidence

[质询]具体数值区间（$500-$2,000）缺乏直接来源支持，且该成本高度依赖于具体服务器型号（如DGX A100/H100 vs HGX基座）及液冷/风冷配置，不同厂商报价差异巨大，单一区间可能以偏概全。 | 来源[2]提及SXM模组涉及风冷/液冷功耗设计及整机架构，间接支持散热基础设施存在额外成本，但未提供具体金额；来源[1][3]仅涉及芯片规格，无散热成本数据。作为经验事实，逻辑自洽但缺直接来源支持。

## Search Query

H100 SXM cooling infrastructure cost liquid cooling vs air cooling data center

## Retrieval Sources

- {'url': 'https://inferencex.semianalysis.com/chips/h100&rut=4ae57c5cc3bdbd2a33288624e598152e576547d47cab5c116a3fa2215e7eadcc', 'type': 'ddg', 'title': 'NVIDIA H100 SXM Specs: ~$1.17/hr, 80 GB HBM3 | InferenceX'}
- {'url': 'https://blog.csdn.net/essencelite/article/details/166795031&rut=5e52775c2e1ef25cc8c7d6d0fc99181505c3be7766967ef3165ec379b3ed0e98', 'type': 'ddg', 'title': 'Nvidia Dgx/Hgx 服务器全景深度解析：从 H100 到 Gb300，专业算力选型必读'}
- {'url': 'https://inferencex.semianalysis.com/zh/chips/h100&rut=f6f89a20f67a8aabf94d85cb223b75a35e5f2d36db1b8a3ed4a5d3a6bf86b885', 'type': 'ddg', 'title': 'NVIDIA H100 SXM 规格、价格与功耗 | InferenceX'}
