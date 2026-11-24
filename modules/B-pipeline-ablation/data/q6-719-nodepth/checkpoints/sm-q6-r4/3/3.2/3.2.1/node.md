# N93: 平均对象大小 s 的加权计算公式：s_avg = (N_img * s_img + N_vid * s_vid) / (N_img + N_vid)，其中 N_

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N22

## Claim

平均对象大小 s 的加权计算公式：s_avg = (N_img * s_img + N_vid * s_vid) / (N_img + N_vid)，其中 N_img 和 N_vid 分别为日均图片和视频请求次数，s_img 和 s_vid 分别为平均单张图片大小和平均单个短视频大小。

## Corrected Claim

平均对象大小 s 的加权计算公式：s_avg = (N_img * s_img + N_vid * s_vid) / (N_img + N_vid)，其中 N_img 和 N_vid 分别为日均图片和视频请求次数，s_img 和 s_vid 分别为平均单张图片大小和平均单个短视频大小。

## Evidence

父节点级核验未通过：不完备, 有冗余（子节点本质上是同一公式在不同参数取值下的计算示例，属于参数扫描而非独立的概念分解，存在高度冗余；且仅覆盖特定假设场景，未涵盖公式本身的定义边界、单位换算或极端值（如0/1占比）等关键方面，完备性不足。）
