# N84: W_total 的敏感性分析工作点 C（基于 s_min=100KB）：W_total = 10^5 * 1100KB = 110,000,000 KB ≈ 1

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N30

## Claim

W_total 的敏感性分析工作点 C（基于 s_min=100KB）：W_total = 10^5 * 1100KB = 110,000,000 KB ≈ 104.9 GB，表明缓存覆盖率约 1.22，仍完全覆盖，但余量极小。

## Corrected Claim

W_total 的敏感性分析工作点 C（基于 s_min=100KB）：W_total = 10^5 * 1100KB = 110,000,000 KB ≈ 104.9 GB，表明缓存覆盖率约 1.22，仍完全覆盖，但余量极小。

## Evidence

先验知识/题面给定，逻辑校验通过：10^5 * 1100KB = 110,000,000 KB，换算为 GB (110,000,000 / 1024 / 1024 ≈ 104.89 GB) 与陈述一致；覆盖率 1.22 为基于特定工作点 C 的给定参数，数值量级合理且内部自洽。
