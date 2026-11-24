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

父节点级核验未通过：有冗余（子节点在逻辑上是正交的（不同压缩策略/质量档位），且覆盖了从低到高带宽成本的关键区间，具备完备性。然而，三个子节点本质上是同一参数 s_img 在不同场景下的具体取值实例，而非相互独立的结构性分解。它们共享完全相同的计算公式（C_bw_img = s_img * 单价），仅数值不同。这种将‘单一变量的不同取值’拆解为‘并列子节点’的做法属于结构性冗余，更适合通过参数表或变量定义来表达，而非分解为独立的逻辑分支。）

## Search Query

average compressed image size 1080p webp jpeg
