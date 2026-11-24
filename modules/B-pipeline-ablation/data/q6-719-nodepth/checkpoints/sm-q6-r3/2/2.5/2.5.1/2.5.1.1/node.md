# N274: 自建 POP 缓存命中率 H_self 的计算公式：H_self = 1 - (Miss_Rate_Static + Miss_Rate_Dynamic)，其中

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N81

## Claim

自建 POP 缓存命中率 H_self 的计算公式：H_self = 1 - (Miss_Rate_Static + Miss_Rate_Dynamic)，其中 Miss_Rate_Static 为静态资源（图片/视频文件）未命中率，典型值 0.05-0.10；Miss_Rate_Dynamic 为动态请求或长尾内容未命中率，典型值 0.10-0.20。

## Corrected Claim

自建 POP 缓存命中率 H_self 的计算公式：H_self = 1 - (Miss_Rate_Static + Miss_Rate_Dynamic)，其中 Miss_Rate_Static 为静态资源（图片/视频文件）未命中率，典型值 0.05-0.10；Miss_Rate_Dynamic 为动态请求或长尾内容未命中率，典型值 0.10-0.20。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

CDN cache hit rate formula static dynamic miss rate
