# N48: 日均请求量 N_total = 日均下载量 / 加权平均对象大小；加权平均对象大小 s_avg = (N_img * s_img + N_vid * s_vid

- **status**: verified
- **level**: L3
- **source**: given
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N13

## Claim

日均请求量 N_total = 日均下载量 / 加权平均对象大小；加权平均对象大小 s_avg = (N_img * s_img + N_vid * s_vid) / N_total；需先确定图片与视频的请求比例 r_img : r_vid。

## Corrected Claim

日均请求量 N_total = 日均下载量 / 加权平均对象大小；加权平均对象大小 s_avg = (N_img * s_img + N_vid * s_vid) / N_total；需先确定图片与视频的请求比例 r_img : r_vid。

## Evidence

先验知识/题面给定，逻辑校验通过：加权平均大小公式及总请求量推导符合数学定义与物理直觉。

## Search Query

daily request count estimation CDN traffic object size
