# N141: 自建节点的排队延迟 $L_{queue}$ 遵循 M/M/c 模型，与到达率 $\lambda = R_{daily}/86400$ 和服务时间 $1/\mu$

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N34

## Claim

自建节点的排队延迟 $L_{queue}$ 遵循 M/M/c 模型，与到达率 $\lambda = R_{daily}/86400$ 和服务时间 $1/\mu$ 相关。当 $s_{avg}$ 从 1MB 增至 5MB，$\lambda$ 下降 80%，在服务器并发能力 $c$ 不变的情况下，利用率 $\rho = \lambda/c$ 显著降低，导致 $L_{queue}$ 非线性下降。

## Corrected Claim

自建节点的排队延迟 $L_{queue}$ 遵循 M/M/c 模型，与到达率 $\lambda = R_{daily}/86400$ 和服务时间 $1/\mu$ 相关。当 $s_{avg}$ 从 1MB 增至 5MB，$\lambda$ 下降 80%，在服务器并发能力 $c$ 不变的情况下，利用率 $\rho = \lambda/c$ 显著降低，导致 $L_{queue}$ 非线性下降。

## Evidence

先验知识/题面给定，逻辑校验通过：M/M/c 模型中利用率 ρ 降低确实会导致排队延迟非线性下降，且 s_avg 增大导致 λ 下降符合业务逻辑。
