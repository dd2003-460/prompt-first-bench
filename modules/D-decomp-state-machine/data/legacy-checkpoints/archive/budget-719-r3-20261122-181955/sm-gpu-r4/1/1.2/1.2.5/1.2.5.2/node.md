# N164: A6000 在 BF16 精度下，Decode 阶段（Batch=1, KV_Cache≈32.77GB, Weights≈54GB）的理论吞吐量上限为 768

- **status**: pending
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N49

## Claim

A6000 在 BF16 精度下，Decode 阶段（Batch=1, KV_Cache≈32.77GB, Weights≈54GB）的理论吞吐量上限为 768 / (32.77 + 54) ≈ 8.86 tokens/s；此数值略低于 L40S，但两者均在 10 tokens/s 量级，带宽是主要瓶颈。

## Corrected Claim

A6000 在 BF16 精度下，Decode 阶段（Batch=1, KV_Cache≈32.77GB, Weights≈54GB）的理论吞吐量上限为 768 / (32.77 + 54) ≈ 8.86 tokens/s；此数值略低于 L40S，但两者均在 10 tokens/s 量级，带宽是主要瓶颈。

## Evidence

父节点级核验未通过：不完备（子节点之间存在逻辑依赖（子节点2依赖子节点1的修正值），且子节点3基于子节点2的理论值推导，因此严格来说它们不是完全正交的独立事实，而是因果链条。更重要的是，父节点的核心结论“带宽是主要瓶颈”以及“与L40S的量级对比”在子节点中未得到显式覆盖或验证，导致完备性不足。）
