# N273: 公有云部分 P99 延迟 L_p99_cloud 的约束值：公有云 CDN 全球/全国节点密度高，平均首字节时间 TTFB 较低，L_p99_cloud ≈ 3

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N90

## Claim

公有云部分 P99 延迟 L_p99_cloud 的约束值：公有云 CDN 全球/全国节点密度高，平均首字节时间 TTFB 较低，L_p99_cloud ≈ 30-50ms；其优势在于长尾区域覆盖，但受限于公有云内部调度，P99 可能略高于自建核心区域的理想值，需取保守值 50ms 进行计算。

## Corrected Claim

公有云部分 P99 延迟 L_p99_cloud 的约束值：公有云 CDN 全球/全国节点密度高，平均首字节时间 TTFB 较低，L_p99_cloud ≈ 30-50ms；其优势在于长尾区域覆盖，但受限于公有云内部调度，P99 可能略高于自建核心区域的理想值，需取保守值 50ms 进行计算。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

Cloudflare vs Alibaba Cloud CDN P99 latency comparison China
