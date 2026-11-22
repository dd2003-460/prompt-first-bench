# N122: 惩罚强度系数 α 的品类异质性修正项：α_eff = α_base * (1 + η_var * Var(Q)), 其中 Var(Q) 为商品质量方差，标准化程

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N40

## Claim

惩罚强度系数 α 的品类异质性修正项：α_eff = α_base * (1 + η_var * Var(Q)), 其中 Var(Q) 为商品质量方差，标准化程度越低的非标品（高方差），平台算法对高价的容忍度越低（α_eff 越大），需检索具体品类下的 α 分布。

## Corrected Claim

惩罚强度系数 α 可能存在品类异质性修正，通常非标品（高方差）面临更严格的定价约束，但具体公式 α_eff = α_base * (1 + η_var * Var(Q)) 缺乏公开来源验证，需进一步检索特定平台算法文档或实证研究。

## Evidence

[质询]该公式为特定平台内部算法的黑盒参数，属于经验事实，无法从第一性原理推导，且缺乏公开文献或官方文档支持其具体数学形式及变量定义（如η_var的具体取值或Var(Q)的标准化方式）。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）

## Search Query

marketplace algorithm price sensitivity variance non-standard goods penalty coefficient alpha
