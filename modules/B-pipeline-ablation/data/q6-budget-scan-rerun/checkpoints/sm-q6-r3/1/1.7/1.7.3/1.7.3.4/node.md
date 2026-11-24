# N175: 公有云CDN带宽升级对延迟的影响：升级带宽套餐（如从500Mbps到1Gbps）主要减少排队延迟。若当前带宽利用率80%，升级后利用率降至40%，排队延迟（M/

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N45

## Claim

公有云CDN带宽升级对延迟的影响：升级带宽套餐（如从500Mbps到1Gbps）主要减少排队延迟。若当前带宽利用率80%，升级后利用率降至40%，排队延迟（M/M/1模型）从 (ρ/(1-ρ)) * Service_Time 降低。假设Service_Time=1ms, ρ=0.8→0.4，排队延迟从4ms降至0.67ms，降低3.33ms。

## Corrected Claim

公有云CDN带宽升级对延迟的影响：升级带宽套餐（如从500Mbps到1Gbps）主要减少排队延迟。若当前带宽利用率80%，升级后利用率降至40%，排队延迟（M/M/1模型）从 (ρ/(1-ρ)) * Service_Time 降低。假设Service_Time=1ms, ρ=0.8→0.4，排队延迟从4ms降至0.67ms，降低3.33ms。

## Evidence

先验知识/题面给定，逻辑校验通过：M/M/1排队模型公式 Wq = (ρ/(1-ρ)) * S 计算正确（0.8/0.2*1=4ms, 0.4/0.6*1≈0.67ms），差值3.33ms符合数学推导。
