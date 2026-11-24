# N95: 平均单张图片大小 s_img，基于典型 C 端图片压缩参数（JPEG/WebP，分辨率 1080x1080，质量 80%）估算，典型值约为 100-200 KB

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N22

## Claim

平均单张图片大小 s_img，基于典型 C 端图片压缩参数（JPEG/WebP，分辨率 1080x1080，质量 80%）估算，典型值约为 100-200 KB，取中值 150 KB = 0.000143 GB，[时效待核]。

## Corrected Claim

平均单张图片大小 s_img，基于典型 C 端图片压缩参数（JPEG/WebP，分辨率 1080x1080，质量 80%）估算，典型值约为 100-200 KB，取中值 150 KB = 0.000143 GB，[时效待核]。

## Evidence

父节点级核验未通过：有冗余（子节点本质上是同一参数 s_img 在不同压缩/质量工作点下的取值枚举，而非结构上独立的子维度。虽然覆盖了低、中、高三个典型档位，但属于‘参数变体’而非‘正交子概念’，存在结构性冗余。）

## Search Query

average compressed image size 1080p webp jpeg
