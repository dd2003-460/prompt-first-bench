# N82: 软件兼容性与稳定性风险量化：评估 vLLM/TensorRT-LLM 在 2x RTX 4090 (PCIe 互联) 上的实际吞吐效率 k_parallel_e

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N18

## Claim

软件兼容性与稳定性风险量化：评估 vLLM/TensorRT-LLM 在 2x RTX 4090 (PCIe 互联) 上的实际吞吐效率 k_parallel_efficiency，通常低于 NVLink 方案，需查找具体 benchmark 数据（如 tokens/sec 对比单卡线性扩展的理论值），以修正有效吞吐量 Throughput_eff = N * Throughput_single * k_parallel。

## Corrected Claim

vLLM/TensorRT-LLM 在 2x RTX 4090 (PCIe 互联) 上的实际吞吐效率 k_parallel_efficiency 通常低于 NVLink 方案，具体数值需查阅针对该硬件配置的实测 benchmark 数据以修正有效吞吐量。

## Evidence

[质询]该陈述包含具体的工程经验参数（k_parallel_efficiency 的具体量化或 benchmark 数据），属于经验事实，无法仅从第一性原理推导得出具体数值，且参考来源未提供 RTX 4090 PCIe 互联的具体吞吐效率数据。 | 逻辑上 PCIe 带宽低于 NVLink 导致多卡扩展效率降低是合理的物理/工程直觉，但参考来源 [1] 仅讨论数据中心硬件及框架选型，未覆盖消费级 GPU (RTX 4090) 的 PCIe 互联具体 benchmark 数据，属于经验事实缺来源支持。

## Search Query

vLLM 2x RTX 4090 PCIe tensor parallelism throughput efficiency benchmark

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/2024113488100869524&rut=8f2995f66b5a2764e99687f76a40f7b5a1af40f710600280dc3577913669222c', 'type': 'ddg', 'title': '大模型推理服务架构解析：vLLM、TensorRT-LLM与llama.cpp选型与实现'}
