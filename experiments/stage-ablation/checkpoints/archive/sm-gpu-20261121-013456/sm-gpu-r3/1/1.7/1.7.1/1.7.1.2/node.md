# N173: GQA 架构对推理吞吐量的带宽敏感性降低系数：由于 KV Cache 读取量减少 75%，GQA 使得推理吞吐量对显存带宽的依赖性降低，在带宽受限硬件（如 RT

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N67

## Claim

GQA 架构对推理吞吐量的带宽敏感性降低系数：由于 KV Cache 读取量减少 75%，GQA 使得推理吞吐量对显存带宽的依赖性降低，在带宽受限硬件（如 RTX 4090 1008GB/s）上，GQA 相比 MHA 可提升 ~1.5-2x 的 tokens/s 吞吐量，具体数值需实测验证。

## Corrected Claim

GQA 架构通过减少 KV Cache 读取量（具体比例取决于分组数 G，例如 G=4 时减少 75%），降低了推理对显存带宽的依赖。在带宽受限硬件上，GQA 相比 MHA 可显著提升 tokens/s 吞吐量，具体加速比（如 1.5-2x）取决于 G 值及硬件特性，需实测验证。

## Evidence

[质询]陈述中声称 GQA 相比 MHA 可提升 ~1.5-2x 吞吐量，但 GQA 的加速比高度依赖于具体的分组数（G）和硬件带宽/计算比。若 G 较大（如 G=8），KV Cache 减少量仅为 87.5% 而非 75%（75% 对应 G=4 或 MQA 的极端情况），且 1.5-2x 的加速比并非 GQA 的通用常数，而是特定配置下的经验值，直接将其作为 GQA 架构的固有属性陈述存在以偏概全和数值量级不确定的风险。 | 来源 [3] 明确提到 MQA 削减 75% 显存，GQA 是折中方案，但未直接给出 GQA 相比 MHA 的 1.5-2x 吞吐量提升这一具体数值；来源 [1] 和 [2] 讨论了带宽瓶颈但缺乏该具体加速比的直接支持。该数值属于经验事实，逻辑上自洽（带宽受限下减少访存确实能提升吞吐），但缺乏来源直接支持具体倍数，故降级。

## Search Query

GQA vs MHA inference throughput improvement bandwidth bound LLM Qwen3

## Retrieval Sources

- {'url': 'https://blog.csdn.net/weixin_31715171/article/details/166978623&rut=9e57fc8c37283439b5ddda80de168ccaf4910a9df84ca900fca3ac92a3030f80', 'type': 'ddg', 'title': '一文讲透MHA、MQA、GQA与KV Cache：大模型推理加速的核心-CSDN博客'}
- {'url': 'https://blog.csdn.net/weixin_29032489/article/details/170120277&rut=01dfe97646fd3097b0bd687883584da4039bcbd1530390feff08cfb83d596a75', 'type': 'ddg', 'title': 'MHA、MQA、GQA：注意力机制变体的KV Cache显存与推理速度全解析-CSDN博客'}
- {'url': 'https://www.kongchang.com/articles/mqayu-gqaxiang-jie-kv-cacheru-he-jiang-di-da-mo-xing-tui-li-xian-cun&rut=8aaa6af74dee71ef75dc0f28f6f6f8612c7290ee6e25ab1e281fa8a5b50995a2', 'type': 'ddg', 'title': 'MQA与GQA详解：KV Cache如何降低大模型推理显存 - 控场AI'}
