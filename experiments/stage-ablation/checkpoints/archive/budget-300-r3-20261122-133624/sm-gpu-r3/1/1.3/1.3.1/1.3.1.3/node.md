# N194: 数据中心卡（如 H100/H200）的 CUDA Context 及框架基础开销通常高于消费级卡，约为 1.5-2.0GB，主要因为 Hopper 架构的 Te

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N49

## Claim

数据中心卡（如 H100/H200）的 CUDA Context 及框架基础开销通常高于消费级卡，约为 1.5-2.0GB，主要因为 Hopper 架构的 Tensor Core 初始化及更复杂的内存管理单元，此差异在 TCO 计算中虽占比小但影响显存利用率上限。

## Corrected Claim

数据中心卡（如 H100/H200）的 CUDA Context 及框架基础开销通常高于消费级卡，约为 1.5-2.0GB，主要因为 Hopper 架构的 Tensor Core 初始化及更复杂的内存管理单元，此差异在 TCO 计算中虽占比小但影响显存利用率上限。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

H100 vLLM base memory overhead GB
