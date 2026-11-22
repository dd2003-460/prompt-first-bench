# N9: LRU 稳态字节命中率下界的理论下界公式：HitRate_LRU >= 1 - (TotalByteMiss / TotalByteRequest)，其中 To

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N4

## Claim

LRU 稳态字节命中率下界的理论下界公式：HitRate_LRU >= 1 - (TotalByteMiss / TotalByteRequest)，其中 TotalByteMiss 由 LRU 缓存替换策略下的驱逐字节数决定，需通过工作集大小与缓存容量的比值估算

## Corrected Claim

LRU 稳态字节命中率下界的理论下界公式：HitRate_LRU >= 1 - (TotalByteMiss / TotalByteRequest)，其中 TotalByteMiss 由 LRU 缓存替换策略下的驱逐字节数决定，需通过工作集大小与缓存容量的比值估算

## Evidence

父节点级核验未通过：不完备（子节点分别覆盖了分母（TotalByteRequest）和关键参数（工作集比值R_ws），二者内容正交且无冗余。但父节点明确提到公式中包含 TotalByteMiss，且说明其由驱逐字节数决定，需通过 R_ws 估算。子节点2仅给出了 MissRate 的近似公式，未明确建立 TotalByteMiss 与 TotalByteRequest 及 MissRate 之间的具体换算关系（即 TotalByteMiss = TotalByteRequest * MissRate），导致父节点中核心变量 TotalByteMiss 的计算逻辑在子节点中缺失，覆盖不完备。）

## Search Query

LRU cache hit rate lower bound formula steady state
