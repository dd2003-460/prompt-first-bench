# N38: 多卡显存分片策略：2x RTX 3090 (48GB Total) 在 BF16 下仍不足 (需 60GB)，需使用 FP8 (27B * 1 byte = 2

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

多卡显存分片策略：2x RTX 3090 (48GB Total) 在 BF16 下仍不足 (需 60GB)，需使用 FP8 (27B * 1 byte = 27GB) 或 INT8 (27GB) 量化，此时总显存占用约 27GB + KV + Overhead ≈ 32GB，可在 2x 3090 (48GB) 上运行，但需启用 Tensor Parallelism，通信开销增加约 10-15%。

## Corrected Claim

多卡显存分片策略：2x RTX 3090 (48GB Total) 在 BF16 下不足（27B模型BF16权重约54GB），需使用 FP8 或 INT8 量化（权重约27GB），此时总显存占用约27GB + KV + Overhead，可在 2x 3090 (48GB) 上运行，需启用 Tensor Parallelism，通信开销增加。

## Evidence

[质询]来源主要覆盖14B模型（BF16约28GB），未直接提供27B模型在BF16下需60GB及FP8/INT8量化后总显存约32GB的具体数据支持，且27B模型BF16权重约54GB，加上KV Cache和Overhead确实可能超过48GB，但具体数值（如32GB）缺乏直接来源佐证。 | 逻辑自洽：27B参数BF16权重约54GB，超过48GB总显存，需量化；FP8/INT8权重约27GB，加上KV Cache和Overhead后约32GB，可在48GB上运行。但来源[1][2][3]主要讨论14B模型，未直接支持27B模型的具体显存占用数值，属于间接支持。

## Retrieval Sources

- {'url': 'https://blog.csdn.net/weixin_29051811/article/details/168703146&rut=a97139b7b8c5cf6dc4fed523d647a9bd9706b5c5e30f9966000cf16b25852e41', 'type': 'ddg', 'title': '双卡RTX 3090部署Qwen2.5-14B全量BF16：vLLM张量并行实战与显存调优-CSDN博客'}
- {'url': 'https://blog.csdn.net/weixin_29046035/article/details/168703289&rut=2d234fa693ff6f0f36bb094a4cd5b8eccc9d1c315e54e739b4c0870ef5404efa', 'type': 'ddg', 'title': '双卡3090部署Qwen2.5-14B BF16全量推理：vLLM张量并行与显存调优实战-CSDN博客'}
- {'url': 'https://juejin.cn/post/7615073403721105427&rut=294fb583c904c58230945f5bc01623c6ad286992f0e57a48ca1388848d5f5c7f', 'type': 'ddg', 'title': '双RTX3090多卡推理深度解析# 双 RTX 3090 多卡推理深度解析：从 Tensor Parallelism 到 - 掘金'}
