# N104: E_high 的分子 %ΔConsultations 需修正为'有效咨询率'，即剔除机器人/无效咨询后的 CTR_effective = (Unique_Use

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N27, N28, N29

## Claim

E_high 的分子 %ΔConsultations 需修正为'有效咨询率'，即剔除机器人/无效咨询后的 CTR_effective = (Unique_User_Queries / Impressions)，以排除平台流量注水导致的虚假弹性。

## Corrected Claim

E_high 的分子 %ΔConsultations 需修正为'有效咨询率'，即剔除机器人/无效咨询后的 CTR_effective = (Unique_User_Queries / Impressions)，以排除平台流量注水导致的虚假弹性。

## Evidence

父节点级核验未通过：非正交（子节点1和子节点2在数学逻辑上存在矛盾且非正交。子节点1通过分子端剔除无效咨询（乘以(1-0.15)）来降低CTR，而子节点2通过分母端剔除注水流量（除以(1-0.1)）来提高CTR。然而，'无效咨询'（如机器人）通常也伴随'无效曝光'（Impressions），两者并非独立维度。若同时应用这两个修正，逻辑上会双重计数或相互抵消，导致最终CTR计算错误。正交性要求子节点处理互不影响的独立变量，但这里两者都作用于'有效流量'的定义，且方向相反，构成逻辑冲突。）

## Search Query

unique user queries vs impressions CTR correction bot filter
