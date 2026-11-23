# N174: 公有云策略的 P99 延迟对回源概率的敏感度：∂P99_cloud/∂p_miss_cloud = t_origin_cloud，其中 t_origin_clo

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N54

## Claim

公有云策略的 P99 延迟对回源概率的敏感度：∂P99_cloud/∂p_miss_cloud = t_origin_cloud，其中 t_origin_cloud 为公有云POP点到源站的回源延迟，通常 50-150ms（取决于POP点与源站距离及跨域路由），每增加 1% 回源概率，P99 增加 0.5-1.5ms

## Corrected Claim

公有云策略的 P99 延迟对回源概率的敏感度：∂P99_cloud/∂p_miss_cloud = t_origin_cloud，其中 t_origin_cloud 为公有云POP点到源站的回源延迟，通常 50-150ms（取决于POP点与源站距离及跨域路由），每增加 1% 回源概率，P99 增加 0.5-1.5ms

## Evidence

先验知识/题面给定，逻辑校验通过：P99延迟对回源概率的导数在理想化线性模型下等于回源延迟，数值量级（50-150ms）符合公有云跨域回源常识，且1%概率对应0.5-1.5ms增量在数学上自洽（1% * 50-150ms = 0.5-1.5ms）。

## Search Query

CDN origin fetch latency P99 sensitivity cache miss
