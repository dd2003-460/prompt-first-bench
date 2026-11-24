# N125: 短视频与图片对象的访问频率差异导致混合长尾分布：图片对象Zipf指数α_img≈1.0，短视频对象α_vid≈0.8，总请求分布为加权混合 P_total = 

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N36

## Claim

短视频与图片对象的访问频率差异导致混合长尾分布：图片对象Zipf指数α_img≈1.0，短视频对象α_vid≈0.8，总请求分布为加权混合 P_total = w_img × P_img + w_vid × P_vid，其中w_img和w_vid由用户上传比例决定。

## Corrected Claim

短视频与图片对象的访问频率差异导致混合长尾分布：图片对象Zipf指数α_img≈1.0，短视频对象α_vid≈0.8，总请求分布为加权混合 P_total = w_img × P_img + w_vid × P_vid，其中w_img和w_vid由用户上传比例决定。

## Evidence

父节点级核验未通过：有冗余（子节点1和子节点2本质上是对同一参数（上传体积比30:70）的拆分计算，存在明显冗余；此外，父节点提到的Zipf指数α具体数值未在子节点中作为独立参数或推导步骤体现，略显不完备。）
