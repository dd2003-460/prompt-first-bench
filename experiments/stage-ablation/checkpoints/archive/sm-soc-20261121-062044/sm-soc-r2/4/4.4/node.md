# N22: 归因结论『平台驱动均衡』的置信度评估：若平台算法推荐权重 W_recommend 中，『高挂价』特征系数 β_high > 0.1 且显著（p < 0.05），

- **status**: verified
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N4

## Claim

归因结论『平台驱动均衡』的置信度评估：若平台算法推荐权重 W_recommend 中，『高挂价』特征系数 β_high > 0.1 且显著（p < 0.05），则归因于平台的置信度为 0.9；若 β_high < 0.05，则归因于卖家的置信度升至 0.8。

## Corrected Claim

在平台归因分析中，若高挂价特征系数显著为正（β_high > 0.1, p < 0.05），通常支持平台算法驱动假设；若系数较小或不显著（β_high < 0.05），则更倾向于归因于卖家策略。具体置信度需结合模型整体解释力（R²）及其他控制变量综合评估，而非仅依赖单一阈值。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点逻辑清晰且正交：节点1负责参数提取（数据层），节点3负责因果识别/稳健性检验（方法论层），节点2负责基于参数和显著性的最终置信度映射（决策层）。三者分别对应统计推断的不同阶段，无重复或矛盾。父节点中的阈值判断逻辑在节点2中得到了完整覆盖，且节点3补充了父节点隐含的因果有效性前提，提升了完备性。）

## Search Query

marketplace algorithm recommendation bias high asking price seller behavior
