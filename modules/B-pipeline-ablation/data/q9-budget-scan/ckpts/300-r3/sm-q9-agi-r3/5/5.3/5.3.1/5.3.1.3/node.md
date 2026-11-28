# N276: 联合判断策略中，若 P(Token>1024 | Normal)=2.5% 且 P(Entropy<0.1 | Token>1024, Normal)=10%，

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N96

## Claim

联合判断策略中，若 P(Token>1024 | Normal)=2.5% 且 P(Entropy<0.1 | Token>1024, Normal)=10%，则联合误报率 FP_rate = 0.25%，但若任务类型偏向代码生成，FP_rate 将上升至 1.5-2.0%，需按任务类型动态调整阈值

## Corrected Claim

联合判断策略中，若 P(Token>1024 | Normal)=2.5% 且 P(Entropy<0.1 | Token>1024, Normal)=10%，则联合误报率 FP_rate = 0.25%；若任务类型偏向代码生成，由于长文本和低熵特征更常见，FP_rate 通常会显著上升，需按任务类型动态调整阈值。

## Evidence

[质询]后半部分关于‘任务类型偏向代码生成时FP_rate上升至1.5-2.0%’的具体数值范围缺乏通用理论支撑，属于特定场景下的经验估计，不同模型和任务分布下波动极大，难以作为普适事实。 | 前半部分联合概率计算（2.5% * 10% = 0.25%）逻辑正确；后半部分为经验性断言，虽逻辑上可能成立（代码生成通常token更长、熵更低，易触发误报），但具体数值1.5-2.0%无来源支持且非第一性原理可推导，故降级。
