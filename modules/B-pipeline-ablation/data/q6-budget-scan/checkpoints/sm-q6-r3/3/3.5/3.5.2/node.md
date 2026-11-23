# N112: 转码处理成本C_processing_upload：基于GPU转码集群利用率，单GB视频转码成本≈¥1-3/GB（取决于分辨率和码率），图片处理（压缩/水印）成

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N30

## Claim

转码处理成本C_processing_upload：基于GPU转码集群利用率，单GB视频转码成本≈¥1-3/GB（取决于分辨率和码率），图片处理（压缩/水印）成本≈¥0.1-0.5/GB，加权后C_processing_upload ≈ 0.6 * 0.3 + 0.4 * 2.0 = ¥1.02/GB

## Corrected Claim

转码处理成本C_processing_upload：基于GPU转码集群利用率，单GB视频转码成本≈¥1-3/GB（取决于分辨率和码率），图片处理（压缩/水印）成本≈¥0.1-0.5/GB，加权后C_processing_upload ≈ 0.6 * 0.3 + 0.4 * 2.0 = ¥1.02/GB

## Evidence

父节点级核验未通过：不完备（子节点仅覆盖了视频转码成本的计算逻辑，完全缺失了父节点中明确提到的图片处理成本（C_image_processing）及其权重计算过程，导致无法复现父节点最终的加权结果（¥1.02/GB）。）
