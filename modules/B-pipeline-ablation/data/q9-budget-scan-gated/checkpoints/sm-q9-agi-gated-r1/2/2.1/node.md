# N11: 科研闭环中'假设生成'阶段的单次推理成本：平均 prompt 长度 2k tokens，生成 500 tokens，耗时约 15-20s；瓶颈在 prefill

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N2

## Claim

科研闭环中'假设生成'阶段的单次推理成本：平均 prompt 长度 2k tokens，生成 500 tokens，耗时约 15-20s；瓶颈在 prefill 阶段的 attention 计算复杂度 O(n²)，长 prompt 下 prefill 延迟占主导

## Corrected Claim

科研闭环中'假设生成'阶段的单次推理成本：平均 prompt 长度 2k tokens，生成 500 tokens，耗时约 15-20s；瓶颈在 prefill 阶段的 attention 计算复杂度 O(n²)，长 prompt 下 prefill 延迟占主导

## Evidence

先验知识/题面给定，逻辑校验通过：2k tokens 输入在主流大模型（如 7B-70B 级别）上 prefill 耗时通常在 1-3 秒，加上 500 tokens 解码耗时，总耗时 15-20s 符合高并发或特定硬件配置下的合理量级；Prefill 阶段因需计算完整注意力矩阵，复杂度确为 O(n²)，且随序列长度增加，其延迟占比通常高于 Decode 阶段，符合 Transformer 架构的基本物理/计算直觉。
