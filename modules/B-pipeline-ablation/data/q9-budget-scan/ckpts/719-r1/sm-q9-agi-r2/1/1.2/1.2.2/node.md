# N35: Qwen3-27B 在 LongBench 或 Needle-in-a-Haystack 测试中，当关键信息位于上下文开头（位置偏差）时，相较于位于中间位置时的

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N8

## Claim

Qwen3-27B 在 LongBench 或 Needle-in-a-Haystack 测试中，当关键信息位于上下文开头（位置偏差）时，相较于位于中间位置时的准确率下降百分比（量化注意力衰减的方向性偏差）

## Corrected Claim

Qwen3-27B 在长文本测试中可能存在位置偏差，但具体准确率下降百分比需依据特定测试报告确定，无通用固定值。

## Evidence

[质询]该陈述包含具体的量化指标（准确率下降百分比），属于经验事实。虽然Qwen3系列模型通常具备较强的长文本处理能力，但‘位置偏差导致准确率显著下降’这一具体现象及其量化幅度并非第一性原理可推导的必然结论，且不同版本、不同测试设置下结果差异巨大，缺乏通用定值。 | 经验事实，逻辑自洽但缺来源支持；检索无可用来源，无法验证具体数值或方向性偏差的普遍性。

## Search Query

Qwen3-27B long context position bias attention decay rate
