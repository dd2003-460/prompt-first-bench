# N16: 262k上下文内的信息衰减曲线：随着上下文长度增加，模型对早期信息的注意力权重下降（Lost in the Middle现象）；量化表现为：位置在0-20%和8

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N3

## Claim

262k上下文内的信息衰减曲线：随着上下文长度增加，模型对早期信息的注意力权重下降（Lost in the Middle现象）；量化表现为：位置在0-20%和80-100%的信息提取准确率差异；在256k上下文中，中间部分（40-60%位置）的关键假设被忽略的概率P_ignore约为15-25%，需通过分段摘要或关键信息重注策略补偿。

## Corrected Claim

262k上下文内存在信息衰减现象（Lost in the Middle），模型对中间位置信息的注意力权重通常低于首尾位置；具体忽略概率随模型架构和任务类型显著变化，建议通过分段摘要或关键信息重注策略进行补偿。

## Evidence

[质询]具体数值（15-25%忽略概率）缺乏通用基准支持，不同模型架构（如RoPE vs ALiBi）及具体实现下该指标波动极大，属于特定实验条件下的经验数据而非普适规律。 | 经验事实，逻辑自洽但缺来源支持（检索失败，无外部证据佐证具体数值区间）

## Search Query

lost in the middle long context attention decay LLM 100k 200k information retention accuracy
