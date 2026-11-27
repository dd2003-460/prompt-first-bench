# N112: 参数 x_max 的物理意义与典型取值：在 CDN 场景中，x_max 受限于单对象最大下载限制（通常 100MB-1GB）或 CDN 厂商的特定配置；x_ma

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N34, N35, N36

## Claim

参数 x_max 的物理意义与典型取值：在 CDN 场景中，x_max 受限于单对象最大下载限制（通常 100MB-1GB）或 CDN 厂商的特定配置；x_max 的选取直接决定了长尾大对象对 E[S] 的贡献比例，因为 Pareto 分布重尾特性使得 E[S] 对 x_max 高度敏感。

## Corrected Claim

参数 x_max 的物理意义与典型取值：在 CDN 场景中，x_max 受限于单对象最大下载限制（通常 100MB-1GB）或 CDN 厂商的特定配置；x_max 的选取直接决定了长尾大对象对 E[S] 的贡献比例，因为 Pareto 分布重尾特性使得 E[S] 对 x_max 高度敏感。

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布的期望值确实随截断上限x_max线性增长，且CDN单对象大小限制通常在百MB至GB量级，符合工程常识。

## Search Query

CDN maximum object size limit Pareto distribution tail sensitivity
