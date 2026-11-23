# N81: 公有云 CDN 的折扣率 discount_rate 取决于合约期限和承诺用量，对于 1 年期且承诺月流量 > 10TB 的企业客户，阿里云/Cloudflar

- **status**: pending
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N17

## Claim

公有云 CDN 的折扣率 discount_rate 取决于合约期限和承诺用量，对于 1 年期且承诺月流量 > 10TB 的企业客户，阿里云/Cloudflare 的折扣率通常为 15%-25%；对于 3 年期合约，折扣率可达 30%-40%，需通过销售报价单确认具体阶梯。

## Corrected Claim

公有云 CDN 的折扣率通常随合约期限延长和承诺用量增加而提高，对于长期（如3年期）且高承诺用量的企业客户，折扣幅度显著高于短期或按量付费模式，具体阶梯需通过销售报价单确认。

## Evidence

父节点级核验未通过：不完备, 有冗余（1. 完备性缺失：父节点明确指出阿里云/Cloudflare 的折扣率范围（1年期15%-25%，3年期30%-40%），但子节点仅选取了单一中值（20%和35%），未涵盖范围边界或阶梯变化的具体逻辑，导致信息丢失。2. 冗余性高：子节点1和子节点2本质上是同一参数（合约期限+承诺量）的两个不同取值，属于枚举而非正交的概念分解，可以合并为一个“定价矩阵”或“参数化模型”。3. 正交性存疑：子节点3（临界点/决策逻辑）与前两个子节点（具体报价）不在同一维度，前两者是“状态描述”，后者是“决策规则”，混合在一起导致结构不纯。）

## Search Query

Alibaba Cloud CDN pricing discount rate long-term contract enterprise

## Retrieval Sources

- {'url': 'https://aws.amazon.com/cn/cloudfront/pricing/&rut=09dbd0ab7fd23b12cc74fb440556149ae8cedc2c709046ee635d95be9f9cd699', 'type': 'ddg', 'title': 'Amazon CloudFront CDN — 计划和定价 — 免费试用'}
- {'url': 'https://docs.aws.amazon.com/zh_cn/AmazonCloudFront/latest/DeveloperGuide/flat-rate-pricing-plan.html&rut=f0897a7af1e54329e7a3bf178776aa7624cffee495a08763f3c095b21c868865', 'type': 'ddg', 'title': 'CloudFront 固定费率定价方案 - Amazon CloudFront'}
- {'url': 'https://developer.aliyun.com/article/1774690&rut=6951a050a0bb1ef3d56ed09c39dd081c7ba1cb3c837589ba53acb80ccb849a9c', 'type': 'ddg', 'title': '2026 年阿里云双十一活动，Cdn 内容分发怎么计费，年付包月按量费用汇总-阿里云开发者社区'}
