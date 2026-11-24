# N221: 公有云 CDN 流量单价验证：Unit_Price_Per_GB 需区分下行流量与回源流量。阿里云/Cloudflare 中国区边缘下行流量单价通常阶梯定价：0

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N66

## Claim

公有云 CDN 流量单价验证：Unit_Price_Per_GB 需区分下行流量与回源流量。阿里云/Cloudflare 中国区边缘下行流量单价通常阶梯定价：0-5TB 约 ¥0.24/GB，5-50TB 约 ¥0.20/GB，50TB+ 约 ¥0.15/GB。当前月流量 60TB，处于第二阶梯，加权平均单价 ≈ (5×0.24 + 55×0.20)/60 ≈ ¥0.207/GB。修正后 Traffic_Cost ≈ 61,440 × 0.207 ≈ ¥12,718/月，低于 N66 中 ¥15,360 的估算。

## Corrected Claim

公有云 CDN 流量单价需区分下行与回源。阿里云等厂商通常采用阶梯定价，具体单价随市场波动（如按量付费可能在 ¥0.15-0.25/GB 区间），需以官方最新价目表为准。若按 ¥0.207/GB 估算，月成本约 ¥12,718。

## Evidence

[质询]具体阶梯单价数值（0.24/0.20/0.15）属于经验事实，且参考来源[1]提到的流量包单价（约0.09元/GB）与陈述中的按量付费单价存在巨大差异，来源未直接支持该特定阶梯定价结构，存在口径混淆或数据过时风险。 | 逻辑推导自洽（加权平均计算正确），但具体单价为经验事实，参考来源[1]提供的是流量包价格而非按量阶梯价，无法直接支持具体数值，故降级。

## Search Query

Alibaba Cloud CDN China traffic price per GB tiered 2024

## Retrieval Sources

- {'url': 'https://github.com/lfjrjr/cdn-pricing-models&rut=9c962577aade9a2fad04bcfdbafea8cf95db8d20b1a5f61d848277c1e92c521e', 'type': 'ddg', 'title': 'GitHub - lfjrjr/cdn-pricing-models: 阿里云CDN价格表，CDN如何收费的：三种计费模式对比+流量包年费明细 ...'}
- {'url': 'https://zhuanlan.zhihu.com/p/2053451104332013653&rut=b139ab919bbe4e1dccd41c5e3e873aad50cf163a1e7db1808bef286e4d92c0f8', 'type': 'ddg', 'title': '不同带宽、流量规格下，云加速价格如何计算？ - 知乎'}
