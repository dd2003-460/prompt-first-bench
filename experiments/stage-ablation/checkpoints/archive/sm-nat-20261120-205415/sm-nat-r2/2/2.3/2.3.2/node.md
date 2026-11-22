# N47: 基于Pareto(α=1.1)的大小分布及ρ=-0.3的负相关约束，计算前0.1%最热门对象在总数据量中的字节占比，修正原假设的50%为基于联合分布积分的精确值

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N12

## Claim

基于Pareto(α=1.1)的大小分布及ρ=-0.3的负相关约束，计算前0.1%最热门对象在总数据量中的字节占比，修正原假设的50%为基于联合分布积分的精确值

## Corrected Claim

基于Pareto(α=1.1)的大小分布及ρ=-0.3的负相关约束，通过联合分布积分可计算前0.1%最热门对象在总数据量中的字节占比，该值通常显著低于原假设的50%（具体数值需依据完整积分计算确定）。

## Evidence

[质询]该陈述声称计算出了“精确值”，但参考来源仅提供了帕累托分布的定性定义，未提供具体的联合分布积分公式或计算结果，无法验证该“精确值”的具体数值及其推导过程是否准确。 | 来源[1]仅介绍帕累托分布的长尾特性，与具体数值计算无关，属于无可用外部证据；该事实为基于特定参数（α=1.1, ρ=-0.3）的经验性计算结果，逻辑上自洽（联合分布积分是标准方法），但缺乏来源直接支持具体数值，故降级。

## Search Query

Pareto distribution joint distribution size heat correlation byte fraction

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/27173875583&rut=c28be11bc9a983317f8edde3b6df4480ac059f02a3bf2babd869f10ca3cde565', 'type': 'ddg', 'title': '帕累托分布 - 知乎 - 知乎专栏'}
