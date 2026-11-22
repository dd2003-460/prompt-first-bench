# N99: Qwen3-27B在INT8精度下的权重占用应为27GB（27B参数×1字节/参数），而非N12中声称的13.5GB；13.5GB是W4/NVFP4精度下的占用

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N12

## Claim

Qwen3-27B在INT8精度下的权重占用应为27GB（27B参数×1字节/参数），而非N12中声称的13.5GB；13.5GB是W4/NVFP4精度下的占用值，N12的计算存在精度混淆错误，需修正为27GB权重占用，剩余显存仅1.5GB用于KV Cache，32K上下文下KV Cache需求5.2GB导致显存溢出，该工作点不可行。

## Corrected Claim

Qwen3-27B在INT8精度下的权重占用应为27GB（27B参数×1字节/参数），而非N12中声称的13.5GB；13.5GB是W4/NVFP4精度下的占用值，N12的计算存在精度混淆错误，需修正为27GB权重占用，剩余显存仅1.5GB用于KV Cache，32K上下文下KV Cache需求5.2GB导致显存溢出，该工作点不可行。

## Evidence

先验知识/题面给定，逻辑校验通过：27B参数在INT8（1字节/参数）下权重占用确为27GB，13.5GB对应W4精度，计算逻辑自洽且符合硬件常识。
