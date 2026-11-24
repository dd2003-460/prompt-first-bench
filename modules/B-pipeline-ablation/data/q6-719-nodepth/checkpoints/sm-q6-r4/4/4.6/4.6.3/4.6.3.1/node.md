# N387: 公有云CDN L1边缘节点缓存容量 C_L1 的典型估算值：单节点物理内存通常为 64-256GB，假设 80% 用于缓存，有效容量 C_L1_eff ≈ 51

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N120

## Claim

公有云CDN L1边缘节点缓存容量 C_L1 的典型估算值：单节点物理内存通常为 64-256GB，假设 80% 用于缓存，有效容量 C_L1_eff ≈ 51-204GB。

## Corrected Claim

公有云CDN L1边缘节点缓存容量 C_L1 的典型估算值：单节点物理内存通常为 64-256GB，假设 80% 用于缓存，有效容量 C_L1_eff ≈ 51-204GB。

## Evidence

先验知识/题面给定，逻辑校验通过：64-256GB * 80% = 51.2-204.8GB，数值量级与计算逻辑自洽，符合公有云CDN边缘节点常见硬件配置范围。

## Search Query

CDN edge node typical memory size cache capacity GB
