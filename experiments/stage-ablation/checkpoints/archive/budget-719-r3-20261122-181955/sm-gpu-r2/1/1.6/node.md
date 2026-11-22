# N12: CPU推理方案：AMD EPYC 9004系列 / Intel Xeon Scalable 4th Gen，配合AVX-512/AMX指令集；需确认CPU推理Q

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N1

## Claim

CPU推理方案：AMD EPYC 9004系列 / Intel Xeon Scalable 4th Gen，配合AVX-512/AMX指令集；需确认CPU推理Qwen3-27B (INT4/INT8) 的吞吐量（tokens/s）及内存带宽需求。

## Corrected Claim

CPU推理方案：AMD EPYC 9004系列 / Intel Xeon Scalable 4th Gen，配合AVX-512/AMX指令集；需通过基准测试确认CPU推理Qwen3-27B (INT4/INT8) 的实际吞吐量（tokens/s）及内存带宽需求。

## Evidence

[质询]陈述中关于Qwen3-27B在指定CPU架构下的具体吞吐量（tokens/s）及内存带宽需求属于经验性性能数据，无法从第一性原理推导，且参考来源仅提及AMD EPYC 9004支持AI推理，未提供针对该特定模型和量化格式的具体性能指标或带宽需求数据。 | 来源[1]确认AMD EPYC 9004系列支持CPU AI推理，间接支持了硬件选型部分的合理性，但缺乏对具体模型性能指标的直接支持，且未覆盖Intel Xeon部分，属于间接支持。

## Search Query

CPU inference Qwen3-27B tokens/s AVX-512 AMX performance benchmark

## Retrieval Sources

- {'url': 'https://www.amd.com/zh-cn/products/processors/server/epyc/ai/9004-inference.html&rut=d929d583df17aafd1e3b988287335e4faa4603f9fffce346aeaa7248e19b0ffe', 'type': 'ddg', 'title': 'Amd Epyc（霄龙）9004 处理器助力加速 Ai 推理'}
