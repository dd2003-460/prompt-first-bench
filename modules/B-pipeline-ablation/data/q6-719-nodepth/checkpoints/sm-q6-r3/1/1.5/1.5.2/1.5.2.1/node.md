# N186: 图片处理延迟 T_processing_img：对于 JPEG/WebP 图片，源站通常不进行实时转码（已预生成多尺寸），主要延迟为存储 I/O 和 HTTP 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N54

## Claim

图片处理延迟 T_processing_img：对于 JPEG/WebP 图片，源站通常不进行实时转码（已预生成多尺寸），主要延迟为存储 I/O 和 HTTP 响应头生成；T_storage_io ≈ 100us (SSD随机读) + 网络栈处理 ≈ 1-5ms；因此 T_processing_img ≈ 2ms (P99)。

## Corrected Claim

图片处理延迟 T_processing_img：对于 JPEG/WebP 图片，源站通常不进行实时转码（已预生成多尺寸），主要延迟为存储 I/O 和 HTTP 响应头生成；T_storage_io ≈ 100us (SSD随机读) + 网络栈处理 ≈ 1-5ms；因此 T_processing_img ≈ 2ms (P99)。

## Evidence

先验知识/题面给定，逻辑校验通过
