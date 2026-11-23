# N154: 工作点A（轻量化图片）：$s_{img}=0.5 \text{ MB}$（WebP/AVIF压缩极致），$s_{vid}=5 \text{ MB}$（低码率短视

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N37

## Claim

工作点A（轻量化图片）：$s_{img}=0.5 \text{ MB}$（WebP/AVIF压缩极致），$s_{vid}=5 \text{ MB}$（低码率短视频），组合后 $s_{avg} = 0.7 \times 0.5 + 0.3 \times 5 = 1.85 \text{ MB}$，最小化带宽成本但可能牺牲画质指标。

## Corrected Claim

工作点A（轻量化图片）：$s_{img}=0.5 \text{ MB}$（WebP/AVIF压缩极致），$s_{vid}=5 \text{ MB}$（低码率短视频），组合后 $s_{avg} = 0.7 \times 0.5 + 0.3 \times 5 = 1.85 \text{ MB}$，最小化带宽成本但可能牺牲画质指标。

## Evidence

先验知识/题面给定，逻辑校验通过：加权平均计算 0.7*0.5 + 0.3*5 = 0.35 + 1.5 = 1.85 MB，数值准确，量级符合轻量化媒体场景常识。
