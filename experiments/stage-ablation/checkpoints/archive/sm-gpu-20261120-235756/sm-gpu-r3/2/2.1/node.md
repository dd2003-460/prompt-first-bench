# N13: 满足32K上下文的显存下限 = 权重显存 + KV Cache显存 + 激活值峰值显存，其中KV Cache显存随上下文长度线性增长，是主要瓶颈。

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N2

## Claim

满足32K上下文的显存下限 = 权重显存 + KV Cache显存 + 激活值峰值显存，其中KV Cache显存随上下文长度线性增长，是主要瓶颈。

## Corrected Claim

满足32K上下文的显存下限 = 权重显存 + KV Cache显存 + 激活值峰值显存，其中KV Cache显存随上下文长度线性增长，是主要瓶颈。

## Evidence

父节点级核验未通过：不完备（子节点仅覆盖了KV Cache和激活值显存，遗漏了父节点公式中明确列出的'权重显存'部分，导致分解不完备。）

## Search Query

LLM inference VRAM requirement KV cache activation memory
