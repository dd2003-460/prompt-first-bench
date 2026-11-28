# N103: 定义召回率（Recall）的计算公式：Recall = (Correctly Retrieved Facts / Total Injected Facts) *

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N28

## Claim

定义召回率（Recall）的计算公式：Recall = (Correctly Retrieved Facts / Total Injected Facts) * 100%，其中 Correctly Retrieved 判定标准为模型输出中包含针的关键实体或数值，允许 ±5% 的数值误差

## Corrected Claim

定义召回率（Recall）的计算公式：Recall = (Correctly Retrieved Facts / Total Injected Facts) * 100%，其中 Correctly Retrieved 判定标准为模型输出中包含针的关键实体或数值，允许 ±5% 的数值误差

## Evidence

父节点级核验未通过：不完备（虽然只有一个子节点不存在正交性冲突，但该分解严重缺乏完备性。父节点定义了完整的召回率计算公式及其核心判定标准（包含实体/数值匹配与误差容忍），而唯一的子节点仅深入探讨了'误差容忍度'这一细节的边界情况，完全遗漏了'关键实体识别'、'事实总数统计'以及'整体计算流程'等关键组成部分。此外，子节点引入了新的参数分类（epsilon_type），这超出了原父节点定义的简单百分比范围，属于过度细化且未涵盖主体逻辑。）

## Search Query

needle in haystack recall metric definition
