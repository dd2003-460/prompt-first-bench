# N19: 推理吞吐量基准（Prefill & Decode）：收集各候选硬件在Qwen3-27B上的Prefill速度（tokens/s，输入长文本）和Decode速度（

- **status**: pending
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N3

## Claim

推理吞吐量基准（Prefill & Decode）：收集各候选硬件在Qwen3-27B上的Prefill速度（tokens/s，输入长文本）和Decode速度（tokens/s，生成阶段）实测数据或理论峰值估算。

## Corrected Claim

推理吞吐量基准（Prefill & Decode）：收集各候选硬件在Qwen3-27B上的Prefill速度（tokens/s，输入长文本）和Decode速度（tokens/s，生成阶段）实测数据或理论峰值估算。

## Evidence

父节点级核验未通过：不完备（子节点之间正交性良好（分别对应KV Cache约束、Decode理论估算、Prefill理论估算），无重复或矛盾。但存在两个主要问题：1. 完备性不足：父节点明确要求‘实测数据或理论峰值’，子节点仅提供了理论估算且标记为[待核验]，完全缺失了‘实测数据’这一关键组成部分；2. 内容偏差：子节点1侧重于内存占用计算，虽与Decode相关，但偏离了父节点‘吞吐量基准’的核心指标，属于前置条件而非直接指标。）

## Search Query

Qwen3-27B inference benchmark tokens/s prefill decode RTX 4090 A100 M2 Ultra

## Retrieval Sources

- {'url': 'https://blog.csdn.net/gitblog_00677/article/details/161712516&rut=ca34062c242707a38ec5e1fc0d0e8df91a7c21a8828a03630ce6efea7dc9e83d', 'type': 'ddg', 'title': 'Qwen3-0.6B大模型Benchmark方法论：prefill、decode、TTFT与内存占用全面解析'}
- {'url': 'https://blog.csdn.net/weixin_29070721/article/details/164383871&rut=a4c6fbeac7dd3fa1db7e129ff339a7554c04476efd0cf9b10909b4ad6b64f20f', 'type': 'ddg', 'title': '27B大模型本地部署实测：prefill、decode与前缀缓存性能拆解-CSDN博客'}
- {'url': 'https://wiki.hynx.com.cn/entries/qwen38-27b-local-inference-benchmark/&rut=4a3e756afe709f81919b73964725334a356388b6e0f22a16b76b746c2989ea0a', 'type': 'ddg', 'title': 'Qwen3.8-27B 本地推理怎么评估？显存、Context、TTFT、Prefill、Decode 与推理引擎'}
