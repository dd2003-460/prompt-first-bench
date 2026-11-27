# N138: 分子项'接收降价推送通知的活跃买家数'的实际观测值需提取自平台日志，其理论上限受限于通知权限开启率（通常60%-80%）与APP活跃时长重叠率，若权限关闭率>4

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N40

## Claim

分子项'接收降价推送通知的活跃买家数'的实际观测值需提取自平台日志，其理论上限受限于通知权限开启率（通常60%-80%）与APP活跃时长重叠率，若权限关闭率>40%，则触达率R的理论上限被压缩至0.5以下。

## Corrected Claim

分子项'接收降价推送通知的活跃买家数'的实际观测值需提取自平台日志，其理论上限受限于通知权限开启率与APP活跃时长重叠率；具体触达率上限需结合特定平台的权限开启率统计数据计算，而非固定为0.5以下。

## Evidence

[质询]陈述中关于“通知权限开启率通常60%-80%”以及“权限关闭率>40%则触达率上限<0.5”的具体数值属于经验性统计假设，缺乏普适性，且不同平台（iOS/Android）及用户群体差异巨大，不能直接作为理论上限的硬性约束条件。 | 来源[1]仅说明如何从控制台提取“推送数量”和“用户打开次数”等日志数据，支持了“需提取自平台日志”的操作部分，但未提供关于权限开启率或触达率理论上限的具体数值支持，属于间接支持/部分覆盖。

## Search Query

second hand marketplace push notification opt-in rate average 2023

## Retrieval Sources

- {'url': 'https://www.engagelab.com/zh_CN/docs/app-push/user-guide/console/stat/active-analysis&rut=9c0ac0c7414df565b4b47436225d9bbe4de7111149bd169d63656ab1d51a2f8e', 'type': 'ddg', 'title': '活跃分析 | AppPush 控制台指南 统计 简体中文 - EngageLab Docs'}
