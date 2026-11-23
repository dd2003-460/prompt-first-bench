# N7: 日均总请求量 $R_{daily}$ 需基于日均下载量 2TB 和平均对象大小 $s_{avg}$ 计算：$R_{daily} = 2 \times 10^6 

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N1

## Claim

日均总请求量 $R_{daily}$ 需基于日均下载量 2TB 和平均对象大小 $s_{avg}$ 计算：$R_{daily} = 2 \times 10^6 \text{ MB} / s_{avg}$ (单位：请求/天)，其中 $s_{avg}$ 需根据图片(约1MB)与短视频(约5-10MB)的混合比例加权确定。

## Corrected Claim

日均总请求量 $R_{daily}$ 需基于日均下载量 2TB 和平均对象大小 $s_{avg}$ 计算：$R_{daily} = 2 \times 10^6 \text{ MB} / s_{avg}$ (单位：请求/天)，其中 $s_{avg}$ 需根据图片(约1MB)与短视频(约5-10MB)的混合比例加权确定。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点逻辑清晰，分别定义了输入参数（占比、大小）、中间计算（加权平均）和最终结果（请求量），各节点职责单一且无重叠，完整覆盖了父节点中关于 $s_{avg}$ 确定及 $R_{daily}$ 计算的所有关键步骤。）

## Search Query

average file size image vs short video streaming distribution
