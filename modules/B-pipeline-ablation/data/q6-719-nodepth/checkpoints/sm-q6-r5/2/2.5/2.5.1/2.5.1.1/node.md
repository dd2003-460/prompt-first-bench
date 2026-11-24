# N195: T_img 的量化依据：Google Web Vitals 标准中 LCP (Largest Contentful Paint) 良好阈值为 2.5s，但针对 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N62

## Claim

T_img 的量化依据：Google Web Vitals 标准中 LCP (Largest Contentful Paint) 良好阈值为 2.5s，但针对 CDN 边缘节点 P99 延迟，行业基准为图片加载 P99 ≤ 100ms 优秀，≤ 300ms 可接受；此值基于用户感知延迟阈值研究（如 Amazon 每 100ms 延迟导致 1% 销售损失）

## Corrected Claim

T_img 的量化依据：Google Web Vitals 标准中 LCP (Largest Contentful Paint) 良好阈值为 2.5s，但针对 CDN 边缘节点 P99 延迟，行业基准为图片加载 P99 ≤ 100ms 优秀，≤ 300ms 可接受；此值基于用户感知延迟阈值研究（如 Amazon 每 100ms 延迟导致 1% 销售损失）

## Evidence

先验知识/题面给定，逻辑校验通过：LCP 2.5s 为 Google Web Vitals 官方标准；CDN 边缘节点 P99 延迟 100ms-300ms 符合行业工程基准；Amazon 100ms 延迟对应 1% 销售损失为经典行业引用数据，数值量级与逻辑均自洽。
