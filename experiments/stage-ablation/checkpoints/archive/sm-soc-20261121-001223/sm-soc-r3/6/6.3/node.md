# N72: 泊松分布参数 λ_t 的校准：在降价后 48 小时窗口内，新增咨询量 N_consult 服从 Poisson(λ_t)。根据题面 60% 无咨询（P(N=0)

- **status**: verified
- **level**: L3
- **source**: given
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N23

## Claim

泊松分布参数 λ_t 的校准：在降价后 48 小时窗口内，新增咨询量 N_consult 服从 Poisson(λ_t)。根据题面 60% 无咨询（P(N=0)=e^{-λ_t}=0.6），反推 λ_t = -ln(0.6) ≈ 0.51。需验证该 λ_t 是否显著低于基准期（未降价时）的 λ_base。

## Corrected Claim

泊松分布参数 λ_t 的校准：在降价后 48 小时窗口内，新增咨询量 N_consult 服从 Poisson(λ_t)。根据题面 60% 无咨询（P(N=0)=e^{-λ_t}=0.6），反推 λ_t = -ln(0.6) ≈ 0.51。需验证该 λ_t 是否显著低于基准期（未降价时）的 λ_base。

## Evidence

先验知识/题面给定，逻辑校验通过：由 P(N=0)=e^{-λ}=0.6 推导 λ=-ln(0.6)≈0.51 符合泊松分布定义及数学计算。
