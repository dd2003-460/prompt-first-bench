# N164: 源站处理延迟 t_server 由对象处理复杂度决定：图片缩略图生成 t_img ≈ 5-10ms（CPU密集型），短视频转码/切片 t_video ≈ 20-

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N51

## Claim

源站处理延迟 t_server 由对象处理复杂度决定：图片缩略图生成 t_img ≈ 5-10ms（CPU密集型），短视频转码/切片 t_video ≈ 20-50ms（GPU/CPU密集型），静态文件读取 t_static ≈ 1-5ms（NVMe SSD IOPS > 100k）

## Corrected Claim

源站处理延迟 t_server 由对象处理复杂度决定：图片缩略图生成 t_img ≈ 5-10ms（CPU密集型），短视频转码/切片 t_video ≈ 20-50ms（GPU/CPU密集型），静态文件读取 t_static ≈ 1-5ms（NVMe SSD IOPS > 100k）

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

image processing latency ms server side vs video transcoding
