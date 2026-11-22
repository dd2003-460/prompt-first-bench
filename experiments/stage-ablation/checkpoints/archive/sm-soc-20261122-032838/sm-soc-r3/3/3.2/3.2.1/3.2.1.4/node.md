# N206: 买家估值分布 $g(P)$ 的参数化：假设 $V \sim N(\mu_v, \sigma_v^2)$，其中 $\mu_v = P_{ref}$，$\sigma

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N67, N68, N69

## Claim

买家估值分布 $g(P)$ 的参数化：假设 $V \sim N(\mu_v, \sigma_v^2)$，其中 $\mu_v = P_{ref}$，$\sigma_v = \beta \cdot \sigma_{quality} \cdot P_{ref}$。在二手电子产品市场，$\sigma_{quality}=0.15, \beta=0.8$，则 $\sigma_v = 0.12 P_{ref}$。

## Corrected Claim

买家估值分布 $g(P)$ 的参数化：假设 $V \sim N(\mu_v, \sigma_v^2)$，其中 $\mu_v = P_{ref}$，$\sigma_v = \beta \cdot \sigma_{quality} \cdot P_{ref}$。在二手电子产品市场，$\sigma_{quality}=0.15, \beta=0.8$，则 $\sigma_v = 0.12 P_{ref}$。

## Evidence

先验知识/题面给定，逻辑校验通过：0.8 * 0.15 = 0.12，数值计算正确，参数化假设在二手市场估值模型中逻辑自洽。
