# N397: 对象大小不均对命中率的影响修正项：若短视频对象大小是图片的 5 倍，且请求比例各占 50%，则按字节计算的命中率 $H_{byte} = H_{req} \ti

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N147

## Claim

对象大小不均对命中率的影响修正项：若短视频对象大小是图片的 5 倍，且请求比例各占 50%，则按字节计算的命中率 $H_{byte} = H_{req} \times \frac{\bar{s}_{hit}}{\bar{s}_{total}}$，需分别计算图片与视频的请求命中率并加权。

## Corrected Claim

对象大小不均对命中率的影响修正项：若短视频对象大小是图片的 5 倍，且请求比例各占 50%，则按字节计算的命中率 $H_{byte} = H_{req} \times \frac{\bar{s}_{hit}}{\bar{s}_{total}}$，需分别计算图片与视频的请求命中率并加权。

## Evidence

先验知识/题面给定，逻辑校验通过：字节命中率定义为命中字节数除以总请求字节数，数学上等价于请求命中率乘以命中对象平均大小与总对象平均大小之比，推导自洽。
