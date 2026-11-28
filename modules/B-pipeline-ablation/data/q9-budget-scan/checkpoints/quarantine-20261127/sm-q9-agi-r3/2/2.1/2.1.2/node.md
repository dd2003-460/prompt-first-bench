# N40: 在 >64k tokens 的长上下文中，Transformer 模型的 'Lost in the Middle' 效应导致中间位置信息的召回率下降约 15-3

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N12

## Claim

在 >64k tokens 的长上下文中，Transformer 模型的 'Lost in the Middle' 效应导致中间位置信息的召回率下降约 15-30%；量化表现为：当关键事实位于上下文第 50% 处时，基于该事实的回答准确率比位于头部或尾部时低 20-40 个百分点，因此科研闭环中的假设生成步骤需采用 RAG 重排序或滑动窗口策略，将关键证据移至上下文首尾 10% 区域以提升可靠性。

## Corrected Claim

在长上下文中，Transformer 模型普遍存在 'Lost in the Middle' 效应，导致中间位置信息的利用效率低于首尾位置，从而降低基于中间关键事实的回答准确率；因此，在科研闭环等高精度场景中，建议采用 RAG 重排序或滑动窗口等策略优化关键证据的位置分布以提升可靠性。

## Evidence

[质询]数值精度与普适性存疑：'Lost in the Middle' 效应的具体降幅（15-30% 召回率下降，20-40 个百分点准确率差异）高度依赖于具体的模型架构、上下文长度及任务类型，并非固定常数；此外，将‘召回率’与‘回答准确率’混用不同量纲的百分比进行对比，且声称‘必须’采用特定策略（RAG/滑动窗口）作为唯一解，缺乏绝对逻辑必然性。 | 先验知识/题面给定，逻辑校验通过：该现象（Lost in the Middle）在 Transformer 长上下文处理中已被广泛证实，量级符合一般认知，但具体数值区间为经验估计而非严格定理，故降级为定性表述。

## Search Query

lost in the middle effect quantitative accuracy drop long context LLM benchmark
