# N394: 单 POP 点 10Gbps 带宽接入的运营商选择与价格区间：中国电信/联通骨干网 10Gbps 静态 IP 包年费用在 35-45 万元区间，取中位数 40 

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N125

## Claim

单 POP 点 10Gbps 带宽接入的运营商选择与价格区间：中国电信/联通骨干网 10Gbps 静态 IP 包年费用在 35-45 万元区间，取中位数 40 万元/年；此配置确保峰值 37.5 RPS 下单点带宽利用率 < 40%（10Gbps ≈ 1.25 GB/s，37.5 RPS * 2.05MB ≈ 77 MB/s，利用率 ≈ 6%），存在显著带宽冗余以应对突发流量。

## Corrected Claim

单 POP 点 10Gbps 带宽接入的运营商选择与价格区间：中国电信/联通骨干网 10Gbps 静态 IP 包年费用通常在数十万元量级（具体需询价，参考区间 35-45 万元/年）；此配置确保峰值 37.5 RPS 下单点带宽利用率极低（约 6%），存在显著带宽冗余以应对突发流量。

## Evidence

[质询]具体价格区间（35-45万元/年）属于高度依赖地区、具体运营商政策及谈判折扣的经验性市场数据，参考来源仅涉及网络架构和通用产品介绍，未提供该特定规格（10Gbps静态IP包年）的确切报价，存在价格口径混淆或数据过时的风险。 | 带宽利用率计算逻辑自洽（37.5 RPS * 2.05MB ≈ 77MB/s，远小于1.25GB/s），但价格数据为经验事实，参考来源[1][2][3]仅描述架构与产品，未直接支持具体价格区间，故降级。

## Search Query

China Telecom 10Gbps dedicated line annual cost CNY 2024

## Retrieval Sources

- {'url': 'https://developer.aliyun.com/article/1657355&rut=340a5b750d2b140643170ef9f1aacde281ca43a142538b7a370b381bc73d148f', 'type': 'ddg', 'title': '三大运营商国际专线架构性能成本与选型-开发者社区-阿里云'}
- {'url': 'https://juejin.cn/post/7482208912467148838&rut=4109bff7f02c367c4798730251da8d40785c52e531210f6514948664a2b711a3', 'type': 'ddg', 'title': '三大运营商骨干网架构深度剖析：线路建设与用户体验详细分析了中国电信、中国联通、中国移动的互联网线路建设和运营，以及从稳定 - 掘金'}
- {'url': 'https://www.ctyun.cn/products/sd-wan&rut=afa304358914aa51ba6d05c9b35864ad4042aed8501a071b9e0cac1eaa902036', 'type': 'ddg', 'title': '天翼云sd-wan_价格详情_功能优势_解决方案 -天翼云'}
