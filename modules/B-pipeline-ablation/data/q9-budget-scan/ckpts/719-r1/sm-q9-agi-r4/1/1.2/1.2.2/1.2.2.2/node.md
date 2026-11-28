# N128: 长上下文注意力衰减的理论模型：基于 Transformer 注意力机制，距离越远的 token 注意力权重越低；在 128K 上下文中，中间位置的 token 

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N35

## Claim

长上下文注意力衰减的理论模型：基于 Transformer 注意力机制，距离越远的 token 注意力权重越低；在 128K 上下文中，中间位置的 token 与 query 的平均距离大于开头位置，导致注意力分散，准确率下降幅度与上下文长度的平方根成正比 [待核验]

## Corrected Claim

长上下文注意力衰减的理论模型：基于 Transformer 注意力机制，距离越远的 token 注意力权重通常越低；在长上下文中，中间位置的 token 往往比开头或结尾位置更难被有效关注（即“迷失在中间”现象），导致准确率下降，但具体下降幅度与上下文长度的定量关系依赖于具体模型和任务，并非简单的平方根正比关系。

## Evidence

[质询]“准确率下降幅度与上下文长度的平方根成正比”这一具体数学关系缺乏普遍公认的理论推导支持，属于过度简化的经验拟合或特定实验观察，并非Transformer注意力机制的通用第一性原理结论。 | 先验知识/题面给定，逻辑校验通过：注意力随距离衰减及中间位置劣势（Lost in the Middle）现象符合Transformer机制直觉，但具体的“平方根”定量关系缺乏普适理论支撑，故降级为定性描述。

## Search Query

transformer attention decay long context distance impact accuracy theoretical model
