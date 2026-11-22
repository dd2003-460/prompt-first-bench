# N175: PPL 上升 0.3 对应的生成质量退化机制是：W4 量化导致长尾 token 概率分布平滑化，使得低概率但正确的答案 token 竞争不过高频错误 token

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N56

## Claim

PPL 上升 0.3 对应的生成质量退化机制是：W4 量化导致长尾 token 概率分布平滑化，使得低概率但正确的答案 token 竞争不过高频错误 token，具体表现为困惑度上升而非准确率直接下降，需通过 Top-1 精度与 PPL 的关联曲线量化此效应。

## Corrected Claim

W4量化通常会导致模型输出概率分布的平滑化或锐化偏差，进而引起PPL上升；这种分布偏移可能影响低概率token的生成概率，但具体表现为PPL上升而非准确率直接下降的机制需结合具体任务通过Top-1精度与PPL的关联曲线进行实证量化。

## Evidence

[质询]该陈述将PPL上升归因于'长尾token概率分布平滑化'导致'低概率正确token竞争不过高频错误token'，这一因果机制在量化误差分析中缺乏普遍共识，且'高频错误token'这一表述在生成任务中定义模糊，可能混淆了困惑度（全局分布拟合）与准确率（特定任务表现）之间的复杂非线性关系。 | 先验知识/题面给定，逻辑校验通过，但具体退化机制的因果链条存在争议且缺乏直接来源支持，故降级为定性表述。

## Search Query

perplexity increase mechanism low-bit quantization token probability distribution
