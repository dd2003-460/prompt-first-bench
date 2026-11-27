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

父节点级核验未通过：不完备, 有冗余（子节点A和B本质上是同一物理过程（KV Cache Offloading）在不同存储介质配置下的两个具体工作点（参数取值），而非正交的独立概念；此外，父节点强调'必须启用'及'延迟飙升至150ms以上'的定性结论，而子节点仅提供了两个极端算例（56ms和234ms），未覆盖中间状态或通用公式推导，导致对父节点中'10x吞吐量下降'这一核心量化指标的支撑不完整。）

## Search Query

DDR4 memory bandwidth typical server GB/s
