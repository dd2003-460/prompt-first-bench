# N117: SWE-bench Verified 中'中等复杂度'子集的定义：取 patch 行数在 50-200 行之间且依赖库数量 ≤ 3 的题目子集，该子集共包含约 

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N33

## Claim

SWE-bench Verified 中'中等复杂度'子集的定义：取 patch 行数在 50-200 行之间且依赖库数量 ≤ 3 的题目子集，该子集共包含约 150 道题目，需在此子集上计算通过率以符合'中等复杂度'限定

## Corrected Claim

SWE-bench Verified 官方未明确定义基于 patch 行数 50-200 行且依赖库 ≤ 3 的“中等复杂度”子集及其具体题目数量（约 150 道），该描述缺乏官方依据。

## Evidence

[质询]SWE-bench Verified 官方并未定义名为“中等复杂度”且基于特定 patch 行数（50-200行）和依赖库数量（≤3）的子集，该定义疑似为虚构或混淆了其他基准测试的分类标准。 | 经验事实，逻辑自洽但缺来源支持；SWE-bench Verified 公开文档中无此特定子集定义，属于具体经验参数，无法从第一性原理推出。

## Search Query

SWE-bench Verified medium complexity subset definition patch lines dependencies
