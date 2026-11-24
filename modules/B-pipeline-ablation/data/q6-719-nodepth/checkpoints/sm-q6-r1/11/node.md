# N49: 敏感性分析：P99 目标 T 从 200ms 降低至 100ms 时，公有云 CDN 在长尾区域（距离 >500km）的合规率下降至 <60%，而自建 POP 

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

敏感性分析：P99 目标 T 从 200ms 降低至 100ms 时，公有云 CDN 在长尾区域（距离 >500km）的合规率下降至 <60%，而自建 POP 若仅覆盖核心区域，合规率取决于核心区域流量占比 P_core 是否 >40%。

## Corrected Claim

敏感性分析：P99 目标 T 从 200ms 降低至 100ms 时，公有云 CDN 在长尾区域（距离 >500km）的合规率下降至 <60%，而自建 POP 若仅覆盖核心区域，合规率取决于核心区域流量占比 P_core 是否 >40%。

## Evidence

检索失败: no sources from any channel (all 5 failed)
