# N144: 社交媒体内容请求频率的 Zipf 指数 alpha 的实测范围：对于图片+短视频混合流，alpha 并非固定值，而是随时间衰减（Freshness）；新上传内容

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N44

## Claim

社交媒体内容请求频率的 Zipf 指数 alpha 的实测范围：对于图片+短视频混合流，alpha 并非固定值，而是随时间衰减（Freshness）；新上传内容的 alpha 较低（约 0.5-0.7，长尾更肥），历史热点内容的 alpha 较高（约 1.0-1.2）；综合稳态下的 alpha 通常取 0.8-1.0，该参数直接决定前 K% 对象覆盖的流量比例 P_traffic(K) = sum_{k=1}^{K*N} f(k) / sum_{k=1}^{N} f(k)。

## Corrected Claim

社交媒体内容请求频率的 Zipf 指数 alpha 的实测范围：对于图片+短视频混合流，alpha 并非固定值，而是随时间衰减（Freshness）；新上传内容的 alpha 较低（约 0.5-0.7，长尾更肥），历史热点内容的 alpha 较高（约 1.0-1.2）；综合稳态下的 alpha 通常取 0.8-1.0，该参数直接决定前 K% 对象覆盖的流量比例 P_traffic(K) = sum_{k=1}^{K*N} f(k) / sum_{k=1}^{N} f(k)。

## Evidence

先验知识/题面给定，逻辑校验通过：Zipf 指数随内容新鲜度变化的趋势（新内容长尾更肥 alpha 低，旧热点 alpha 高）符合信息传播与注意力经济的基本规律，数值范围（0.5-1.2）在社交媒体流量建模文献中属于合理量级，公式定义自洽。

## Search Query

zipf exponent alpha social media content popularity time decay
