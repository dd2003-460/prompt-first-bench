# N235: 负载系数随工作负载类型变化：Prefill阶段（计算密集）负载系数为0.9-1.0，Decode阶段（内存密集）负载系数为0.7-0.85；对于32K上下文长文

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N74

## Claim

负载系数随工作负载类型变化：Prefill阶段（计算密集）负载系数为0.9-1.0，Decode阶段（内存密集）负载系数为0.7-0.85；对于32K上下文长文本生成，Prefill占比约10-20%，加权平均负载系数约为0.82-0.88，而非恒定0.85

## Corrected Claim

负载系数随工作负载类型变化：Prefill阶段（计算密集）负载系数为0.9-1.0，Decode阶段（内存密集）负载系数为0.7-0.85；对于32K上下文长文本生成，Prefill占比约10-20%，加权平均负载系数约为0.82-0.88，而非恒定0.85

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

GPU power consumption prefill vs decode phase LLM inference load coefficient difference
