# N64: 回源链路排队延迟 $L_{queue}$ 与链路利用率 $\rho$ 呈非线性关系：在 M/M/1 模型下，$L_{queue} \approx L_{serv

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N13

## Claim

回源链路排队延迟 $L_{queue}$ 与链路利用率 $\rho$ 呈非线性关系：在 M/M/1 模型下，$L_{queue} \approx L_{service} \times \rho / (1-\rho)$；当 $\rho < 0.5$ 时，$L_{queue} < 1$ ms；当 $\rho > 0.8$ 时，$L_{queue}$ 急剧增加，可能超过 10-50 ms，这是 P99 延迟波动的主要来源。

## Corrected Claim

回源链路排队延迟 $L_{queue}$ 与链路利用率 $\rho$ 呈非线性关系：在 M/M/1 模型下，$L_{queue} \approx L_{service} \times \rho / (1-\rho)$；当 $\rho < 0.5$ 时，$L_{queue} < 1$ ms；当 $\rho > 0.8$ 时，$L_{queue}$ 急剧增加，可能超过 10-50 ms，这是 P99 延迟波动的主要来源。

## Evidence

先验知识/题面给定，逻辑校验通过：M/M/1排队论公式正确，非线性关系及阈值描述符合理论推导
