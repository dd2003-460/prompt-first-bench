# N33: 消费级显卡显存带宽瓶颈量化：RTX 4090/5090 的显存带宽 (GB/s) 与 H100/A100 的具体比值，以及该带宽差异在 Decode 阶段（内存

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

消费级显卡显存带宽瓶颈量化：RTX 4090/5090 的显存带宽 (GB/s) 与 H100/A100 的具体比值，以及该带宽差异在 Decode 阶段（内存密集型）对 Token/s 吞吐量的线性影响系数，用于论证为何高显存但低带宽的消费卡在长上下文推理中可能不如中端数据中心卡。

## Corrected Claim

RTX 5090显存带宽约为1792 GB/s，RTX 4090约为1008 GB/s，两者带宽差异显著。在Decode阶段，显存带宽是主要瓶颈，带宽越高通常能带来更高的Token/s吞吐量，但具体线性影响系数需结合模型架构和Batch Size实测确定，不能简单由带宽比值直接推导。

## Evidence

[质询]陈述中关于“线性影响系数”的具体数值缺失，且仅凭带宽比值无法直接推导出吞吐量的精确线性系数（受计算密度、KV Cache大小、Batch Size等多重因素影响），属于经验事实且缺乏多源一致的具体量化数据支持。 | 来源[1]提供了RTX 5090/4090的带宽数据（1792 GB/s vs ~1008 GB/s），支持了带宽差异的存在，但未提供与H100/A100的具体比值，也未提供Decode阶段吞吐量的线性影响系数，属于间接支持且关键量化指标缺失。

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/2061513310672049483&rut=0a886210c03cb39ee2b54d628dc3b5e7dd400a08a1bed4f4eb3639d021a8af8c', 'type': 'ddg', 'title': 'RTX 5090 vs RTX 4090算力对比：训练、推理、渲染场景实测差异'}
