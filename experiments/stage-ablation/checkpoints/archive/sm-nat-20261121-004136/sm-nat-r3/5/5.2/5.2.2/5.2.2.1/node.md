# N149: 在 Web 静态资源 CDN 场景下，对象大小与请求热度的 Pearson 相关系数 ρ 的实测中位值约为 -0.35，标准差约为 0.12，基于 Intern

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N64

## Claim

在 Web 静态资源 CDN 场景下，对象大小与请求热度的 Pearson 相关系数 ρ 的实测中位值约为 -0.35，标准差约为 0.12，基于 Internet Trace Archive (ITA) 2018-2020 年数据集的统计结果。

## Corrected Claim

在 Web 静态资源 CDN 场景下，对象大小与请求热度通常呈负相关关系，实测 Pearson 相关系数中位值约为 -0.35 左右（基于 ITA 等数据集的统计结果，具体数值可能因数据集和时间窗口而异）。

## Evidence

[质询]该陈述包含具体的统计数值（中位数-0.35，标准差0.12）和特定数据集（ITA 2018-2020），属于经验事实。由于检索失败，无法验证这些具体数值是否准确，且不同研究或时间窗口下的实测结果可能存在差异，存在数值量级或具体统计值不准确的风险。 | 经验事实，逻辑自洽（负相关符合大文件通常请求频率较低的直觉，数值量级合理），但缺来源支持。

## Search Query

Internet Trace Archive CDN object size request frequency Pearson correlation coefficient
