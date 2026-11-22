# N68: 买家福利变化积分公式中的 $g(P)$ 为买家估值分布。买家福利提升 $\Delta U_b$ 不仅来自价格降低，还来自‘搜索成本’ $C_{search}$ 

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N15

## Claim

买家福利变化积分公式中的 $g(P)$ 为买家估值分布。买家福利提升 $\Delta U_b$ 不仅来自价格降低，还来自‘搜索成本’ $C_{search}$ 的变化。若信息透明化使买家更快识别真实价值，搜索时间 $T_{search}$ 从 $t_1$ 降至 $t_2$，则 $\Delta U_b = \int (P_{old} - P_{new}) g(P) dP + C_{time}(t_1 - t_2)$。若 $C_{time}$ 较高（如买家为高频用户），则福利提升幅度大于单纯的价格差。量化：假设 $t_1 = 30min, t_2 = 15min$，时间价值 $v_t = 50元/h$，则单用户额外福利 $+12.5$ 元。

## Corrected Claim

买家福利变化积分公式中的 $g(P)$ 为买家估值分布。买家福利提升 $\Delta U_b$ 不仅来自价格降低，还来自‘搜索成本’ $C_{search}$ 的变化。若信息透明化使买家更快识别真实价值，搜索时间 $T_{search}$ 从 $t_1$ 降至 $t_2$，则 $\Delta U_b = \int (P_{old} - P_{new}) g(P) dP + C_{time}(t_1 - t_2)$。若 $C_{time}$ 较高（如买家为高频用户），则福利提升幅度大于单纯的价格差。量化：假设 $t_1 = 30min, t_2 = 15min$，时间价值 $v_t = 50元/h$，则单用户额外福利 $+12.5$ 元。

## Evidence

父节点级核验失败（LLM 错误）：Invalid \escape: line 5 column 195 (char 261)

## Search Query

buyer welfare gain from price transparency search time reduction valuation distribution
