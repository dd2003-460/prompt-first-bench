# N137: P99 延迟的非线性阈值验证：当 $H=90\%$ 时，10% 请求回源，若 $L_{backhaul}=50\text{ms}$，$L_{edge}=5\te

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N33

## Claim

P99 延迟的非线性阈值验证：当 $H=90\%$ 时，10% 请求回源，若 $L_{backhaul}=50\text{ms}$，$L_{edge}=5\text{ms}$，则加权平均延迟 $L_{avg} = 0.9 \times 5 + 0.1 \times 55 = 10\text{ms}$，但 P99 延迟主要由那 10% 的回源请求决定，故 $L_{p99} \approx 55\text{ms}$。

## Corrected Claim

P99 延迟的非线性阈值验证：当 $H=90\%$ 时，10% 请求回源，若 $L_{backhaul}=50\text{ms}$，$L_{edge}=5\text{ms}$，则加权平均延迟 $L_{avg} = 0.9 \times 5 + 0.1 \times 55 = 10\text{ms}$，但 P99 延迟主要由那 10% 的回源请求决定，故 $L_{p99} \approx 55\text{ms}$。

## Evidence

先验知识/题面给定，逻辑校验通过：加权平均计算正确（0.9*5 + 0.1*55 = 10ms），P99延迟由尾部高延迟请求主导的逻辑符合统计学直觉。
