# N392: FP8 KV Cache 在 L=128k 长度下的 Coherence Error Rate (CER_FP8_128k) 实测值：用于消除长度混杂因素，验证

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N129

## Claim

FP8 KV Cache 在 L=128k 长度下的 Coherence Error Rate (CER_FP8_128k) 实测值：用于消除长度混杂因素，验证 ΔCER 是否随 L 非线性增长，预期值高于 L=64k 的情况 [待核验]。

## Corrected Claim

FP8 KV Cache 在 L=128k 长度下的 Coherence Error Rate (CER_FP8_128k) 的具体实测值需依赖特定实验环境的数据；理论上，随着序列长度增加，累积误差可能导致 CER 上升，但具体数值及非线性增长特性需实证验证。

## Evidence

[质询]该陈述声称拥有具体的“实测值”（Empirical Value），但在缺乏任何实验数据、论文引用或基准测试报告的情况下，断言具体的数值或趋势（如“预期值高于...”）属于无据的经验事实主张。此外，FP8 KV Cache 的 Coherence Error Rate 并非标准通用指标，其定义和测量方法未明确，导致“实测值”这一说法在逻辑上缺乏支撑基础。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且该具体实测数据无法从第一性原理推导，属于特定实验结果）。

## Search Query

vLLM FP8 KV cache coherence error rate benchmark 128k context
