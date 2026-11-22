# N324: CV计算的'近30天'时间窗口选择依据：时间窗口W应覆盖至少一个完整的'供需波动周期'。若品类成交量Q_7d波动剧烈（CV_Q>0.2），则W=30天可能不足，

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N94

## Claim

CV计算的'近30天'时间窗口选择依据：时间窗口W应覆盖至少一个完整的'供需波动周期'。若品类成交量Q_7d波动剧烈（CV_Q>0.2），则W=30天可能不足，需扩展至W=60天或W=90天。量化影响：W缩短导致σ_price低估，CV偏低。需检验W对CV的敏感性：dCV/dW，若|dCV/dW|>0.01/day，则W=30天为不稳定窗口，需调整。

## Corrected Claim

CV计算的'近30天'时间窗口选择依据：时间窗口W应覆盖至少一个完整的'供需波动周期'。若品类成交量Q_7d波动剧烈（CV_Q>0.2），则W=30天可能不足，需扩展至W=60天或W=90天。量化影响：W缩短导致σ_price低估，CV偏低。需检验W对CV的敏感性：dCV/dW，若|dCV/dW|>0.01/day，则W=30天为不稳定窗口，需调整。

## Evidence

先验知识/题面给定，逻辑校验通过
