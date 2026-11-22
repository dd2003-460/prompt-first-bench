# N272: 算法屏蔽假设 (H_algo) 的区分性证据：若 CTR 无显著变化（|ΔCTR| < 5%, p>0.1），但‘降价商品’的曝光量 (Impressions)

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N98

## Claim

算法屏蔽假设 (H_algo) 的区分性证据：若 CTR 无显著变化（|ΔCTR| < 5%, p>0.1），但‘降价商品’的曝光量 (Impressions) 相对基准衰减 > 50%，且该衰减与降价幅度正相关（相关系数 r > 0.6），则支持 H_algo，此时 N98 中‘信号失效’假设的置信度应降至 0.10，而 N77 中‘算法屏蔽’假设的置信度应相应上调。

## Corrected Claim

若 CTR 无显著变化，但‘降价商品’的曝光量相对基准显著衰减，且该衰减与降价幅度正相关，则支持 H_algo（算法屏蔽假设），此时‘信号失效’假设的置信度应降低，而‘算法屏蔽’假设的置信度应上调。

## Evidence

[质询]该陈述包含具体的统计阈值（如 |ΔCTR| < 5%, p>0.1, r > 0.6）和置信度调整数值（0.10），这些属于经验性参数或特定研究/业务场景下的设定，无法从第一性原理或数学公理中严格推导出来。若缺乏特定来源支持这些具体数值，则其普适性存疑。 | 逻辑自洽：CTR 无变化但曝光量显著下降且与降价幅度正相关，确实指向算法层面的屏蔽而非用户兴趣变化（信号失效）。但具体阈值和置信度数值属于经验事实，且本轮检索无可用来源支持，故降级。

## Search Query

platform algorithm exposure suppression price reduction second hand market impression decay correlation
