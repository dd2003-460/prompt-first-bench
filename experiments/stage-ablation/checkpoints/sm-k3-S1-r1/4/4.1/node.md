# N25: 长上下文有效注意力窗口衰减率：Qwen3.8-27B 在 262k max_len 下，位于末尾 10% token 的注意力权重相比中间位置下降约 15-20

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N4, N5, N6

## Claim

长上下文有效注意力窗口衰减率：Qwen3.8-27B 在 262k max_len 下，位于末尾 10% token 的注意力权重相比中间位置下降约 15-20% [时效待核]，需通过滑动窗口或分段摘要策略将有效信息密度提升 2 倍。

## Corrected Claim

长上下文模型通常存在注意力窗口衰减现象，位于末尾的token注意力权重可能低于中间位置，具体衰减率取决于模型架构与训练数据分布，需通过滑动窗口或分段摘要等策略优化有效信息密度。

## Evidence

[质询]该陈述包含具体的模型版本（Qwen3.8-27B）及精确的性能指标（15-20%衰减率、2倍密度提升），属于典型的经验事实。由于缺乏任何外部来源支持，且这些具体数值无法从第一性原理推导得出，存在数据虚构或张冠李戴的风险。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源，无法验证具体数值与模型版本的对应关系）

## Search Query

Qwen 27B long context attention decay effective window 262k tokens
