# N39: 价格偏离度 $Deviation$ 的展示阈值与用户感知：当 $Deviation < 5\%$ 时，买家通常不感知异常；当 $5\% \le Deviatio

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N14

## Claim

价格偏离度 $Deviation$ 的展示阈值与用户感知：当 $Deviation < 5\%$ 时，买家通常不感知异常；当 $5\% \le Deviation \le 15\%$ 时，触发‘可议价’心理预期；当 $Deviation > 15\%$ 时，触发‘高价信号’或‘欺诈/错误’警示。干预设计应针对 $Deviation > 15\%$ 区间进行强制标注，以最大化信息透明化的边际效用。

## Corrected Claim

价格偏离度 $Deviation$ 的展示阈值与用户感知：通常认为，当 $Deviation$ 较小时（如低于一定阈值），买家感知异常的概率较低；随着 $Deviation$ 增大，买家产生‘可议价’或‘高价/异常’心理预期的概率显著上升。干预设计应针对高偏离度区间（如显著高于市场均价）进行强制标注，以提升信息透明度。

## Evidence

[质询]该陈述将具体的心理感知阈值（5%、15%）作为普遍事实陈述，缺乏实证数据支持。不同品类、用户群体及市场环境下，价格敏感度差异巨大，固定百分比阈值可能过于简化，且‘通常不感知’与‘触发警示’属于主观心理判断，难以用单一数值区间精确界定。 | source=knowledge，逻辑自洽（阈值设计符合一般经济学直觉），但具体数值（5%/15%）属于经验性参数，缺乏普适性实证支持，故降级为定性表述。

## Search Query

price deviation threshold consumer perception bargaining expectation study
