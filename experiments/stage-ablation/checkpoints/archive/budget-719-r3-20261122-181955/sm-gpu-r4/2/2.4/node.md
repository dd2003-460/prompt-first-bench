# N17: 总内存需求汇总与硬件匹配：Total Mem = Weights + KV Cache + Overhead；计算各精度下总内存需求，并映射到N7-N12中各G

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N2

## Claim

总内存需求汇总与硬件匹配：Total Mem = Weights + KV Cache + Overhead；计算各精度下总内存需求，并映射到N7-N12中各GPU的显存容量，判断可行性（是否OOM）。

## Corrected Claim

总内存需求汇总与硬件匹配：Total Mem = Weights + KV Cache + Overhead；计算各精度下总内存需求，并映射到N7-N12中各GPU的显存容量，判断可行性（是否OOM）。

## Evidence

先验知识/题面给定，逻辑校验通过：总内存需求由权重、KV Cache和开销组成是LLM推理的标准内存模型，逻辑自洽且量级合理。
