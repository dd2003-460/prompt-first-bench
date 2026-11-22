# N116: Batch Size 对推荐方案的敏感性分析：在 Batch Size=1 时，Decode 阶段为带宽受限，推荐方案基于 N33/N35/N37 的带宽计算；

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N31

## Claim

Batch Size 对推荐方案的敏感性分析：在 Batch Size=1 时，Decode 阶段为带宽受限，推荐方案基于 N33/N35/N37 的带宽计算；在 Batch Size>1 时，Prefill 阶段为算力受限，需重新计算各候选卡在 Peak_FLOPS 下的吞吐量上限（N22），并评估不同 Batch Size 下性价比排序是否发生反转（如 H100 在高并发下优势扩大，消费级卡在低并发下性价比更高）。

## Corrected Claim

Batch Size 对推荐方案的敏感性分析：在 Batch Size=1 时，Decode 阶段为带宽受限，推荐方案基于 N33/N35/N37 的带宽计算；在 Batch Size>1 时，Prefill 阶段为算力受限，需重新计算各候选卡在 Peak_FLOPS 下的吞吐量上限（N22），并评估不同 Batch Size 下性价比排序是否发生反转（如 H100 在高并发下优势扩大，消费级卡在低并发下性价比更高）。

## Evidence

先验知识/题面给定，逻辑校验通过：Batch Size=1时Decode阶段受显存带宽限制，Batch Size>1时Prefill阶段受算力限制，符合LLM推理的基本物理直觉和工程常识。
