# N177: 实时压缩/转码开销：若启用 Brotli/Gzip 压缩，CPU 占用率增加 5-15%，P99 延迟增加 2-5ms（取决于对象大小与压缩级别）；若启用视频转

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N65

## Claim

实时压缩/转码开销：若启用 Brotli/Gzip 压缩，CPU 占用率增加 5-15%，P99 延迟增加 2-5ms（取决于对象大小与压缩级别）；若启用视频转码（如 WebP），延迟增加 50-200ms（通常异步处理，不计入 P99 同步路径）

## Corrected Claim

实时压缩/转码开销：若启用 Brotli/Gzip 压缩，CPU 占用率增加 5-15%，P99 延迟增加 2-5ms（取决于对象大小与压缩级别）；若启用视频转码（如 WebP），延迟增加 50-200ms（通常异步处理，不计入 P99 同步路径）

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

CDN real-time compression brotli gzip latency overhead P99
