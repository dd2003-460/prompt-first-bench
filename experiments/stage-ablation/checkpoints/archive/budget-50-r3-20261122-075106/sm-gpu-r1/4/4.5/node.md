# N31: 在FP8精度下，NVIDIA H100 (80GB) 运行 Qwen3-27B 的稳态生成吞吐率（Token/s）约为 80-120，首Token延迟（TTFT

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N4

## Claim

在FP8精度下，NVIDIA H100 (80GB) 运行 Qwen3-27B 的稳态生成吞吐率（Token/s）约为 80-120，首Token延迟（TTFT）约为 0.3-0.6s，每Token生成时间（TPOT）约为 8-12ms

## Corrected Claim

在FP8精度下，NVIDIA H100 (80GB) 运行 Qwen3-27B（假设该规格存在且为单卡部署）的稳态生成吞吐率（Token/s）约为 80-120，首Token延迟（TTFT）约为 0.3-0.6s，每Token生成时间（TPOT）约为 8-12ms（注：具体数值需以实际基准测试为准，当前来源未提供直接证据）

## Evidence

[质询]参考来源中未包含针对 H100 80GB 单卡运行 Qwen3-27B FP8 的具体吞吐率（Token/s）、TTFT 或 TPOT 数值，无法通过外部证据直接验证具体数值区间；且来源 [2] 和 [3] 提及的模型版本为 'Qwen3.8-27B'（可能为笔误或非标准命名，通常应为 Qwen2.5-32B 或 Qwen3-32B 等，Qwen3 系列目前公开主要参数为 0.6B-235B，27B 并非标准发布尺寸，存在模型名称混淆风险），导致来源与事实节点中的模型规格匹配度存疑。 | 逻辑上，27B 参数 FP8 模型权重约 27GB，H100 80GB 显存足以容纳并留出 KV Cache，单卡推理吞吐 80-120 Token/s 及 TPOT 8-12ms 符合大模型单卡推理的一般性能量级（受限于显存带宽，H100 HBM3 带宽约 3.35TB/s，27GB 权重读取一次约 8ms，理论极限 TPOT 接近 8ms，实际因计算和通信开销略高，数值合理）。但参考来源 [1] 讨论 397B 多卡，[2][3] 讨论 27B 但缺乏具体性能指标数据且模型命名存疑，无直接数值支持。

## Search Query

NVIDIA H100 80GB Qwen3-27B FP8 inference throughput tokens per second TTFT TPOT

## Retrieval Sources

- {'url': 'https://blog.csdn.net/weixin_44262492/article/details/160346989&rut=7bea0539c9ed79eda7b2f0a43b92a01d1bc88499a9db638dd5c06a1096b5fdd6', 'type': 'ddg', 'title': '【vLLM 部署 Qwen3-397B-A17B 技术解析】FP8 八卡 H100 推理服务全攻略_397b vllm部署在英伟达-CSDN博客'}
- {'url': 'https://devpress.csdn.net/v1/article/detail/163982375&rut=6ec67c90618847e2b35020e17bedef1686aca40df25dd3f62a1876e321b153df', 'type': 'ddg', 'title': '本地部署 Qwen3.8-27B-FP8 + DFlash2：96GB 总显存实测提速 2.89 倍（保姆级教程）'}
- {'url': 'https://blog.csdn.net/weixin_29056781/article/details/166022297&rut=7c73d43c2d312385e48aa0ad557ba2e8eff51baaeb38951c62af550fd88281bf', 'type': 'ddg', 'title': 'Qwen3.8-27B FP8量化部署实战：从显存计算到性能调优-CSDN博客'}
