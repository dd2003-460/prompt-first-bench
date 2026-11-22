# N168: 工作点 C（低波动-高遗忘）：λ=1.0, T_shift=10 天，σ_f=0.8，计算 f_stale = exp(-1.0*10) ≈ 0.0000454

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N58, N59, N60

## Claim

工作点 C（低波动-高遗忘）：λ=1.0, T_shift=10 天，σ_f=0.8，计算 f_stale = exp(-1.0*10) ≈ 0.0000454，此时 LFU 几乎无残留，但高 λ 导致频率计数器频繁重置，需量化重置开销对吞吐量的影响（如 CPU 占用率增加 ΔCPU%）。

## Corrected Claim

工作点 C（低波动-高遗忘）：λ=1.0, T_shift=10 天，σ_f=0.8，计算 f_stale = exp(-1.0*10) ≈ 0.0000454，此时 LFU 几乎无残留，但高 λ 导致频率计数器频繁重置，需量化重置开销对吞吐量的影响（如 CPU 占用率增加 ΔCPU%）。

## Evidence

先验知识/题面给定，逻辑校验通过：数学计算 exp(-10) ≈ 4.54e-5 正确，LFU 在高遗忘率下计数器重置导致开销增加的逻辑符合系统原理。
