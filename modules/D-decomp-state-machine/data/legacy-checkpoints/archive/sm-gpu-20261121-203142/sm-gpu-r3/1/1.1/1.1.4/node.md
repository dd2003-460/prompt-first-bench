# N38: 推理框架激活值峰值显存占用：基于vLLM或TGI实测数据，27B模型在32K上下文下的激活值（Activations）峰值通常在1.5-3.0GB之间，取决于b

- **status**: verified
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N7

## Claim

推理框架激活值峰值显存占用：基于vLLM或TGI实测数据，27B模型在32K上下文下的激活值（Activations）峰值通常在1.5-3.0GB之间，取决于batch size=1时的序列并行策略

## Corrected Claim

基于vLLM或TGI实测数据，27B模型在32K上下文下的激活值（Activations）峰值通常较小（具体数值取决于精度和实现，一般在GB级别以下或低个位数GB），主要显存瓶颈通常来自KV Cache和模型权重。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点1聚焦于计算峰值（Activations）的具体数值推导及不同Attention实现的影响，子节点2聚焦于固定运行时开销（Fixed Overhead）。两者分别对应显存占用的两个不同组成部分（动态计算部分 vs 静态固定部分），逻辑上正交且互补，共同覆盖了父节点中提到的'激活值峰值'及'框架实测数据'的关键方面，无重复或矛盾。）

## Search Query

vLLM Qwen3-27B activation memory usage 32k context batch size 1

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/1947229675689603831&rut=f6d9a0013dfebf1ddaafb2f67f387926e181406e404e8198e12bfed67614377f', 'type': 'ddg', 'title': 'vLLM 在大模型推理中的显存分析-以 Qwen3-32B 为例 - 知乎'}
