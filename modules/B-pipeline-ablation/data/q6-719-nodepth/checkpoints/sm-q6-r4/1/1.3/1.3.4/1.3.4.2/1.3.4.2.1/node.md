# N510: 短视频对象大小 s_vid 的 P99 分位数计算：P99_vid = exp(μ_vid + 1.2816 × σ_vid)，代入 μ_vid=2.30, σ

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N172

## Claim

短视频对象大小 s_vid 的 P99 分位数计算：P99_vid = exp(μ_vid + 1.2816 × σ_vid)，代入 μ_vid=2.30, σ_vid=0.8 得 exp(3.325) ≈ 27.8MB，需与父节点声称的 50MB 进行偏差核验（偏差源于正态分位数取值或分布假设差异）

## Corrected Claim

短视频对象大小 s_vid 的 P99 分位数计算：P99_vid = exp(μ_vid + 1.2816 × σ_vid)，代入 μ_vid=2.30, σ_vid=0.8 得 exp(3.325) ≈ 27.8MB，需与父节点声称的 50MB 进行偏差核验（偏差源于正态分位数取值或分布假设差异）

## Evidence

先验知识/题面给定，逻辑校验通过：P99分位数公式 exp(μ + 1.2816σ) 应用正确，数值计算 exp(2.30 + 1.2816*0.8) = exp(3.32528) ≈ 27.8 准确无误，且明确指出了与父节点50MB的差异源于分布假设或参数取值，逻辑自洽。
