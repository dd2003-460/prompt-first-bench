# N139: 高优先级通道的最低承诺消费（CUD）门槛量化：Minimum_Commitment = Max(Monthly_Usage_Cost, CUD_Threshol

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N37, N38, N39

## Claim

高优先级通道的最低承诺消费（CUD）门槛量化：Minimum_Commitment = Max(Monthly_Usage_Cost, CUD_Threshold)。阿里云/Cloudflare企业级CUD门槛通常为月消费 10,000-50,000 元人民币。若实际月消费低于门槛，需按门槛支付固定费用，导致小流量场景下单位成本急剧上升。

## Corrected Claim

高优先级通道的最低承诺消费（CUD）门槛量化：Minimum_Commitment = Max(Monthly_Usage_Cost, CUD_Threshold)。若实际月消费低于门槛，需按门槛支付固定费用，导致小流量场景下单位成本急剧上升。具体门槛值因云厂商及合同条款而异，需查阅阿里云/Cloudflare最新企业级定价政策。

## Evidence

[质询]来源主题不匹配：参考来源均为 Google Cloud (GCP) 的 CUD 文档，而陈述针对的是阿里云/Cloudflare 的具体人民币门槛数值（10,000-50,000元），属于经验事实且缺乏对应来源支持。 | 逻辑自洽（CUD机制确实导致低流量下单位成本上升），但参考来源[1][2][3]仅覆盖GCP，与阿里云/Cloudflare的具体金额无关，无法提供外部证据支持该具体数值范围。

## Search Query

CDN committed use discount minimum commitment threshold monthly spend 10000 RMB

## Retrieval Sources

- {'url': 'https://docs.cloud.google.com/compute/docs/instances/committed-use-discounts-overview?hl=zh-cn&rut=8a2cca90031773c17680e82df66be688862000dc67cb97d966edb7cd84f17c1b', 'type': 'ddg', 'title': 'Compute Engine 承诺使用折扣 (CUD) | Google Cloud Documentation'}
- {'url': 'https://docs.cloud.google.com/docs/cuds?hl=zh-cn&rut=60298c024e018be799101e19feed7879d8312d4d73a622868661139d7e8fa9b5', 'type': 'ddg', 'title': '承诺使用折扣 | Get started | Google Cloud Documentation'}
- {'url': 'https://duoyun.io/zh/blog/gcp-committed-use-discounts-explained&rut=ed12bad74cf1634e02651406ab23e6f54013571401b0d85c8e09a732c2cb9982', 'type': 'ddg', 'title': 'GCP承诺使用折扣CUD详解 | Duoyun Cloud | 多云 Duoyun Cloud'}
