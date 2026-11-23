# N49: 图片与视频的请求比例 r_img : r_vid 通常约为 10:1 或 5:1（因图片加载频率远高于短视频）；假设 r_img=0.9, r_vid=0.1，

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N13

## Claim

图片与视频的请求比例 r_img : r_vid 通常约为 10:1 或 5:1（因图片加载频率远高于短视频）；假设 r_img=0.9, r_vid=0.1，则 s_avg = 0.9*500KB + 0.1*5MB = 950KB。

## Corrected Claim

图片与视频的请求比例 r_img : r_vid 通常约为 10:1 或 5:1（因图片加载频率远高于短视频）；假设 r_img=0.9, r_vid=0.1，则 s_avg = 0.9*500KB + 0.1*5MB = 950KB。

## Evidence

父节点级核验未通过：不完备, 有冗余（子节点本质上是同一参数（请求比例 r_img/r_vid）在不同取值下的计算实例，属于参数扫描而非独立维度的分解，因此存在冗余；同时，父节点的核心逻辑是“比例决定平均大小及成本”，子节点仅列举了两个极端/特定工况，未覆盖中间状态或一般性公式推导，且缺少对成本结构（如缓存vs带宽权衡）的独立维度分析，导致完备性不足。）

## Search Query

image vs video request ratio social media platform
