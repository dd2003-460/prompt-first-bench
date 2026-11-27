# N150: 工作点 A (高频热点对象)：当 R_i 极高（如第 1 名，τ_res(i) << τ_obj）时，P_valid(i) ≈ 1 - (1 - e^(-0.0

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N48

## Claim

工作点 A (高频热点对象)：当 R_i 极高（如第 1 名，τ_res(i) << τ_obj）时，P_valid(i) ≈ 1 - (1 - e^(-0.01)) * (τ_res(i)/100) ≈ 0.9999，失效概率可忽略，该对象始终有效。

## Corrected Claim

工作点 A (高频热点对象)：当 R_i 极高（如第 1 名，τ_res(i) << τ_obj）时，P_valid(i) ≈ 1 - (1 - e^(-0.01)) * (τ_res(i)/100) ≈ 0.9999，失效概率可忽略，该对象始终有效。

## Evidence

先验知识/题面给定，逻辑校验通过：当 τ_res(i) << τ_obj 且系数极小（0.01）时，失效概率项趋近于0，P_valid 趋近于1，数值量级与逻辑推导自洽。
