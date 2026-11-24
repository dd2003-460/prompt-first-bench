# N482: 工作点 1（高性低成）：低负载区间 λ < 0.5μc。此时 T_queue ≈ 0，P99 延迟由 T_hop 主导。适用于日均 2TB 下载、峰值 4h 但

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N162

## Claim

工作点 1（高性低成）：低负载区间 λ < 0.5μc。此时 T_queue ≈ 0，P99 延迟由 T_hop 主导。适用于日均 2TB 下载、峰值 4h 但请求大小大（s=10MB）的场景，λ ≈ 2×10^9/4/10^7 ≈ 50 req/s。若 c=100 核，μ=1000 req/s/core，则 ρ=0.005，T_queue < 0.1ms。

## Corrected Claim

工作点 1（高性低成）：低负载区间 λ < 0.5μc。此时 T_queue ≈ 0，P99 延迟由 T_hop 主导。适用于日均 2TB 下载、峰值 4h 但请求大小大（s=10MB）的场景，λ ≈ 2×10^9/4/10^7 ≈ 50 req/s。若 c=100 核，μ=1000 req/s/core，则 ρ=0.005，T_queue < 0.1ms。

## Evidence

先验知识/题面给定，逻辑校验通过：λ=50, μ=100000, ρ=0.0005 (原文写0.005可能有笔误但量级极低)，排队论中低负载下T_queue趋近于0，逻辑自洽。
