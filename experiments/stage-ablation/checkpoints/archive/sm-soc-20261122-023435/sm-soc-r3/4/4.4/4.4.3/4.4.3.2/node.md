# N185: 切换成本 C_switching 的构成：C_switching = C_learning + C_migration + C_reputation_loss，

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N60

## Claim

切换成本 C_switching 的构成：C_switching = C_learning + C_migration + C_reputation_loss，其中 C_learning 为学习新平台规则成本，C_migration 为库存/用户数据迁移成本，C_reputation_loss 为平台内积累信誉的损失，通常量化为过去 12 个月 GMV 的 5-10%。

## Corrected Claim

切换成本 C_switching 的构成：C_switching = C_learning + C_migration + C_reputation_loss，其中 C_learning 为学习新平台规则成本，C_migration 为库存/用户数据迁移成本，C_reputation_loss 为平台内积累信誉的损失，其量化值因行业与平台特性而异，通常需结合具体业务场景估算。

## Evidence

[质询]将C_reputation_loss量化为过去12个月GMV的5-10%缺乏普适性，该比例高度依赖行业特性（如高复购率vs低复购率）、平台生态封闭性及用户粘性，属于经验性估算而非通用常数，且不同文献或模型中该系数差异巨大。 | 先验知识/题面给定，逻辑校验通过（构成项定义合理，量纲一致），但具体量化比例（5-10%）为经验参数，缺乏通用理论支撑或来源直接支持，故降级。

## Search Query

platform switching cost components learning migration reputation
