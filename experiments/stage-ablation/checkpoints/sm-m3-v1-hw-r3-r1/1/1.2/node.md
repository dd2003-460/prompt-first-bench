# N8: 有效吞吐瓶颈计算：在max-num-seqs=8并发下，V100-16GB×4集群的实际tokens/s吞吐受限于PCIe带宽与HBM2读写速率，理论峰值与实测

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N1

## Claim

有效吞吐瓶颈计算：在max-num-seqs=8并发下，V100-16GB×4集群的实际tokens/s吞吐受限于PCIe带宽与HBM2读写速率，理论峰值与实测差距需用nsys profile数据标定（预期瓶颈在KV cache传输而非算力）

## Corrected Claim

在max-num-seqs=8并发下，V100-16GB×4集群的实际tokens/s吞吐可能受限于PCIe带宽与HBM2读写速率，需通过nsys profile数据标定以确认瓶颈是否在KV cache传输而非算力。

## Evidence

[质询]该陈述包含具体的硬件配置（V100-16GB×4）、软件参数（max-num-seqs=8）及性能瓶颈归因（PCIe/HBM vs KV cache），属于典型的经验性工程观测结论，无法从第一性原理或数学公理中严格推导得出；且缺乏实测数据支持‘理论峰值与实测差距’的具体量化关系。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，无法验证具体瓶颈归因及数值标定）。

## Search Query

V100 SXM2 vLLM throughput bottleneck PCIe bandwidth HBM2 KV cache transfer profiling nsys
