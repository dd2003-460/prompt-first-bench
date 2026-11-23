# N120: POP 点数量 N_POP 与单点带宽 B_pop 的耦合约束：N_POP * B_pop ≥ B_total_peak，且单点存储容量 C_pop ≥ s_a

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N33

## Claim

POP 点数量 N_POP 与单点带宽 B_pop 的耦合约束：N_POP * B_pop ≥ B_total_peak，且单点存储容量 C_pop ≥ s_avg * N_unique_hot_region；当 N_POP 从 10 增至 15 时，单点带宽需求从 4.2Gbps 降至 2.8Gbps，但单点存储需求从 7.68TB 降至 5.12TB，总存储 Capex 降低 33%，而总带宽 Capex 降低 33%，综合 TCO 降低约 25%。

## Corrected Claim

当 N_POP 从 10 增至 15 时，单点带宽需求从 4.2Gbps 降至 2.8Gbps，单点存储需求从 7.68TB 降至 5.12TB。若假设单点带宽和存储的边际成本恒定且忽略其他TCO因素，总带宽和存储Capex均降低约33%，综合TCO降低幅度取决于带宽与存储在总TCO中的权重，通常在25%-33%之间。

## Evidence

[质询]数值量级与逻辑自洽性存疑：1. 存储需求从7.68TB降至5.12TB，降幅为33.3%，但总存储Capex降低33%意味着单点存储成本未变，这与通常的规模效应（单点成本随容量增加而边际递减或固定成本分摊）不符，且未说明存储单价是否恒定；2. 带宽需求从4.2Gbps降至2.8Gbps，降幅为33.3%，总带宽Capex降低33%同样假设单点带宽成本线性且无规模效应；3. 综合TCO降低25%是存储和带宽Capex降低33%的加权平均，但权重未给出，且忽略了运维、电力等其他TCO组成部分，直接得出25%缺乏依据。 | 先验知识/题面给定，逻辑校验未通过：数值推导中隐含了成本线性假设且忽略了TCO的其他组成部分，导致综合TCO降低25%的结论缺乏严谨支撑。

## Search Query

CDN POP point count bandwidth storage capacity coupling constraint TCO optimization
