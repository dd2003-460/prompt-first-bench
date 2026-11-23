# N376: M/M/c 模型中排队延迟 $L_{queue}$ 的解析公式（Pollaczek-Khinchine 近似或 Erlang C 公式）：$L_{queue} 

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N141

## Claim

M/M/c 模型中排队延迟 $L_{queue}$ 的解析公式（Pollaczek-Khinchine 近似或 Erlang C 公式）：$L_{queue} = \frac{P_{wait}}{\mu(1-\rho)}$，其中 $P_{wait}$ 为等待概率；当 $\rho < 0.1$ 时，$L_{queue} < 1\text{ms}$，可忽略不计；当 $\rho > 0.9$ 时，$L_{queue}$ 呈指数级增长，需重新评估服务器并发数 $c$。

## Corrected Claim

M/M/c 模型中，排队延迟 $L_{queue}$ 随利用率 $\rho$ 增加而显著增长。在低负载（如 $\rho < 0.1$）且服务率足够高的情况下，延迟通常可忽略；在高负载（如 $\rho > 0.9$）时，延迟呈非线性（近似指数）增长，需重新评估服务器并发数 $c$。具体数值（如 1ms）取决于服务率 $\mu$ 和到达率 $\lambda$ 的具体量级。

## Evidence

[质询]公式 $L_{queue} = \frac{P_{wait}}{\mu(1-\rho)}$ 并非 M/M/c 模型中排队延迟的标准解析公式（标准公式为 $L_q = \frac{P_{wait}}{\mu(1-\rho)}$ 仅在特定近似或特定定义下成立，通常 Erlang C 公式给出的等待时间期望为 $W_q = \frac{P_{wait}}{c\mu - \lambda}$ 或类似形式，且 $P_{wait}$ 本身随 $\rho$ 非线性变化，直接断言 $\rho < 0.1$ 时 $L_{queue} < 1\text{ms}$ 缺乏对服务率 $\mu$ 和到达率 $\lambda$ 具体量级的约束，属于经验性断言而非普适数学结论。 | 先验知识/题面给定，逻辑校验通过。虽然公式形式在标准排队论中需结合具体参数（如 $\mu$ 的单位）才能得出时间量级，但作为工程经验法则（knowledge 节点），其逻辑自洽性成立：低负载下延迟确实极低，高负载下延迟确实急剧上升。由于缺乏外部来源直接支持该特定公式形式及具体阈值（1ms），且涉及具体数值阈值，依据经验事实排除条款（若视为 search）或保守原则（若视为 knowledge 但公式非标准普适形式），降级为 degraded 以提示公式需结合具体参数验证。
