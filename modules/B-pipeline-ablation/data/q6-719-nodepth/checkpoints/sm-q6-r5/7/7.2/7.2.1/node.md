# N351: 小对象主导工作点：s_avg=0.8MB（图片占比80%），适用于头像/缩略图密集场景，请求数激增但单请求带宽成本低。

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N117

## Claim

小对象主导工作点：s_avg=0.8MB（图片占比80%），适用于头像/缩略图密集场景，请求数激增但单请求带宽成本低。

## Corrected Claim

小对象主导工作点：s_avg=0.8MB（图片占比80%），适用于头像/缩略图密集场景，请求数激增但单请求带宽成本低。

## Evidence

先验知识/题面给定，逻辑校验通过：0.8MB平均对象大小符合图片主导场景特征，小对象高并发低单请求带宽的逻辑自洽。
