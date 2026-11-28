# N96: INT8 量化对长文本生成一致性的量化指标：在 32K 上下文下，INT8 模型的重复率（Repetition Penalty 触发频率）比 BF16 高 15

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N21

## Claim

INT8 量化对长文本生成一致性的量化指标：在 32K 上下文下，INT8 模型的重复率（Repetition Penalty 触发频率）比 BF16 高 15-25%，导致长文本连贯性评分（Coherence Score）下降约 3-5 分（满分 10）[待核验]

## Corrected Claim

INT8 量化通常会导致长文本生成中重复率上升及连贯性评分轻微下降，但具体幅度（如重复率增幅15-25%、评分下降3-5分）高度依赖于模型规模、量化方法及评估数据集，需结合具体实验报告确认。

## Evidence

[质询]具体数值（15-25%重复率增幅、3-5分连贯性下降）缺乏通用基准支持，不同模型架构、量化算法（如SmoothQuant, GPTQ）及评估协议下差异巨大，属于特定实验条件下的经验数据而非普适规律。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且具体量化指标非第一性原理可推导）

## Search Query

INT8 quantization long text generation consistency repetition rate increase 32K context
