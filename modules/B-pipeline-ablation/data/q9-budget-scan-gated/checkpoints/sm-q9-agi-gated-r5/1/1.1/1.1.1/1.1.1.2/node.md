# N34: 在1451 tokens硬上限下，若需处理262144 tokens的max_model_len请求，必须启用KV Cache Offloading至主机内存。

- **status**: pending
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N18

## Claim

在1451 tokens硬上限下，若需处理262144 tokens的max_model_len请求，必须启用KV Cache Offloading至主机内存。V100服务器典型DDR4内存带宽为50-70 GB/s，相比HBM2的900 GB/s低一个数量级，Offload后每token decode延迟将从~15ms飙升至~150ms以上，导致吞吐量下降10x。

## Corrected Claim

在1451 tokens硬上限下，若需处理262144 tokens的max_model_len请求，必须启用KV Cache Offloading至主机内存。V100服务器典型DDR4内存带宽为50-70 GB/s，相比HBM2的900 GB/s低一个数量级，Offload后每token decode延迟将从~15ms飙升至~150ms以上，导致吞吐量下降10x。

## Evidence

父节点级核验未通过：不完备, 有冗余（子节点存在严重冗余：两个节点本质上是同一物理机制（KV Cache Offloading）在不同存储介质配置下的参数实例，而非独立的正交概念。此外，父节点强调的核心结论是‘延迟飙升至~150ms以上’和‘吞吐量下降10x’，主要基于纯RAM（DDR4）场景。子节点B引入了SSD，其计算出的234ms虽然符合逻辑，但偏离了父节点设定的‘典型V100服务器DDR4’这一主要约束语境，导致覆盖重点偏移。更关键的是，父节点并未提及SSD或冷热分层策略，因此子节点B超出了父节点的语义边界，破坏了完备性的对齐。）

## Search Query

DDR4 memory bandwidth typical server GB/s
