# N187: 短视频处理延迟 T_processing_vid：若源站提供实时转码或切片（HLS/DASH），T_encode 为主导项；H.264 1080p 实时转码耗时

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N54

## Claim

短视频处理延迟 T_processing_vid：若源站提供实时转码或切片（HLS/DASH），T_encode 为主导项；H.264 1080p 实时转码耗时约为视频时长的 1/2 到 1/5；对于 15s 短视频，单次转码耗时 3-7.5s，但 CDN 场景下通常缓存转码结果，仅首次请求触发；若未缓存，P99 T_processing_vid ≈ 500ms-2s（取决于硬件加速卡数量与并发度）。

## Corrected Claim

短视频处理延迟 T_processing_vid：若源站提供实时转码，T_encode 为主导项；H.264 1080p 实时转码耗时通常与视频时长成正比，具体数值取决于硬件加速能力；CDN 场景下通常缓存转码结果，仅首次请求触发高延迟，后续请求延迟极低。

## Evidence

[质询]陈述中关于H.264 1080p实时转码耗时为视频时长1/2到1/5（即3-7.5s）以及P99延迟500ms-2s的具体数值属于经验性工程参数，缺乏通用物理定律或第一性原理支持，且参考来源未提供具体延迟数据，仅提及功能存在。 | 逻辑自洽（转码耗时与视频时长正相关符合直觉），但参考来源[1][2]仅描述腾讯云/EdgeOne的视频即时处理功能，未提供具体延迟数值或转码速度比例，属于经验事实且缺来源直接支持。

## Search Query

real-time video transcoding latency H.264 1080p server side

## Retrieval Sources

- {'url': 'https://www.tencentcloud.com/document/product/1145/65803?lang=zh&rut=e4beb94190d0385595095a42b71cf8a7ec20b02b3b3a5c76572279566c9ad98f', 'type': 'ddg', 'title': '视频即时处理'}
- {'url': 'https://edgeone.ai/zh/document/65803&rut=817b117397169bc54840b4e9b478d47dbf1d2dcb5819a31fed92822241f2759a', 'type': 'ddg', 'title': '视频即时处理 - Tencent EdgeOne'}
- {'url': 'https://creatortribune.com/youtube-video-stuck-processing/&rut=a06ee1acaa7035bfb82c86091bfc2bacd9f86e69f77cded196531382c122c9eb', 'type': 'ddg', 'title': 'How To Fix a YouTube Video Stuck on Processing'}
