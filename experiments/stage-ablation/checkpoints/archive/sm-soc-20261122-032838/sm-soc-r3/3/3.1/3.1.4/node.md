# N66: 最小干预的判定标准不仅是 $C_{int}$ 最小，还需考虑‘可逆性成本’ $C_{reverse}$。若干预导致用户流失或卖家大规模下架，恢复原状的成本极高。

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N14

## Claim

最小干预的判定标准不仅是 $C_{int}$ 最小，还需考虑‘可逆性成本’ $C_{reverse}$。若干预导致用户流失或卖家大规模下架，恢复原状的成本极高。方案A（信息透明）一旦实施，买家心理锚点永久改变，$C_{reverse} \to \infty$；方案B（算法降权）可通过参数回滚恢复，$C_{reverse} \approx C_{train}$；方案C（补贴）停止即失效，$C_{reverse} \approx 0$。综合成本 $C_{total} = C_{int} + \gamma C_{reverse}$，其中 $\gamma$ 为风险折现系数。若 $\gamma > 0.5$，方案C或B可能优于A，尽管其初始 $C_{int}$ 较高。

## Corrected Claim

最小干预的判定标准不仅是 $C_{int}$ 最小，还需考虑‘可逆性成本’ $C_{reverse}$。若干预导致用户流失或卖家大规模下架，恢复原状的成本极高。方案A（信息透明）一旦实施，买家心理锚点永久改变，$C_{reverse} \to \infty$；方案B（算法降权）可通过参数回滚恢复，$C_{reverse} \approx C_{train}$；方案C（补贴）停止即失效，$C_{reverse} \approx 0$。综合成本 $C_{total} = C_{int} + \gamma C_{reverse}$，其中 $\gamma$ 为风险折现系数。若 $\gamma > 0.5$，方案C或B可能优于A，尽管其初始 $C_{int}$ 较高。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

reversibility cost of platform policy intervention user behavior anchoring irreversible change
