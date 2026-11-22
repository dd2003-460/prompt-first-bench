# N48: 参数一致性检验的约束条件1：成交周期 $T_{sale}$ 较短的充分条件。根据 N7，$T_{sale} \propto 1/A_{eff}$，且 $A_{e

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N9

## Claim

参数一致性检验的约束条件1：成交周期 $T_{sale}$ 较短的充分条件。根据 N7，$T_{sale} \propto 1/A_{eff}$，且 $A_{eff} = A_{base}(1 + \alpha I_{new})$。要使 $T_{sale}$ 显著短于常态（例如 $T_{sale} < 0.5 T_{normal}$），需满足 $\alpha I_{new} > 1$。假设 $I_{new}=1$（新上架标识），则需 $\alpha > 1$。此条件与 $P_{ask}$ 的具体数值无关，仅依赖于平台对新品的曝光加权系数 $\alpha$。

## Corrected Claim

参数一致性检验的约束条件1：成交周期 $T_{sale}$ 较短的充分条件。根据 N7，$T_{sale} \propto 1/A_{eff}$，且 $A_{eff} = A_{base}(1 + \alpha I_{new})$。要使 $T_{sale}$ 显著短于常态（例如 $T_{sale} < 0.5 T_{normal}$），需满足 $\alpha I_{new} > 1$。假设 $I_{new}=1$（新上架标识），则需 $\alpha > 1$。此条件与 $P_{ask}$ 的具体数值无关，仅依赖于平台对新品的曝光加权系数 $\alpha$。

## Evidence

先验知识/题面给定，逻辑校验通过：由 T_sale ∝ 1/A_eff 及 A_eff = A_base(1 + αI_new) 推导，T_sale < 0.5 T_normal 等价于 A_eff > 2 A_base，即 1 + αI_new > 2，在 I_new=1 时得 α > 1，推导自洽且量纲正确。
