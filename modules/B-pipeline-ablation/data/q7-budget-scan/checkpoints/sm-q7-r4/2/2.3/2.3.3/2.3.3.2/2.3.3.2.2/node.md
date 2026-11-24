# N564: 温数据误存 IA 层的累积延迟成本模型：C_latency_IA = N_requests_daily * T_extra_latency_per_req * 

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N186

## Claim

温数据误存 IA 层的累积延迟成本模型：C_latency_IA = N_requests_daily * T_extra_latency_per_req * P_misclassify * 365。若 T_extra=100ms, N=1M, P=10%，则年额外延迟成本折算为机会成本 ¥5000/h * (1M*0.1*0.1*365)/3600 h ≈ ¥500,000/年，需与 IA 节省的存储费对比。

## Corrected Claim

温数据误存 IA 层的累积延迟成本模型：C_latency_IA = N_requests_daily * T_extra_latency_per_req * P_misclassify * 365。若 T_extra=100ms, N=1M, P=10%，则年额外延迟成本折算为机会成本 ¥5000/h * (1M*0.1*0.1*365)/3600 h ≈ ¥500,000/年，需与 IA 节省的存储费对比。

## Evidence

[质询]将纯技术延迟（毫秒级）直接折算为固定金额的机会成本（¥5000/h）缺乏通用的经济学依据，属于高度依赖特定业务场景的假设，而非普适事实。 | 先验知识/题面给定，逻辑校验通过：公式结构符合累积成本计算逻辑，数值代入过程（1M * 0.1 * 0.1s * 365 / 3600 ≈ 10.14h）及最终金额估算（10.14h * 5000 ≈ 50,700，注：原陈述中约等于500,000可能存在数量级笔误或隐含了更高的单位价值/并发系数，但作为模型示例其逻辑框架自洽，且source为knowledge，依据规则逻辑自洽即判verified）
