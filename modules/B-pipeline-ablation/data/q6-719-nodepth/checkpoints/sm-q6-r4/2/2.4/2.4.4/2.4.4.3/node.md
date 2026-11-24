# N239: 公有云 CDN 月度请求数成本 Cloud_Request_Cost = Tail_Monthly_Requests × Unit_Price_Request，

- **status**: pending
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N71

## Claim

公有云 CDN 月度请求数成本 Cloud_Request_Cost = Tail_Monthly_Requests × Unit_Price_Request，其中 Unit_Price_Request 为单次请求计费（阿里云 CDN 约 ¥0.04/万次请求，即 ¥0.000004/次），小对象高频率场景下此项占比显著，需与 N141 的 s_avg 分布耦合计算。

## Corrected Claim

公有云 CDN 成本计算需根据具体厂商计费模式（流量或请求数）确定。若按请求数计费，Cloud_Request_Cost = Tail_Monthly_Requests × Unit_Price_Request。阿里云 CDN 主要按流量计费，若涉及请求数计费需查阅最新官方文档确认具体单价，不宜直接断定为 ¥0.04/万次。

## Evidence

父节点级核验未通过：有冗余（子节点通过三个具体的流量工作点（低、中、高）覆盖了父节点的成本计算逻辑，且各区间互斥（正交），覆盖了主要场景（完备）。然而，这三个子节点本质上是同一个线性/分段函数公式在不同输入参数下的具体实例化，属于‘参数取值’而非‘独立维度’，因此存在结构性冗余。）

## Search Query

Alibaba Cloud CDN request count pricing per 10000 requests cost

## Retrieval Sources

- {'url': 'https://cloud.google.com/cdn/pricing?hl=zh-tw&rut=99f10762043f724e43a5449a00e92904a365d04f48db583c60eeb2bb9417a268', 'type': 'ddg', 'title': 'Cloud CDN 定價 | Google Cloud'}
- {'url': 'https://cloud.google.com/cdn/pricing?hl=zh-cn&rut=74fac12a2c12ad0f3ff9712259e6fb7f4eb556c23cf368ae2dd79e79f2660348', 'type': 'ddg', 'title': 'Cloud CDN 价格 | Google Cloud'}
- {'url': 'https://cloudinsight.cc/zh/blog/cdn-pricing&rut=654151bc9b88e9834d32418962ce2e5781eda8f0b377faa402e8a0c39a62ae38', 'type': 'ddg', 'title': 'CDN 費用完整指南：2026 各大廠商定價比較與省錢技巧 | CloudInsight'}
