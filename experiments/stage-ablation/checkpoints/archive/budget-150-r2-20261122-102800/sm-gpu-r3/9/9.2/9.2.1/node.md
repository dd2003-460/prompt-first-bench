# N383: MATH基准测试集（MATH-500）包含500道高中数学竞赛级别题目，涵盖代数、几何、数论等7个子领域；Qwen3-27B在BF16下的基准分约为80%，在W

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N153

## Claim

MATH基准测试集（MATH-500）包含500道高中数学竞赛级别题目，涵盖代数、几何、数论等7个子领域；Qwen3-27B在BF16下的基准分约为80%，在W4量化下降至66%，绝对损失14个百分点，相对损失17.5%，高于GSM8K的相对损失，表明MATH任务对4-bit量化更为敏感。

## Corrected Claim

MATH基准测试集（MATH-500）包含500道高中数学竞赛级别题目，涵盖代数、几何、数论等7个子领域；在典型4-bit量化方案下，Qwen3-27B在MATH任务上的性能通常会出现显著下降（相对损失常高于GSM8K），表明MATH任务对量化更为敏感。

## Evidence

[质询]具体数值（80%、66%、14pp、17.5%）及与GSM8K的对比结论属于特定实验条件下的经验事实，缺乏通用性，且不同量化方法（如GPTQ, AWQ, SmoothQuant）和校准集会导致结果显著差异，直接断言‘约为’可能掩盖了方法依赖性。 | source=knowledge，逻辑自洽（14/80=17.5%计算正确，MATH难度高于GSM8K符合直觉），但具体数值为经验事实，无外部来源支持，依据经验事实排除条款降级。

## Search Query

MATH benchmark 500 questions Qwen3-27B W4 quantization accuracy drop
