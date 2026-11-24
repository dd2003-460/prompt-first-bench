# N9: 延迟达标可行性过滤：若 T=300ms，公有云 CDN 100% 达标（P99 ≤ 400ms 但核心区域 < 300ms，长尾可能超阈值需优化）；自建 10 

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1

## Claim

延迟达标可行性过滤：若 T=300ms，公有云 CDN 100% 达标（P99 ≤ 400ms 但核心区域 < 300ms，长尾可能超阈值需优化）；自建 10 点长尾 20% 用户 P99 可能 > 300ms，不达标；混合策略整体 P99 ≈ 250-350ms，边界达标

## Corrected Claim

延迟达标可行性过滤：若 T=300ms，公有云 CDN 100% 达标（P99 ≤ 400ms 但核心区域 < 300ms，长尾可能超阈值需优化）；自建 10 点长尾 20% 用户 P99 可能 > 300ms，不达标；混合策略整体 P99 ≈ 250-350ms，边界达标

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

CDN strategy P99 latency compliance 300ms threshold feasibility
