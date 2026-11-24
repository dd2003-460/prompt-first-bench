# N1247: 双格式（HEIC+JPEG）分发导致的存储冗余倍数 M_storage = (S_heic + S_jpeg) / S_heic，其中 S_heic 为 HEI

- **status**: verified
- **level**: L6
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N428, N429, N430

## Claim

双格式（HEIC+JPEG）分发导致的存储冗余倍数 M_storage = (S_heic + S_jpeg) / S_heic，其中 S_heic 为 HEIC 文件大小，S_jpeg 为对应 JPEG q=95 文件大小；基于典型图片压缩比，S_jpeg ≈ 2.5-3.0 * S_heic，故 M_storage ≈ 3.5-4.0

## Corrected Claim

双格式（HEIC+JPEG）分发导致的存储冗余倍数 M_storage = (S_heic + S_jpeg) / S_heic，其中 S_heic 为 HEIC 文件大小，S_jpeg 为对应 JPEG q=95 文件大小；基于典型图片压缩比，S_jpeg ≈ 2.5-3.0 * S_heic，故 M_storage ≈ 3.5-4.0

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

HEIC vs JPEG file size ratio compression efficiency 1080p
