# N288: 佣金率 r 的取值范围及具体值：r 在 5%-10% 之间，具体取决于平台政策。[待核验]：需确认当前平台实际佣金率，例如若 r=7.5%，则代入公式计算。

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: stochastic
- **rework_count**: 1
- **parent_ids**: N78

## Claim

佣金率 r 的取值范围及具体值：r 在 5%-10% 之间，具体取决于平台政策。[待核验]：需确认当前平台实际佣金率，例如若 r=7.5%，则代入公式计算。

## Corrected Claim

佣金率 r 因平台、类目及售价区间而异，例如亚马逊美国站部分类目费率在 5% 至 17% 甚至更高之间，具体需参照平台最新费率表。

## Evidence

[质询]陈述声称佣金率 r 在 5%-10% 之间，但参考来源 [2] 显示亚马逊美国站部分类目（如售价超过 $20 的情况）佣金率可达 17%，且不同类目费率差异巨大，5%-10% 并非通用或准确的范围，存在以偏概全或数据过时/错误的可能。 | 来源 [2] 指出亚马逊佣金率存在 17% 的情况，直接反驳了 '5%-10%' 的上限；来源 [1] 为合规指南，未提供具体数值。因经验事实（具体费率）与来源存在矛盾/不匹配，且无法从第一性原理推出具体数值，故降级。

## Search Query

current commission rate for second-hand trading platform

## Retrieval Sources

- {'url': 'https://www.gov.cn/zhengce/zhengceku/202508/content_7034993.htm&rut=92c1453a344450501aaf2f62a6bfc89619e670a88e343b560062b25e969809a3', 'type': 'ddg', 'title': '市场监管总局关于发布《网络交易平台收费行为合规指南》的公告_国务院部门文件_中国政府网'}
- {'url': 'https://vendscope.cn/guide/amazon-referral-fee-rates&rut=ae0faf3735ca351fde440f8239f1364b96f3afe94624b39d0fed6843fd01e45a', 'type': 'ddg', 'title': '2026 亚马逊各类目佣金费率表（美国站，含分段规则与最低佣金） | 选品镜 Vendscope'}
