# N63: 下游投影 3（打破均衡的临界条件）：平台打破均衡的临界点为 ΔGMV_loss * Fee_rate > ΔAd_revenue_gain；量化为：当挂价下调导

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N12

## Claim

下游投影 3（打破均衡的临界条件）：平台打破均衡的临界点为 ΔGMV_loss * Fee_rate > ΔAd_revenue_gain；量化为：当挂价下调导致 GMV 下降 ΔGMV_loss 时，若 ΔGMV_loss * Fee_rate > δ_ad * N_unsold * ΔTime_on_site，则平台有动力干预；该不等式定义了平台从“被动受益者”转向“主动干预者”的财务阈值，具体数值需根据平台实际费率与广告单价校准。

## Corrected Claim

下游投影 3（打破均衡的临界条件）：平台打破均衡的临界点为 ΔGMV_loss * Fee_rate > ΔAd_revenue_gain；量化为：当挂价下调导致 GMV 下降 ΔGMV_loss 时，若 ΔGMV_loss * Fee_rate > δ_ad * N_unsold * ΔTime_on_site，则平台有动力干预；该不等式定义了平台从“被动受益者”转向“主动干预者”的财务阈值，具体数值需根据平台实际费率与广告单价校准。

## Evidence

父节点级核验未通过：不完备（子节点在逻辑上是正交的（分别处理噪声、左侧项、右侧项、综合求解），且无冗余。但在完备性上存在缺失：父节点明确提到临界条件涉及‘打破均衡’，且子节点4提到了‘最小挂价下调比例’，但子节点中缺少对‘均衡状态’或‘市场供需平衡’本身的定义或量化（即没有解释为什么 GMV 下降会打破均衡，或者均衡的基准是什么）。此外，子节点1提到的随机扰动 σ_match 是外部噪声，而父节点主要描述的是确定性的财务阈值，虽然相关，但子节点未涵盖‘均衡’这一核心概念的具体量化或定义，导致对‘打破均衡’这一前提条件的解释不完整。）

## Search Query

platform intervention threshold GMV loss advertising revenue gain break even point
