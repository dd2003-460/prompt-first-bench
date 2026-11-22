# N182: AMD MI300X 的 HBM3 显存带宽标称值为 5300 GB/s，但实际有效带宽受内存控制器效率及 ROCm 驱动优化影响，通常在 85%-95% 之间

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N60

## Claim

AMD MI300X 的 HBM3 显存带宽标称值为 5300 GB/s，但实际有效带宽受内存控制器效率及 ROCm 驱动优化影响，通常在 85%-95% 之间，需根据具体驱动版本（如 ROCm 6.x）实测确定 [待核验]。

## Corrected Claim

AMD MI300X 的 HBM3 显存带宽标称值为 5300 GB/s，实际有效带宽受内存控制器效率及 ROCm 驱动优化影响，通常低于标称值，具体效率需根据驱动版本（如 ROCm 6.x）及测试场景实测确定。

## Evidence

[质询]85%-95% 的有效带宽效率区间属于经验性工程数据，缺乏通用理论推导支持，且具体数值高度依赖测试基准（如 STREAM vs 实际算子）和驱动版本，直接断言该固定区间可能过于绝对。 | source=knowledge，逻辑自洽（5300 GB/s 为 MI300X 官方标称值，效率受驱动影响符合工程常识），但具体效率区间为经验事实，无外部来源直接支持，依据经验事实排除条款降级。

## Search Query

AMD MI300X HBM3 effective bandwidth efficiency ROCm driver optimization
