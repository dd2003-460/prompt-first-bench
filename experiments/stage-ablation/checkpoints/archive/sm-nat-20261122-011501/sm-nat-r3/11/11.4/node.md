# N183: 容量覆盖率敏感度分析：若 s_min 从 1KB 增至 10KB，E[S] 增至 110KB，K_max 降至 1,500-2,000，P_access(K_m

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N75

## Claim

容量覆盖率敏感度分析：若 s_min 从 1KB 增至 10KB，E[S] 增至 110KB，K_max 降至 1,500-2,000，P_access(K_max) 降至 25%-30%，H_upper 降至 20%-25%，显示命中率对最小对象大小极其敏感。

## Corrected Claim

容量覆盖率敏感度分析：若 s_min 从 1KB 增至 10KB，E[S] 增至 110KB，K_max 降至 1,500-2,000，P_access(K_max) 降至 25%-30%，H_upper 降至 20%-25%，显示命中率对最小对象大小极其敏感。

## Evidence

先验知识/题面给定，逻辑校验通过：增大最小对象大小（s_min）会减少可容纳的对象数量（K_max），从而降低总容量（E[S]）和访问概率分布的熵（H_upper），符合缓存/存储系统的基本物理直觉和数学逻辑。
