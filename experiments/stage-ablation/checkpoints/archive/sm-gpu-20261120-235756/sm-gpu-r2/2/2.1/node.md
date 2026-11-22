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

父节点级核验未通过：不完备（子节点分别详细展开了 KV Cache 和激活值显存，两者内容正交且无冗余。但父节点公式中明确包含‘权重显存’作为显存下限的重要组成部分，子节点中完全缺失了对‘权重显存’的分解或说明，导致对父节点公式的覆盖不完整。）

## Search Query

LLM inference VRAM requirement KV cache activation memory
