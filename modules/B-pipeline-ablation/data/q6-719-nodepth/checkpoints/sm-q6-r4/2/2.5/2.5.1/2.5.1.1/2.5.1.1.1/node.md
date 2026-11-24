# N594: T_img_optimal（高性低成工作点）：设定 P99 图片延迟阈值为 50ms，基于 Google Web Vitals 中 LCP < 2.5s 的‘良

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N195, N196, N197

## Claim

T_img_optimal（高性低成工作点）：设定 P99 图片延迟阈值为 50ms，基于 Google Web Vitals 中 LCP < 2.5s 的‘良好’标准，考虑到 CDN 边缘缓存命中率高（H>90%），将 100ms 优秀阈值收紧至 50ms 以最大化用户感知性能，此点对应最高的基础设施冗余投入和最低的带宽成本敏感度。

## Corrected Claim

T_img_optimal（高性低成工作点）：设定 P99 图片延迟阈值为 50ms，基于 Google Web Vitals 中 LCP < 2.5s 的‘良好’标准，考虑到 CDN 边缘缓存命中率高（H>90%），将 100ms 优秀阈值收紧至 50ms 以最大化用户感知性能，此点对应最高的基础设施冗余投入和最低的带宽成本敏感度。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

Google Web Vitals LCP good threshold 2.5s CDN edge latency 50ms best practice
