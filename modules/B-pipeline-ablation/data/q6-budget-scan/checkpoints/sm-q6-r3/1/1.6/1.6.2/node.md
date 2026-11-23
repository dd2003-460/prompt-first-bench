# N48: 源站处理延迟 t_server = t_read + t_encode + t_response，其中 t_read 为存储读取时间（SSD典型 <1ms），t

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N11

## Claim

源站处理延迟 t_server = t_read + t_encode + t_response，其中 t_read 为存储读取时间（SSD典型 <1ms），t_encode 为视频转码或图片压缩时间（典型 10-100ms），t_response 为HTTP响应生成时间（<5ms）；该值反映源站服务器处理请求的耗时。

## Corrected Claim

源站处理延迟 t_server = t_read + t_encode + t_response，其中 t_read 为存储读取时间（SSD典型 <1ms），t_encode 为视频转码或图片压缩时间（典型 10-100ms），t_response 为HTTP响应生成时间（<5ms）；该值反映源站服务器处理请求的耗时。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

video transcoding latency ms
