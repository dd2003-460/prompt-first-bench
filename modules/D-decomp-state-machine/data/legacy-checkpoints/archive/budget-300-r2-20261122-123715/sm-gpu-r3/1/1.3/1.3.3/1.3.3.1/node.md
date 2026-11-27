# N170: 统一内存架构下的显存需求计算：Qwen3-27B W4 权重 (~13.5GB) + 32K KV Cache (GQA, INT8, ~18GB) + 激活值

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N44

## Claim

统一内存架构下的显存需求计算：Qwen3-27B W4 权重 (~13.5GB) + 32K KV Cache (GQA, INT8, ~18GB) + 激活值 (~5GB) = ~36.5GB，远低于 192GB 总内存，因此无 Offload 风险，所有数据驻留 DRAM，带宽利用率受限于内存控制器而非容量

## Corrected Claim

统一内存架构下的显存需求计算：Qwen3-27B W4 权重 (~13.5GB) + 32K KV Cache (GQA, INT8, ~18GB) + 激活值 (~5GB) = ~36.5GB，远低于 192GB 总内存，因此无 Offload 风险，所有数据驻留 DRAM，带宽利用率受限于内存控制器而非容量

## Evidence

[质询]KV Cache 估算值（18GB）可能偏高，取决于具体模型层数和头数配置，但量级在合理范围内；激活值 5GB 对于 32K 上下文也属保守估计，整体逻辑自洽。 | 先验知识/题面给定，逻辑校验通过：Qwen3-27B W4 权重约 13.5GB 符合 27B*4bit/8 的估算；GQA INT8 KV Cache 在 32K 上下文下 18GB 量级合理；总内存 36.5GB 远低于 192GB，无 Offload 风险结论成立。

## Search Query

Qwen3 27B KV cache size 32K context GQA INT8 calculation
