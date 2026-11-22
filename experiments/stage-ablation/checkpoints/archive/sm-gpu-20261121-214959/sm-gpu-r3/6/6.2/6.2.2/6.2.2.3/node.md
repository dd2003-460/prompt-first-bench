# N293: FP8 量化在通用对话任务 (MT-Bench) 上的具体质量损失：基于 N122，FP8 在 MT-Bench 上准确率下降 <0.5% [待核验]，在 IF

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N106

## Claim

FP8 量化在通用对话任务 (MT-Bench) 上的具体质量损失：基于 N122，FP8 在 MT-Bench 上准确率下降 <0.5% [待核验]，在 IFEval 上下降 <0.5% [待核验]。此损失在通用对话场景中几乎不可感知，故 FP8 为性价比最优精度。在 Mac Studio 上，FP8 方案 CapEx $6,999，TCO(5年) = $6,999 + 5*$6132 (假设功耗 700W) = $37,659，低于 2x 4090 的 $44,618 (N127)。

## Corrected Claim

FP8 量化在通用对话任务 (MT-Bench) 和指令遵循 (IFEval) 上的质量损失通常较小（具体数值取决于模型和量化方法，一般认为在可接受范围内），在 Mac Studio 上，FP8 方案 CapEx $6,999，TCO(5年) = $37,659，低于 2x 4090 的 $44,618。

## Evidence

[质询]MT-Bench 和 IFEval 的得分通常以 1-10 分制或百分比准确率呈现，'下降 <0.5%' 的表述存在量纲歧义（是绝对分数下降 0.5 分，还是相对准确率下降 0.5%？）。此外，FP8 在通用对话任务上的具体质量损失属于经验事实，不同模型架构和量化实现（如 SmoothQuant, GPTQ）结果差异较大，缺乏特定上下文下的直接数据支持。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且该数据为具体实验结果，非第一性原理可推导）

## Search Query

Qwen3-27B FP8 MT-Bench IFEval accuracy drop
