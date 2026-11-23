# N87: 长文本一致性验证指标：在 32K 上下文下，4-bit 量化的重复率 (Repetition Penalty) 需控制在 <0.1，否则视为不可接受；当前 GP

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N24

## Claim

长文本一致性验证指标：在 32K 上下文下，4-bit 量化的重复率 (Repetition Penalty) 需控制在 <0.1，否则视为不可接受；当前 GPTQ 算法在该指标上平均值为 0.08

## Corrected Claim

长文本一致性验证中，4-bit 量化模型的重复率需控制在较低水平（如 <0.1）以保证可用性；GPTQ 算法在该指标上通常表现良好，但具体数值需依据实际基准测试确定。

## Evidence

[质询]该陈述包含具体的经验性阈值（<0.1）和特定算法（GPTQ）在特定场景（32K上下文）下的具体统计值（0.08），这些属于经验事实而非第一性原理可推导内容，且缺乏外部来源支持，存在数值虚构或口径混淆的风险。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

4-bit quantization long text consistency repetition penalty LLM
