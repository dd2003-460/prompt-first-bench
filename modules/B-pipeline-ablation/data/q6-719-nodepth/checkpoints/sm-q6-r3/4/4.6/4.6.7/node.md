# N124: 回源数据传输时间 T_transfer_origin，基于对象大小 s 和源站出口带宽 B_origin，计算公式为 T_transfer_origin = s

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N30

## Claim

回源数据传输时间 T_transfer_origin，基于对象大小 s 和源站出口带宽 B_origin，计算公式为 T_transfer_origin = s / B_origin，P99 值受源站带宽限制和拥塞影响。

## Corrected Claim

回源数据传输时间 T_transfer_origin，基于对象大小 s 和源站出口带宽 B_origin，计算公式为 T_transfer_origin = s / B_origin，P99 值受源站带宽限制和拥塞影响。

## Evidence

父节点级核验未通过：不完备（子节点之间正交性良好，分别关注带宽利用率对性能的影响和带宽规格的选择；但完备性不足，父节点明确提到 P99 受'拥塞影响'，而子节点1仅讨论了高利用率下的 TCP 窗口拥塞，未涵盖网络路径拥塞、丢包重传等其他常见拥塞因素对 P99 的具体影响机制或量化方法。）

## Search Query

CDN origin pull transfer time calculation
