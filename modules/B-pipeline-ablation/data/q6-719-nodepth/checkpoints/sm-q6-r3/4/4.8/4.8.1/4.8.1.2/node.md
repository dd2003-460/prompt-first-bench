# N420: 工作点 B（中缓存命中，典型）：H_pop=0.90, 核心区域 RTT_user_pop=20ms, T_proc=10ms, Miss 概率 10%。P99

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N130

## Claim

工作点 B（中缓存命中，典型）：H_pop=0.90, 核心区域 RTT_user_pop=20ms, T_proc=10ms, Miss 概率 10%。P99_core = 0.90 * (20+10) + 0.10 * (20+10+50+0.5) ≈ 27ms + 8.05ms = 35.05ms。

## Corrected Claim

工作点 B（中缓存命中，典型）：H_pop=0.90, 核心区域 RTT_user_pop=20ms, T_proc=10ms, Miss 概率 10%。P99_core = 0.90 * (20+10) + 0.10 * (20+10+50+0.5) ≈ 27ms + 8.05ms = 35.05ms。

## Evidence

先验知识/题面给定，逻辑校验通过：计算过程 0.9*30 + 0.1*80.5 = 27 + 8.05 = 35.05 准确无误，量纲与逻辑自洽。
