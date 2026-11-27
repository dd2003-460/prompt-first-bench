# N112: 点击率与价格偏离度的负相关强度量化：计算皮尔逊相关系数 $\rho = \frac{Cov(CTR, \Delta P)}{\sigma_{CTR}\sigma

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N44

## Claim

点击率与价格偏离度的负相关强度量化：计算皮尔逊相关系数 $\rho = \frac{Cov(CTR, \Delta P)}{\sigma_{CTR}\sigma_{\Delta P}}$，其中 $\Delta P = (P_{ask}-P_{mkt})/P_{mkt}$；若 $\rho < -0.3$ 且 $p < 0.01$，则确认'买家对高挂价有显著惩罚'，此时'买家忽略挂价'的置信度应从0.8下调至0.5。

## Corrected Claim

点击率与价格偏离度的负相关强度量化：计算皮尔逊相关系数 $\rho = \frac{Cov(CTR, \Delta P)}{\sigma_{CTR}\sigma_{\Delta P}}$，其中 $\Delta P = (P_{ask}-P_{mkt})/P_{mkt}$；若 $\rho < -0.3$ 且 $p < 0.01$，则确认'买家对高挂价有显著惩罚'，此时'买家忽略挂价'的置信度应从0.8下调至0.5。

## Evidence

先验知识/题面给定，逻辑校验通过
