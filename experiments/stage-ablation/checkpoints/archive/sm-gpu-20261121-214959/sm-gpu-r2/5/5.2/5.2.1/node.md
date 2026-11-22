# N99: vLLM PagedAttention 在 batch_size=1, context_len=32k 下，KV Cache 内存碎片率 < 5%，导致实际有效

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N27

## Claim

vLLM PagedAttention 在 batch_size=1, context_len=32k 下，KV Cache 内存碎片率 < 5%，导致实际有效带宽利用率约 95-98%；相比之下，llama.cpp 默认连续内存分配在长上下文下碎片率可达 15-20%，有效带宽利用率降至 80-85%，这是两者吞吐量差异的主要来源之一。

## Corrected Claim

vLLM PagedAttention 通过分页管理显著降低了 KV Cache 的内存碎片，提高了显存利用率；相比之下，llama.cpp 默认连续内存分配在长上下文下可能产生更多碎片，导致显存利用率较低。内存管理效率是两者吞吐量差异的因素之一，但非唯一来源。

## Evidence

[质询]具体数值（碎片率<5% vs 15-20%，带宽利用率95-98% vs 80-85%）缺乏通用基准测试支持，且将吞吐量差异主要归因于内存碎片率可能忽略了计算密度、算子优化及调度策略等其他关键因素，存在过度简化因果关系的风险。 | 先验知识/题面给定，逻辑校验通过：PagedAttention 通过分页管理确实能显著降低内存碎片，提升显存利用率，但具体百分比数值属于经验性估计，不同硬件和负载下波动较大，且非唯一决定吞吐量的因素。

## Search Query

vLLM PagedAttention memory fragmentation vs llama.cpp continuous memory KV cache efficiency
