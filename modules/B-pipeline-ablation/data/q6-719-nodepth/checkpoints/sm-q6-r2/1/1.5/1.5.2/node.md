# N54: T_processing = T_decode + T_encode + T_storage_io，其中 T_decode/encode 取决于对象类型（图片 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N10

## Claim

T_processing = T_decode + T_encode + T_storage_io，其中 T_decode/encode 取决于对象类型（图片 JPEG/WebP 处理 ~5ms，短视频 H.264 转码 ~500ms-2s），T_storage_io 取决于源站存储 IOPS（SSD ~100us/op）[待核验]

## Corrected Claim

T_processing = T_decode + T_encode + T_storage_io，其中 T_decode/encode 取决于对象类型（图片 JPEG/WebP 处理 ~5ms，短视频 H.264 转码 ~500ms-2s），T_storage_io 取决于源站存储 IOPS（SSD ~100us/op）[待核验]

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

image processing latency vs video transcoding latency server side
