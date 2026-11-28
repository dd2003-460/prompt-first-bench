# N71: 图表 Caption 与图像内容的对齐误差：F1=0.78 中，20% 的错误来自 Caption 位置偏移（Caption 被识别为正文段落），80% 来自图

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N19, N20, N21

## Claim

图表 Caption 与图像内容的对齐误差：F1=0.78 中，20% 的错误来自 Caption 位置偏移（Caption 被识别为正文段落），80% 来自图像主体识别错误；使用 Unstructured.io 时，若预处理阶段应用 OCR 置信度阈值 Filter_conf>0.9，可过滤掉 30% 的低质量 Caption 提取，使有效提取 F1 提升至 0.82，但会丢弃 5% 的真实但模糊的 Caption。

## Corrected Claim

图表 Caption 与图像内容的对齐误差中，部分错误源于 Caption 位置偏移，部分源于图像主体识别错误；使用 Unstructured.io 并应用较高的 OCR 置信度阈值（如 >0.9）可过滤低质量 Caption 提取，从而提升有效提取的 F1 分数，但会伴随一定比例的真实模糊 Caption 被丢弃。

## Evidence

[质询]该陈述包含具体的经验性数值（F1=0.78, 20%/80%错误分布, Filter_conf>0.9, 30%过滤率, F1提升至0.82, 5%丢弃率），这些并非第一性原理可推导的数学或物理常数，而是依赖于特定数据集、模型版本和预处理管道的经验统计结果。在无外部来源支持的情况下，无法验证这些具体数值的真实性，存在‘幻觉’或‘虚构基准’的风险。 | source=knowledge，逻辑自洽（OCR置信度过滤通常以牺牲召回率为代价换取精度提升，符合一般工程直觉），但缺乏外部来源直接支持具体数值，且属于经验事实，故降级。

## Search Query

PDF figure caption alignment error rate OCR confidence threshold filtering
