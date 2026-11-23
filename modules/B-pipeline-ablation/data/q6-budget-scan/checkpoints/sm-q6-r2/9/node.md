# N36: CDN 缓存命中率（Cache Hit Ratio, CHR）对 P99 延迟的非线性影响：当 CHR 从 80% 提升至 95% 时，回源请求减少 62.5%

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

CDN 缓存命中率（Cache Hit Ratio, CHR）对 P99 延迟的非线性影响：当 CHR 从 80% 提升至 95% 时，回源请求减少 62.5%，P99 延迟通常下降 20-40ms；低于 70% 时，回源抖动导致 P99 急剧恶化

## Corrected Claim

CDN 缓存命中率（CHR）的提升会减少回源请求，从而降低 P99 延迟；当 CHR 较低时，回源抖动可能导致 P99 延迟显著恶化。

## Evidence

[质询]具体数值（P99下降20-40ms）属于高度依赖具体网络环境、源站距离及业务场景的经验数据，缺乏普适性，且参考来源中未包含任何关于延迟具体数值或非线性影响幅度的数据支持。 | 来源[1][2][3]仅定义了缓存命中率（CHR）的概念和计算方式，未提供CHR与P99延迟之间的具体量化关系或非线性影响数据，属于经验事实且缺来源支持。

## Retrieval Sources

- {'url': 'https://www.cloudflare.com/zh-cn/learning/cdn/what-is-a-cache-hit-ratio/&rut=0c72a820b0f7ce42a20a37ab8edc35701c4b16d1087605d179ce450c7c87f325', 'type': 'ddg', 'title': '什么是缓存命中率？ | Cloudflare'}
- {'url': 'https://www.cloudflare.com/zh-tw/learning/cdn/what-is-a-cache-hit-ratio/&rut=50a82c4f9337d5352d138e9ec8904a728152340c6c508c660b4aeb99832c0a9d', 'type': 'ddg', 'title': '什麼是快取命中率？ | Cloudflare'}
- {'url': 'https://support.huaweicloud.com/intl/en-us/productdesc-cdn/cdn_01_0349.html&rut=25aace93d52fb473e82acad460d296f947cc97fa571870290a3e0e9ca9e9cee4', 'type': 'ddg', 'title': 'Cache Hit Ratio_Content Delivery Network-Huawei Cloud'}
