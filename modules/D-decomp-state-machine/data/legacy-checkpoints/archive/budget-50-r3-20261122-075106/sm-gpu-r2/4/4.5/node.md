# N31: 在FP8精度下，NVIDIA H100 (80GB) 运行 Qwen3-27B 的稳态生成吞吐率（Token/s）约为 80-120，首Token延迟（TTFT

- **status**: pending
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

父节点级核验未通过：不完备（子节点在逻辑维度上正交（分别对应显存/并发、计算上限、内存带宽瓶颈），但存在关键事实错误和覆盖缺失。子节点1中KV Cache计算逻辑混乱且数值错误（27B模型FP8下权重应约为13-14GB而非27GB，KV Cache公式量纲错误）；子节点2中单序列理论吞吐推导错误（混淆了批量处理与单序列延迟，22000 Token/s是理论峰值算力下的批量上限，并非单序列稳态指标，且未正确解释为何实际值远低于此）；子节点3正确指出了内存带宽瓶颈，但父节点中的TTFT（首Token延迟）主要由Prefill阶段决定，子节点2和3均聚焦于Decode阶段（TPOT/稳态吞吐），未专门拆解TTFT的决定因素（如Prefill计算量、并行策略），导致对父节点中'TTFT 0.3-0.6s'这一关键指标的成因解释不完备。）

## Search Query

NVIDIA H100 80GB Qwen3-27B FP8 inference throughput tokens per second TTFT TPOT

## Retrieval Sources

- {'url': 'https://blog.csdn.net/weixin_44262492/article/details/160346989&rut=7bea0539c9ed79eda7b2f0a43b92a01d1bc88499a9db638dd5c06a1096b5fdd6', 'type': 'ddg', 'title': '【vLLM 部署 Qwen3-397B-A17B 技术解析】FP8 八卡 H100 推理服务全攻略_397b vllm部署在英伟达-CSDN博客'}
- {'url': 'https://devpress.csdn.net/v1/article/detail/163982375&rut=6ec67c90618847e2b35020e17bedef1686aca40df25dd3f62a1876e321b153df', 'type': 'ddg', 'title': '本地部署 Qwen3.8-27B-FP8 + DFlash2：96GB 总显存实测提速 2.89 倍（保姆级教程）'}
- {'url': 'https://blog.csdn.net/weixin_29056781/article/details/166022297&rut=7c73d43c2d312385e48aa0ad557ba2e8eff51baaeb38951c62af550fd88281bf', 'type': 'ddg', 'title': 'Qwen3.8-27B FP8量化部署实战：从显存计算到性能调优-CSDN博客'}
