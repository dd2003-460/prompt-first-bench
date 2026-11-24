# N227: 公有云CDN与自建POP在相同2TB日流量下的年回源流量差异 ΔF_annual 计算：ΔF_annual = 365 * 2TB * (H_pub - H_s

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N67

## Claim

公有云CDN与自建POP在相同2TB日流量下的年回源流量差异 ΔF_annual 计算：ΔF_annual = 365 * 2TB * (H_pub - H_self)，其中 H_pub=95%, H_self=90%，结果 ΔF_annual ≈ 36.5TB/年

## Corrected Claim

公有云CDN与自建POP在相同2TB日流量下的年回源流量差异 ΔF_annual 计算：ΔF_annual = 365 * 2TB * (H_pub - H_self)，其中 H_pub=95%, H_self=90%，结果 ΔF_annual ≈ 36.5TB/年

## Evidence

先验知识/题面给定，逻辑校验通过：365 * 2TB * (0.95 - 0.90) = 365 * 2TB * 0.05 = 36.5TB，计算无误且量级合理。
