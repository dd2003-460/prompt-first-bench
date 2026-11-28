# N139: Agent 间相关性系数 ρ 的来源分解：ρ = ρ_data + ρ_prompt + ρ_random，其中 ρ_data 源于共享训练数据偏差，ρ_pro

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N55

## Claim

Agent 间相关性系数 ρ 的来源分解：ρ = ρ_data + ρ_prompt + ρ_random，其中 ρ_data 源于共享训练数据偏差，ρ_prompt 源于提示词相似性，ρ_random 源于采样随机性；在相同模型架构下，ρ_data 通常占 ρ 的 60%-80% [待核验]

## Corrected Claim

Agent 间相关性系数 ρ 可分解为数据偏差、提示词相似性及采样随机性等组成部分，其中共享训练数据偏差通常是主要影响因素之一，但其具体占比视具体场景而定。

## Evidence

[质询]该陈述包含具体的经验数值范围（60%-80%）和特定的线性分解公式，属于经验事实。目前缺乏权威文献或实验数据直接支持这一特定比例和分解模型的普适性，不同研究中对各因素权重的估计可能存在显著差异。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源，且该具体数值比例无法从第一性原理严格推出）

## Search Query

LLM agent error correlation sources training data bias prompt similarity
