# N294: 卖家非主导地位的阈值验证：计算卖家在 15-25% 溢价区间内的平均降价幅度 ΔP_avg，若 ΔP_avg < 5%（即未跨越买家感知阈限 ε），则证明卖家行

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N99

## Claim

卖家非主导地位的阈值验证：计算卖家在 15-25% 溢价区间内的平均降价幅度 ΔP_avg，若 ΔP_avg < 5%（即未跨越买家感知阈限 ε），则证明卖家行为受限于心理账户而非主动策略优化；需检索实际平台数据验证 ΔP_avg 的中位数。

## Corrected Claim

卖家非主导地位的阈值验证：需检索实际平台数据以计算卖家在 15-25% 溢价区间内的平均降价幅度 ΔP_avg 的中位数，若 ΔP_avg < 5%，则可能证明卖家行为受限于心理账户而非主动策略优化。

## Evidence

[质询]参考来源仅涉及亚马逊平台定价规则变更，未提供关于卖家在15-25%溢价区间内平均降价幅度（ΔP_avg）的具体统计数据或中位数，无法验证该经验事实。 | 逻辑自洽，但来源[1][2]仅讨论亚马逊新规，未覆盖该特定统计指标，属于经验事实且缺直接来源支持。

## Search Query

average price reduction magnitude for unsold items on second-hand platforms

## Retrieval Sources

- {'url': 'https://blog.csdn.net/kuajingozai/article/details/161181781&rut=10b23c2f31f9d589336702413260cc1ea265edf0217addc061811c0e8d944770', 'type': 'ddg', 'title': '亚马逊价格新规今日生效：90天触发机制拉低常规价，虚高划线价时代终结，卖家如何用数据守住折扣底线？_2026 年 5 月'}
- {'url': 'https://www.partnershare.cn/information/you-mai-yun-erp/6173&rut=9f90735ac0d34a59880186f9c5de6e11f6711848ec5ab308a87df870ef5f8379', 'type': 'ddg', 'title': '亚马逊划线价新规深度解读!5月落地虚高折扣失效，卖家定价应对方案'}
