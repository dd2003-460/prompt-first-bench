# N141: 图片对象大小分布的具体形态：在社交媒体场景下，图片大小通常不服从正态分布，而是服从对数正态分布（Log-Normal），其均值（Mean）约为 300-500K

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N43

## Claim

图片对象大小分布的具体形态：在社交媒体场景下，图片大小通常不服从正态分布，而是服从对数正态分布（Log-Normal），其均值（Mean）约为 300-500KB，但中位数（Median）显著更低（约 100-200KB），标准差（Sigma）需通过实际业务日志拟合，通常 Sigma_log 约为 0.5-0.8（以 log10 为单位），这导致少量极大图片（如 4K 原图）显著占用缓存空间。

## Corrected Claim

图片对象大小分布的具体形态：在社交媒体场景下，图片大小通常不服从正态分布，而是服从对数正态分布（Log-Normal），其均值（Mean）约为 300-500KB，但中位数（Median）显著更低（约 100-200KB），标准差（Sigma）需通过实际业务日志拟合，通常 Sigma_log 约为 0.5-0.8（以 log10 为单位），这导致少量极大图片（如 4K 原图）显著占用缓存空间。

## Evidence

先验知识/题面给定，逻辑校验通过：图片大小服从对数正态分布符合长尾分布特征，均值大于中位数且Sigma_log在0.5-0.8范围内符合常见媒体文件分布规律，数值量级合理。

## Search Query

social media image file size distribution log-normal mean median
