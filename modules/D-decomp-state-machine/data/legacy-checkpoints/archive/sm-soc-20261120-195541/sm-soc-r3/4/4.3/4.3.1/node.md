# N48: 买家浏览-咨询转化率 (CVR) 的计算公式：CVR = N_consult / N_views，需在降价后 48 小时窗口内统计；若 ΔCVR = CVR_p

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N15

## Claim

买家浏览-咨询转化率 (CVR) 的计算公式：CVR = N_consult / N_views，需在降价后 48 小时窗口内统计；若 ΔCVR = CVR_post - CVR_pre 的 95% 置信区间包含 0 (p > 0.05)，则支持‘买家非主动搜索’假设。

## Corrected Claim

买家浏览-咨询转化率 (CVR) 的计算公式：CVR = N_consult / N_views，需在降价后 48 小时窗口内统计；若 ΔCVR = CVR_post - CVR_pre 的 95% 置信区间包含 0 (p > 0.05)，则支持‘买家非主动搜索’假设。

## Evidence

父节点级核验未通过：不完备（子节点1（单样本置信区间）与子节点2（双样本Z检验）在统计逻辑上存在功能重叠且不完全正交。父节点要求判断ΔCVR的置信区间是否包含0，这本质上是一个双样本比例差异的检验问题。子节点1仅计算了CVR_post的单侧置信区间，并未直接回答ΔCVR的显著性（除非结合CVR_pre的点估计，但这不是标准做法），而子节点2提供了正确的双样本Z检验方法。因此，子节点1对于回答父节点的核心问题（ΔCVR显著性）是冗余或不必要的，且与子节点2在目的上冲突（一个侧重单样本CI，一个侧重双样本检验）。此外，父节点未明确CVR_pre的统计窗口，子节点也未覆盖此前提。）
