# N325: 图片请求占比 w_img 的流量加权计算：w_img = (req_img * s_img) / (req_img * s_img + req_video * 

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N110

## Claim

图片请求占比 w_img 的流量加权计算：w_img = (req_img * s_img) / (req_img * s_img + req_video * s_video)，需基于 N163/N164 的日均请求量与对象大小推导，典型值在 0.5-0.7 之间（图片数量多但体积小，短视频数量少但体积大），直接决定 s_avg 的数值区间。

## Corrected Claim

图片请求占比 w_img 的流量加权计算公式为 w_img = (req_img * s_img) / (req_img * s_img + req_video * s_video)，其具体数值取决于业务场景中图片与短视频的请求量及平均大小分布，需基于实际监控数据推导。

## Evidence

[质询]典型值 0.5-0.7 属于经验事实，缺乏具体业务场景（如短视频平台 vs 图文社区）的明确界定，不同场景下该比例波动极大，直接断言典型区间存在口径混淆风险。 | 公式逻辑自洽（加权平均定义），但参考来源均与流量加权计算无关，且典型值属于经验事实，无来源直接支持，故降级。

## Search Query

image vs video request ratio traffic weighted average object size CDN

## Retrieval Sources

- {'url': 'https://blog.csdn.net/L824627453/article/details/120861164&rut=886154b0c0efce97d5ee3e99672735b4d3067d0b1c940b64ab8b710cd3d6eb4a', 'type': 'ddg', 'title': '微信图片延迟加载与自定义属性深入解析-csdn博客'}
- {'url': 'https://megarouter.com/zh/blog/megarouter-ai-api-traffic-scheduling&rut=4faa0678f36bc508c8ac33c2d5d4472f0d0b2598680eef6429deeaf3932c1149', 'type': 'ddg', 'title': 'MegaRouter AI API 流量调度：如何管理并发请求与推理资源'}
- {'url': 'https://ask.csdn.net/questions/9255177&rut=915026e165c42bbc5860b2bfcc45e2ccd0b3698a74678c08dd7761615e230776', 'type': 'ddg', 'title': '天地图瓦片URL中`tiles_img_w`参数的作用及常见拼接错误？_编程语言-CSDN问答'}
