# N244: A/B测试中成交周期 $T_{sale}$ 的分布假设：假设 $T_{sale}$ 服从对数正态分布 $\ln(T_{sale}) \sim N(\mu, \s

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N80

## Claim

A/B测试中成交周期 $T_{sale}$ 的分布假设：假设 $T_{sale}$ 服从对数正态分布 $\ln(T_{sale}) \sim N(\mu, \sigma^2)$，需估算 $\sigma$ 的值以验证样本量 $n \geq 384$ 的适用性。若 $\sigma > 1.5$，则需增加样本量至 $n \geq 500$。

## Corrected Claim

A/B测试中成交周期 $T_{sale}$ 的分布假设：假设 $T_{sale}$ 服从对数正态分布 $\ln(T_{sale}) \sim N(\mu, \sigma^2)$，需估算 $\sigma$ 的值以验证样本量 $n \geq 384$ 的适用性。若 $\sigma > 1.5$，则需增加样本量至 $n \geq 500$。

## Evidence

先验知识/题面给定，逻辑校验通过
