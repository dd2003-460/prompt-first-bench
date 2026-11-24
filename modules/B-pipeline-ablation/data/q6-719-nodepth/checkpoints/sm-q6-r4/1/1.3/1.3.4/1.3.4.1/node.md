# N171: 图片对象大小 s_img 的对数正态分布参数：均值 μ_img = ln(2MB) ≈ 0.69，标准差 σ_img = 0.5，导致 P99 图片大小约为 5

- **status**: pending
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N49

## Claim

图片对象大小 s_img 的对数正态分布参数：均值 μ_img = ln(2MB) ≈ 0.69，标准差 σ_img = 0.5，导致 P99 图片大小约为 5.5MB，用于计算回源带宽分布

## Corrected Claim

图片对象大小 s_img 的对数正态分布参数：均值 μ_img = ln(2MB) ≈ 0.69，标准差 σ_img = 0.5，导致 P99 图片大小约为 5.5MB，用于计算回源带宽分布

## Evidence

父节点级核验未通过：不完备（子节点之间正交，分别处理图片和短视频两种不同对象类型。但父节点明确限定为'图片对象大小 s_img'，而子节点2引入了'短视频'这一超出父节点范围的新对象类型，导致完备性缺失（未覆盖父节点所有关键方面，反而引入了无关内容）。）

## Search Query

image file size log-normal distribution parameters social media
