# N275: 工作点A（高冗余低闲置）：自建核心区域配置利用率目标 U_target=40%，闲置成本 C_idle_self_core_A = C_total_self_c

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N88

## Claim

工作点A（高冗余低闲置）：自建核心区域配置利用率目标 U_target=40%，闲置成本 C_idle_self_core_A = C_total_self_core_annual × (1 - 0.4) / (R_total_annual_core / 1000)，其中 R_total_annual_core = R_total_annual × w_core，C_total_self_core_annual 基于核心区域 POP 数量及单点年成本（N126）计算

## Corrected Claim

工作点A（高冗余低闲置）：自建核心区域配置利用率目标 U_target=40%，闲置成本 C_idle_self_core_A = C_total_self_core_annual × (1 - 0.4) / (R_total_annual_core / 1000)，其中 R_total_annual_core = R_total_annual × w_core，C_total_self_core_annual 基于核心区域 POP 数量及单点年成本（N126）计算

## Evidence

先验知识/题面给定，逻辑校验通过：公式结构符合成本分摊逻辑，量纲一致（年成本/年营收=单位营收成本），参数定义清晰且无内部矛盾。
