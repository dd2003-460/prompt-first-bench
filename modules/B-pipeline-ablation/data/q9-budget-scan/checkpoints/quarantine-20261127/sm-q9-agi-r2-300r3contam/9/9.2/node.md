# N84: V100-SXM2-16GB 的 HBM2 有效带宽利用率在 TP=4 下的实测值：在 27B NVFP4 模型推理负载下，由于 PCIe/SXM 互联带宽限制

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N31

## Claim

V100-SXM2-16GB 的 HBM2 有效带宽利用率在 TP=4 下的实测值：在 27B NVFP4 模型推理负载下，由于 PCIe/SXM 互联带宽限制及反量化开销，实际有效内存带宽约为理论峰值 (900 GB/s) 的 45-55%，即 405-495 GB/s，远低于 A100 的 ~70% 利用率。

## Corrected Claim

V100-SXM2-16GB 的理论 HBM2 带宽为 900 GB/s。在 27B NVFP4 模型推理负载下，受互联带宽及反量化开销影响，其实际有效内存带宽利用率通常低于理论峰值，但具体数值（如45-55%）需依赖特定基准测试数据，当前来源未提供确切实测值。

## Evidence

[质询]该陈述包含具体的经验性性能数据（45-55%利用率、405-495 GB/s带宽、A100对比数据），这些并非V100的固定硬件规格，而是高度依赖于特定软件栈、模型架构和推理框架的动态测量值，无法从第一性原理推导，且参考来源未提供此类负载下的实测数据。 | 参考来源[1]仅提供了V100的基础硬件规格（如发布时间、制程、架构），未涉及HBM2在特定TP=4推理负载下的有效带宽利用率或NVFP4反量化开销等动态性能指标，属于经验事实且缺乏直接来源支持。

## Search Query

V100 SXM2 HBM2 effective bandwidth utilization tensor parallel inference 27B model

## Retrieval Sources

- {'url': 'https://www.techpowerup.com/gpu-specs/tesla-v100-sxm2-16-gb.c3018&rut=a47f18b50a50a5e62aee9efe0e38c9243d1182563870374f50e477082b8c012f', 'type': 'ddg', 'title': 'NVIDIA Tesla V100 SXM2 16 GB Specs - TechPowerUp'}
