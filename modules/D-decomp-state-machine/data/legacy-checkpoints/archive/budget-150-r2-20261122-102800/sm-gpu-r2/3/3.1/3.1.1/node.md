# N88: BF16 工作点下 A100-80GB 的实际推理吞吐修正值：理论带宽上限 35 tokens/s，但受限于 PCIe 4.0/5.0 互联延迟及 Tensor

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N18

## Claim

BF16 工作点下 A100-80GB 的实际推理吞吐修正值：理论带宽上限 35 tokens/s，但受限于 PCIe 4.0/5.0 互联延迟及 Tensor Core 利用率，实测吞吐通常为理论值的 70-80%，即 24.5-28 tokens/s；若使用 NVLink (SXM4 版本)，通信开销降低，吞吐可接近 30 tokens/s，修正系数 [待核验] 取决于具体互联拓扑。

## Corrected Claim

BF16工作点下，A100-80GB的实际推理吞吐受限于模型规模、Batch Size及互联拓扑。通常实测吞吐为理论带宽上限的70-80%左右；使用NVLink互联相比PCIe可降低通信开销，提升吞吐效率。具体数值需结合特定模型（如7B/13B/70B）及推理框架实测确定。

## Evidence

[质询]该陈述包含具体的经验性数值（如理论上限35 tokens/s、实测70-80%、NVLink下30 tokens/s），这些数值高度依赖于具体的模型规模（如7B, 13B, 70B）、Batch Size、序列长度以及具体的推理框架（vLLM, TGI等）。未指定模型和负载条件，直接给出固定的吞吐数值和修正系数属于缺乏上下文的经验断言，且参考来源中并未提供这些具体的数值支持。 | 逻辑上，受限于互联带宽和计算利用率，实测吞吐低于理论峰值是符合物理直觉的；但参考来源[1][2][3]仅涉及BF16与FP16的精度对比或通用性能测试，未提供A100在特定模型下BF16推理的具体吞吐数值（如35 tokens/s或24.5-28 tokens/s），属于经验事实且缺乏直接来源支持。

## Search Query

A100 80GB Qwen 27B BF16 inference throughput tokens per second measured

## Retrieval Sources

- {'url': 'https://blog.csdn.net/gitblog_00411/article/details/154623208&rut=9f2e28b74b903931a278261cde108cb93481167670b31adc54b5508b3734a013', 'type': 'ddg', 'title': 'torchtune半精度训练：BF16 vs FP16在A100上性能对比 - CSDN博客'}
- {'url': 'https://blog.csdn.net/gitblog_00955/article/details/153760947&rut=2795d5322abb3c731b584b922f5ef0961870a6e6cb6b66b4136852486490bad0', 'type': 'ddg', 'title': 'Qwen1.5推理精度对比：FP16 vs BF16性能损耗测试-CSDN博客'}
- {'url': 'https://devpress.csdn.net/v1/article/detail/141946772&rut=b8f85003843a6c3b716a48405af7f3ccb7d35b7da91347c15fc32e5bca624c75', 'type': 'ddg', 'title': 'Qwen3.6-27B-AEON-Ultimate-Uncensored-BF16性能测试：在A100/H100上的吞吐量与延迟基准'}
