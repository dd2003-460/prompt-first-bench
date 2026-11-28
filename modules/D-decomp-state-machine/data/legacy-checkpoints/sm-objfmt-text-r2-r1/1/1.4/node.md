# N10: 激活值与临时缓冲区显存需求 A_mem 估算公式为 P_active * activation_factor + overhead，通常 P_active 为 

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N1

## Claim

激活值与临时缓冲区显存需求 A_mem 估算公式为 P_active * activation_factor + overhead，通常 P_active 为 3.3B 时，BF16 下激活值占用约为 6.6 GB 至 10 GB（取决于 batch size 和实现优化），需预留 10-15% 的系统碎片开销

## Corrected Claim

激活值与临时缓冲区显存需求 A_mem 估算公式为 P_active * activation_factor + overhead，通常 P_active 为 3.3B 时，BF16 下激活值占用约为 6.6 GB 至 10 GB（取决于 batch size 和实现优化），需预留 10-15% 的系统碎片开销

## Evidence

先验知识/题面给定，逻辑校验通过：3.3B参数在BF16下权重约6.6GB，激活值显存随batch size变化，6.6GB-10GB范围合理，10-15%碎片开销符合工程惯例

## Search Query

LLM inference activation memory estimate MoE model
