# N359: 阿里云 CDN 计费模式选择阈值：当日均流量 F_daily > 1.5TB 时，带宽计费通常低于流量计费；当 F_daily < 0.5TB 时，流量计费更优

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N121, N122, N123

## Claim

阿里云 CDN 计费模式选择阈值：当日均流量 F_daily > 1.5TB 时，带宽计费通常低于流量计费；当 F_daily < 0.5TB 时，流量计费更优。本场景日均 2TB，处于带宽计费优势区，但需对比具体阶梯单价计算临界点 F_break_even。

## Corrected Claim

阿里云 CDN 计费模式选择阈值：当日均流量 F_daily > 1.5TB 时，带宽计费通常低于流量计费；当 F_daily < 0.5TB 时，流量计费更优。本场景日均 2TB，处于带宽计费优势区，但需对比具体阶梯单价计算临界点 F_break_even。

## Evidence

先验知识/题面给定，逻辑校验通过
