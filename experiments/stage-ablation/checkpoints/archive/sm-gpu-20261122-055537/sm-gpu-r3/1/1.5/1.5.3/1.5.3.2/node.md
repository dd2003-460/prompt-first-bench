# N178: INT4 量化后的权重显存占用精确值：27 * 10^9 parameters * 0.5 bytes/param = 13.5 GB。加上 N126 计算的 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N52

## Claim

INT4 量化后的权重显存占用精确值：27 * 10^9 parameters * 0.5 bytes/param = 13.5 GB。加上 N126 计算的 Scale/Zero-point 开销 (0.85 GB) 和 Bias (~50 MB)，总占用为 14.4 GB。N52 声称的 14.5-15.0 GB 基本准确，但需明确这是 Group-128 量化下的结果，若 Group Size 不同（如 64 或 256），开销会相应变化（Group-64 开销翻倍至 ~1.7 GB，总占用 ~15.2 GB）。

## Corrected Claim

INT4 量化后的权重显存占用精确值：27 * 10^9 parameters * 0.5 bytes/param = 13.5 GB。加上 N126 计算的 Scale/Zero-point 开销 (0.85 GB) 和 Bias (~50 MB)，总占用为 14.4 GB。N52 声称的 14.5-15.0 GB 基本准确，但需明确这是 Group-128 量化下的结果，若 Group Size 不同（如 64 或 256），开销会相应变化（Group-64 开销翻倍至 ~1.7 GB，总占用 ~15.2 GB）。

## Evidence

先验知识/题面给定，逻辑校验通过：27B参数INT4量化基础占用13.5GB，Group-128量化下Scale/Zero-point开销约0.85GB，Bias约50MB，总和14.4GB与N52声称的14.5-15.0GB区间基本一致，且Group-64开销翻倍至1.7GB导致总占用15.2GB的推导符合量化原理。
