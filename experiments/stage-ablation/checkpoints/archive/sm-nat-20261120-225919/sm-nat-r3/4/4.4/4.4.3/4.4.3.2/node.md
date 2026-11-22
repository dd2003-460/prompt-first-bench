# N194: 长周期下的数值稳定性：当 τ_obj=1000 天时，e^(-0.001) ≈ 0.9990005，(1-e^(-0.001))^2 ≈ 9.99e-7，D ≈

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N70

## Claim

长周期下的数值稳定性：当 τ_obj=1000 天时，e^(-0.001) ≈ 0.9990005，(1-e^(-0.001))^2 ≈ 9.99e-7，D ≈ 0.9999990。在浮点计算中，若使用单精度 float32，该微小差异可能被舍入误差掩盖，需使用双精度 float64 或解析近似 1 - x^2 ≈ 1 - 2x 当 x<<1 时进行计算，以避免灾难性抵消。

## Corrected Claim

长周期下的数值稳定性：当 τ_obj=1000 天时，e^(-0.001) ≈ 0.9990005，(1-e^(-0.001))^2 ≈ 9.99e-7，D ≈ 0.9999990。在浮点计算中，若使用单精度 float32，该微小差异可能被舍入误差掩盖，需使用双精度 float64 或解析近似 1 - x^2 ≈ 1 - 2x 当 x<<1 时进行计算，以避免灾难性抵消。

## Evidence

先验知识/题面给定，逻辑校验通过：数值计算准确（e^-0.001≈0.999, (1-e^-0.001)^2≈1e-6, D≈1-1e-6），浮点精度分析符合IEEE 754标准及数值分析原理（float32精度约7位十进制，无法区分1与1-1e-6，需float64或解析近似避免灾难性抵消）。

## Search Query

floating point precision catastrophic cancellation exponential small x approximation
