# N135: FID分数变化ΔFID = FID_quantized - FID_BF16，用于评估生成文本的多样性和质量变化，需基于固定prompt集（如500条）计算，阈

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N25

## Claim

FID分数变化ΔFID = FID_quantized - FID_BF16，用于评估生成文本的多样性和质量变化，需基于固定prompt集（如500条）计算，阈值设为ΔFID < 5为可接受

## Corrected Claim

FID分数变化ΔFID = FID_quantized - FID_BF16，用于评估生成文本分布与参考分布的差异，需基于固定prompt集（如500条）计算；可接受阈值需根据具体任务基线动态确定，通常参考ΔFID < 5作为初步筛选标准。

## Evidence

[质询]阈值设定缺乏普适性依据：FID分数对数据集规模、领域及模型架构高度敏感，固定阈值ΔFID < 5在不同场景下可能过于宽松或严格，且FID主要衡量分布距离，将其直接等同于'多样性和质量变化'的绝对标准存在口径混淆风险。 | 先验知识/题面给定，逻辑校验通过，但阈值具体数值属于经验性设定，缺乏通用标准支持，故降级为定性表述。
