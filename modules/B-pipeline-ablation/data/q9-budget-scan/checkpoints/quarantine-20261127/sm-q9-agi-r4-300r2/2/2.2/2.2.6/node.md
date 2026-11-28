# N53: Critic 角色的 Token 消耗模型：Critic 输入为初稿全文 (L tokens)，输出为修改建议 (0.2L tokens)；总 Token 消耗

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N12, N13, N14

## Claim

Critic 角色的 Token 消耗模型：Critic 输入为初稿全文 (L tokens)，输出为修改建议 (0.2L tokens)；总 Token 消耗 = L + 0.2L + 0.2L (Re-generation) = 1.4L，相比无 Critic 的 L tokens，开销增加 40%；若初稿包含数学公式，Token 计数需乘以 1.2 系数以反映特殊字符占比。

## Corrected Claim

Critic 角色的 Token 消耗模型通常由输入初稿、输出建议及可能的重生成部分组成。具体比例（如输出占输入的20%、数学公式系数1.2等）取决于具体模型和任务场景，需根据实际基准测试数据确定，不能视为固定常数。

## Evidence

[质询]该陈述包含具体的经验性参数（如输出比例0.2L、重生成比例0.2L、数学公式系数1.2），这些并非第一性原理可推导的数学或物理常数，而是依赖于特定模型行为、任务复杂度及编码方式的经验估计值，缺乏通用性。 | source=knowledge，逻辑自洽（1+0.2+0.2=1.4，1.4-1=0.4即40%），但具体系数属于经验事实，无外部来源支持，依据经验事实排除条款降级。
