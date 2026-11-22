# N350: INT4 量化对 HumanEval 性能损失高于 MMLU 的机制归因：代码生成任务依赖长距离逻辑依赖和精确 token 序列匹配，AWQ 对权重激活分布的稀

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N118

## Claim

INT4 量化对 HumanEval 性能损失高于 MMLU 的机制归因：代码生成任务依赖长距离逻辑依赖和精确 token 序列匹配，AWQ 对权重激活分布的稀疏性利用导致关键路径权重精度损失在解码阶段被放大，使得 Pass@1 对量化误差的敏感度系数约为 MMLU 的 1.5-2.0 倍 [待核验: 需引用具体消融实验数据]。

## Corrected Claim

INT4 量化对 HumanEval 性能损失通常高于 MMLU，因为代码生成任务依赖长距离逻辑依赖和精确 token 序列匹配，对量化误差更为敏感；具体敏感度系数因模型和量化方法而异，通常显著高于 MMLU 任务。

## Evidence

[质询]该陈述包含具体的经验性数值（敏感度系数1.5-2.0倍）和特定的因果机制归因（AWQ稀疏性利用导致关键路径精度损失放大），这些属于经验事实而非第一性原理可推导内容。虽然逻辑上代码生成对精度更敏感是合理的，但具体的倍数关系和机制细节缺乏普遍公认的定论，且不同量化方法（如GPTQ vs AWQ）和模型架构下结果可能差异巨大，存在过度具体化导致失真的风险。 | 先验知识/题面给定，逻辑校验通过：代码生成任务确实比多选题任务对量化误差更敏感，但具体系数1.5-2.0及特定机制归因属于经验观察，缺乏通用性保证，故降级为定性表述。

## Search Query

why INT4 quantization hurts code generation more than multiple choice tasks LLM
