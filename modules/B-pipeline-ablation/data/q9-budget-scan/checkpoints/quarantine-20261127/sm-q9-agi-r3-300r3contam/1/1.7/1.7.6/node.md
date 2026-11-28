# N53: p_base 的领域依赖性量化：在数学推理任务中 p_base ~ 0.55，在事实检索任务中 p_base ~ 0.75，在创意生成任务中 p_base ~ 

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N13, N14, N19

## Claim

p_base 的领域依赖性量化：在数学推理任务中 p_base ~ 0.55，在事实检索任务中 p_base ~ 0.75，在创意生成任务中 p_base ~ 0.40，需按任务类型加权计算综合 p_base 以修正 IR(K) 模型。

## Corrected Claim

p_base 具有领域依赖性，通常认为在事实检索任务中较高，在创意生成任务中较低，具体数值需根据实际基准测试确定，建议按任务类型加权计算以修正 IR(K) 模型。

## Evidence

[质询]该陈述包含具体的经验数值（p_base 在不同任务下的具体概率值），属于经验事实而非第一性原理可推导内容，且参考来源完全无关，缺乏数据支撑。 | 参考来源 [1] 讨论的是 Anthropic 关于质因数分解复杂度的传闻，与 p_base 的领域依赖性量化完全无关，无可用外部证据；该陈述为经验事实，逻辑自洽但缺来源支持。

## Search Query

LLM self-critique error detection rate by task type math fact creative

## Retrieval Sources

- {'url': 'https://www.zhihu.com/question/2107272668999438476&rut=33fc9c80732a48cd4c524ebec263cfa884f5c6518262fac3fbfb577d2f68288e', 'type': 'ddg', 'title': '如何评价网传 Anthropic 在 MIT 闭门会议上称「质因数分解属于 P」？'}
