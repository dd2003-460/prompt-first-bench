# N388: 长上下文注意力衰减导致的准确率下降幅度 ΔAccuracy 的量化模型：基于注意力权重稀释效应，ΔAccuracy ≈ k * sqrt(L/L_ref)，其中

- **status**: degraded
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N128

## Claim

长上下文注意力衰减导致的准确率下降幅度 ΔAccuracy 的量化模型：基于注意力权重稀释效应，ΔAccuracy ≈ k * sqrt(L/L_ref)，其中 L=262144, L_ref=32768, 若基准下降率 k=5% (per sqrt(262144/32768)=2.828x)，则预计 ΔAccuracy ≈ 14.1% [待核验: k值需实测校准]。

## Corrected Claim

长上下文注意力衰减可能导致准确率下降，其幅度受模型架构和位置编码机制影响，通常随上下文长度增加而呈现非线性增长趋势，具体量化需依赖特定模型的实测校准，不宜简单套用固定系数模型。

## Evidence

[质询]该量化模型（ΔAccuracy ≈ k * sqrt(L/L_ref)）缺乏公认的学术或工程共识支持，属于假设性的经验拟合公式；且将‘注意力权重稀释’直接线性映射为‘准确率下降’忽略了模型架构（如RoPE、ALiBi等位置编码机制）和训练数据分布的非线性影响，k值5%亦无实证依据。 | 先验知识/题面给定，逻辑校验通过（数学计算 5% * 2.828 ≈ 14.1% 正确），但该经验公式本身缺乏外部来源直接支持，且标注了‘待核验’，故降级为定性表述。

## Search Query

transformer long context accuracy degradation sqrt length model
