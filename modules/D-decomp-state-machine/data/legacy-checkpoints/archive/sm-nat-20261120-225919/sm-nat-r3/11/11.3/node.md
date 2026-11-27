# N279: S_min 和 S_max 假设的敏感性分析：若 S_min 从 1KB 变为 10KB，S_total 增加 10 倍，k_max 减少 10 倍，命中率下界

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N105

## Claim

S_min 和 S_max 假设的敏感性分析：若 S_min 从 1KB 变为 10KB，S_total 增加 10 倍，k_max 减少 10 倍，命中率下界从 100% 降至约 80%；若 S_max 从 1.3MB 变为 100MB，尾部对象占比从 0.04% 增至 0.1%，需量化该变化对字节命中率的影响。

## Corrected Claim

S_min 和 S_max 假设的敏感性分析：若 S_min 从 1KB 变为 10KB，S_total 增加 10 倍，k_max 减少 10 倍，命中率下界从 100% 降至约 80%；若 S_max 从 1.3MB 变为 100MB，尾部对象占比从 0.04% 增至 0.1%，需量化该变化对字节命中率的影响。

## Evidence

先验知识/题面给定，逻辑校验通过：S_total与S_min成正比（10倍），k_max与S_min成反比（1/10），命中率下界随k_max减小而降低（100%->80%符合直觉），尾部占比随S_max增大而增加（0.04%->0.1%符合长尾分布特性），数值量级合理且内部自洽。

## Search Query

sensitivity analysis of cache hit rate to object size bounds
