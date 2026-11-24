# N102: 中国省级/市级用户流量分布的一手数据基准：基于 QuestMobile 或 CNNIC 最新报告，一二线城市（核心区域）用户占比约为 55%-65%，三四线及以

- **status**: pending
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N31

## Claim

中国省级/市级用户流量分布的一手数据基准：基于 QuestMobile 或 CNNIC 最新报告，一二线城市（核心区域）用户占比约为 55%-65%，三四线及以下（长尾区域）占比约为 35%-45%；具体到 10 个自建 POP 点覆盖的省份（如广东、江苏、浙江、北京、上海等），其流量加权占比 w_core 的基准值为 0.60，剩余 w_tail 为 0.40。

## Corrected Claim

基于QuestMobile等权威报告，一二线城市用户占比通常高于三四线及以下城市，具体比例需查阅最新详细报告，一般认为核心区域占比在50%-70%区间。

## Evidence

父节点级核验未通过：非正交, 不完备, 有冗余（1. 主题偏离：父节点核心是‘用户流量分布的一手数据基准’（即 w_core/w_tail 的确定），但 8 个子节点中仅有第 7 个（P99_base 地理分解）直接涉及该主题，其余 7 个均为缓存命中率、带宽计算或延迟模型，属于下游推导而非父节点本身的分解。2. 正交性/冗余：子节点 5（带宽计算）与子节点 6（传输延迟）高度耦合，且子节点 5 中关于 RPS 和带宽的推导依赖于流量分布，但未明确引用父节点的 w_core/w_tail 参数，导致逻辑链条断裂；子节点 2、3、4 均围绕 CHR 计算，存在参数重叠（如 C_eff 在多个节点中重复引用）。）

## Search Query

QuestMobile China mobile user distribution by city tier 2024 2025

## Retrieval Sources

- {'url': 'https://www.questmobile.com.cn/&rut=6c98b9b757400c8c10ac446d66ceb54519846e13c15d2f310c2a0c8af969fe40', 'type': 'ddg', 'title': 'QuestMobile-中国专业的移动互联网商业智能服务平台-QuestMobile'}
- {'url': 'https://www.questmobile.com.cn/research/report/2049018976051183618/&rut=cbd43005fdf8755115322e3eab711a44470dd9e4249f98f84da6a782480cd304', 'type': 'ddg', 'title': 'QuestMobile2026中国移动互联网春季大报告：结构性大变局来临，用户跨行业、跨终端迁移，部分行业黏性飙涨，如何适应新常态？'}
