# N286: 压缩算法对传输带宽降低的精确量化：ΔCompression = 1 - (compressed_size / original_size)，对于JPEG图片，B

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N92

## Claim

压缩算法对传输带宽降低的精确量化：ΔCompression = 1 - (compressed_size / original_size)，对于JPEG图片，Brotli压缩比约 1.1-1.3x（即节省 9-23%），对于H.264/H.265视频，压缩比约 1.0-1.05x（节省 0-5%）；加权平均 ΔCompression = 0.7×0.15 + 0.3×0.025 = 11.25%，而非题面所述的30-50%，原假设混淆了源编码压缩率与传输层压缩率。

## Corrected Claim

压缩算法对传输带宽降低的量化：ΔCompression = 1 - (compressed_size / original_size)。对于已高度压缩的 JPEG 图片，Brotli 等通用压缩算法的额外压缩比通常接近 1.0x（节省 <5%）；对于 H.264/H.265 视频，传输层压缩比也接近 1.0x。因此，加权平均 ΔCompression 通常远低于 11.25%，原假设中 30-50% 的带宽降低确实混淆了源编码与传输层压缩，但修正后的具体数值应更低。

## Evidence

[质询]数值量级与工程常识存在偏差：Brotli 对 JPEG 的压缩比通常极低（接近 1.0x，因为 JPEG 已是高熵数据），1.1-1.3x 的压缩比（节省 9-23%）过于乐观，通常仅在特定小文件或元数据优化下才可能达到；H.264/H.265 视频在传输层（如 HTTP/2+）的额外压缩空间也极小，0-5% 的估计虽保守但结合 JPEG 的高估，导致加权平均值 11.25% 可能偏高。 | 先验知识/题面给定，逻辑校验通过（公式定义正确，加权计算无误），但具体压缩比数值属于经验事实，缺乏来源支持且与典型工程经验（JPEG 压缩比接近 1.0x）存在潜在偏差，故降级。
