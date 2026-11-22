# N209: 显存带宽数据的来源标注策略：NVIDIA 官方规格表 (Data Sheet) 提供的理论峰值带宽 (如 H100 3.35 TB/s, A100 2.039 

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

显存带宽数据的来源标注策略：NVIDIA 官方规格表 (Data Sheet) 提供的理论峰值带宽 (如 H100 3.35 TB/s, A100 2.039 TB/s) 视为 [高置信度/官方数据]；而实际推理中受 KV Cache 访问模式影响的‘有效带宽’需引用 MLPerf Inference v4.0 或第三方评测 (如 LLM-Bench) 的实测值，此类数据标记为 [中等置信度/实测数据]，波动范围 ±10%。

## Corrected Claim

显存带宽数据的来源标注策略：NVIDIA 官方规格表提供的理论峰值带宽视为高置信度官方数据；实际推理中受 KV Cache 访问模式影响的‘有效带宽’需引用 MLPerf Inference 或第三方评测的实测值，此类数据标记为中等置信度实测数据。

## Evidence

[质询]该陈述包含具体的经验性数值（H100 3.35 TB/s, A100 2.039 TB/s）和特定的置信度波动范围（±10%），这些属于经验事实而非第一性原理可推导内容。参考来源仅涉及带宽测试工具（nvbandwidth）和通用产品资料，未提供具体的H100/A100官方规格数值，也未提供MLPerf或LLM-Bench的具体实测数据及±10%波动范围的依据，因此缺乏直接来源支持。 | 逻辑自洽（区分理论峰值与有效带宽符合工程常识），但参考来源[1]-[3]仅介绍带宽测试工具，未覆盖具体芯片规格数值及实测波动范围，属于经验事实缺来源支持。

## Retrieval Sources

- {'url': 'https://www.nvidia.cn/products/workstations/product-literature/&rut=0b53d54383bd47696b04488a4c321c3f40437493d815be7579b05eda03706e71', 'type': 'ddg', 'title': '专业可视化产品资料 | Nvidia'}
- {'url': 'https://blog.csdn.net/gitblog_00907/article/details/157822519&rut=387ae26b4de989d203318bc2921032352cfced4553f79083fe541dd148825dc1', 'type': 'ddg', 'title': 'NVIDIA nvbandwidth完全指南：GPU带宽性能测试与优化实战-CSDN博客'}
- {'url': 'https://developer.nvidia.cn/blog/nvidia-nvbandwidth-your-essential-tool-for-measuring-gpu-interconnect-and-memory-performance/&rut=d9eecf184ae783ac7bbf3c871e326d0c9232cddb56a3f466bf7eb0a7221d80e7', 'type': 'ddg', 'title': 'NVIDIA NVbandwidth：测量 GPU 互连和显存性能的必备工具'}
