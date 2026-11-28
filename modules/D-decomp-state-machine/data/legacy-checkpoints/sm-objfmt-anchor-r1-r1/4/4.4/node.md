# N24: 量化精度质量损失量化指标：定义PPL（Perplexity）增量ΔPPL和下游任务准确率下降ΔAcc作为可计算代理，基于公开论文/社区评测获取Qwen3系列在F

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4

## Claim

量化精度质量损失量化指标：定义PPL（Perplexity）增量ΔPPL和下游任务准确率下降ΔAcc作为可计算代理，基于公开论文/社区评测获取Qwen3系列在FP8/INT8/NVFP4下的平均ΔPPL值，无数据时标[待核验]并引用同规模模型（Llama3-70B）近似值

## Corrected Claim

量化精度质量损失量化指标：定义PPL（Perplexity）增量ΔPPL和下游任务准确率下降ΔAcc作为可计算代理，基于公开论文/社区评测获取Qwen3系列在FP8/INT8/NVFP4下的平均ΔPPL值，无数据时标[待核验]并引用同规模模型（Llama3-70B）近似值

## Evidence

先验知识/题面给定，逻辑校验通过：PPL和Acc是标准的量化评估指标，定义清晰且符合工程实践；虽无具体数值，但作为方法论描述逻辑自洽。

## Search Query

Qwen3 quantization perplexity degradation FP8 INT8 NVFP4 evaluation
