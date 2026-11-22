# N36: 有效命中率折损的精确公式：H_effective = H_steady * (1 - p_invalid * f_refill * hit_prob_updat

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N11

## Claim

有效命中率折损的精确公式：H_effective = H_steady * (1 - p_invalid * f_refill * hit_prob_update)，其中 hit_prob_update ≈ 0.975，p_invalid = 0.01，f_refill ≈ 0.0021，折损 ≈ 0.01 * 0.0021 * 0.975 ≈ 0.0000205

## Corrected Claim

有效命中率折损的精确公式：H_effective = H_steady * (1 - p_invalid * f_refill * hit_prob_update)，其中 hit_prob_update ≈ 0.975，p_invalid = 0.01，f_refill ≈ 0.0021，折损 ≈ 0.01 * 0.0021 * 0.975 ≈ 0.0000205

## Evidence

父节点级核验未通过：非正交, 不完备（子节点与父节点存在严重逻辑矛盾：父节点定义了特定的公式和数值结果（折损≈0.002%），而子节点1和2明确否定该公式并给出完全不同的数值结果（折损≈0.95%）。这违反了分解的基本逻辑一致性（子节点应解释或细化父节点，而非推翻它）。此外，子节点3引入的‘请求去重’场景虽然在逻辑上可能成立，但它与子节点2的‘无去重基准’形成对比，但整体结构因核心公式的矛盾而失效。）

## Search Query

cache hit rate decay update invalidation refill failure probability formula
