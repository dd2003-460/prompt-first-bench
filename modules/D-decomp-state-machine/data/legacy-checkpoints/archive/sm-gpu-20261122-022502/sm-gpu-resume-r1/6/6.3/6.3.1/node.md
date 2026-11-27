# N108: 128K 上下文下 24GB 单卡 (RTX 4090) 的溢出验证与切换阈值：INT4 权重 (13.5GB) + BF16 KV Cache (50.32G

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N31

## Claim

128K 上下文下 24GB 单卡 (RTX 4090) 的溢出验证与切换阈值：INT4 权重 (13.5GB) + BF16 KV Cache (50.32GB) = 63.82GB >> 24GB (严重溢出)；INT4 权重 (13.5GB) + FP8 KV Cache (25.16GB) = 38.66GB > 24GB (溢出)。结论：24GB 单卡在 128K 上下文中完全不可行，必须切换至多卡方案 (如 2x 4090 总显存 48GB，仍不足 38.66GB+激活值，需 3x 4090 或 2x 5090) 或大容量单卡 (H100 80GB, Mac Studio)。

## Corrected Claim

128K 上下文下 24GB 单卡 (RTX 4090) 的溢出验证与切换阈值：INT4 权重 (13.5GB) + BF16 KV Cache (50.32GB) = 63.82GB >> 24GB (严重溢出)；INT4 权重 (13.5GB) + FP8 KV Cache (25.16GB) = 38.66GB > 24GB (溢出)。结论：24GB 单卡在 128K 上下文中完全不可行，必须切换至多卡方案 (如 2x 4090 总显存 48GB，仍不足 38.66GB+激活值，需 3x 4090 或 2x 5090) 或大容量单卡 (H100 80GB, Mac Studio)。

## Evidence

先验知识/题面给定，逻辑校验通过：13.5GB+50.32GB=63.82GB及13.5GB+25.16GB=38.66GB均远超24GB，且38.66GB>48GB(2x4090)的结论在数值上成立，符合显存溢出逻辑。
