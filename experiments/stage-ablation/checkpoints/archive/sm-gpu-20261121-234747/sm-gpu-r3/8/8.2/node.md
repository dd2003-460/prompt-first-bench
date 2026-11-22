# N148: 多卡推理框架（如vLLM, DeepSpeed-Inference）在2卡PCIe互联下的扩展效率（Speedup Ratio）具体数值，定义为：(2 * Si

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N28

## Claim

多卡推理框架（如vLLM, DeepSpeed-Inference）在2卡PCIe互联下的扩展效率（Speedup Ratio）具体数值，定义为：(2 * Single_GPU_Throughput) / Multi_GPU_Throughput，需区分Prefill和Decode阶段的效率差异，Decode阶段通常受限于All-Reduce通信

## Corrected Claim

多卡推理框架（如vLLM, DeepSpeed-Inference）在2卡PCIe互联下的扩展效率（Speedup Ratio）通常低于理想线性加速比，且Prefill和Decode阶段的效率存在差异，Decode阶段往往因通信开销（如All-Reduce）而受到更大限制。

## Evidence

[质询]该陈述包含具体的经验性结论（如'Decode阶段通常受限于All-Reduce通信'）和隐含的数值预期，属于硬件/系统性能经验事实，无法从第一性原理严格推导，且缺乏具体数值支撑。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）

## Search Query

vLLM DeepSpeed multi-GPU PCIe tensor parallelism speedup ratio efficiency 2x GPU
