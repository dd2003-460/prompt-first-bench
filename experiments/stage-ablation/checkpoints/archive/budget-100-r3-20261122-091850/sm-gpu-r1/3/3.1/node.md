# N16: 推理延迟（Time to First Token, TTFT）的主要决定因素是权重加载时间（取决于内存带宽）和首 token 计算时间（取决于算力），公式：TT

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N3

## Claim

推理延迟（Time to First Token, TTFT）的主要决定因素是权重加载时间（取决于内存带宽）和首 token 计算时间（取决于算力），公式：TTFT ≈ Weight_Size / Memory_Bandwidth + Compute_Time_First_Token。

## Corrected Claim

推理延迟（Time to First Token, TTFT）的主要决定因素是权重加载时间（取决于内存带宽）和首 token 计算时间（取决于算力），公式：TTFT ≈ Weight_Size / Memory_Bandwidth + Compute_Time_First_Token。

## Evidence

先验知识/题面给定，逻辑校验通过
