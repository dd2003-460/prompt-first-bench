# N100: 本地27B模型在V100集群上的实际推理吞吐量（Tokens/sec），在TP=4、NVFP4量化、长上下文（>8k）场景下，需实测确定，预期瓶颈为KV Cac

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N33

## Claim

本地27B模型在V100集群上的实际推理吞吐量（Tokens/sec），在TP=4、NVFP4量化、长上下文（>8k）场景下，需实测确定，预期瓶颈为KV Cache显存限制导致的低Batch Size，吞吐量可能降至10-20 tokens/sec（[时效待核]）。

## Corrected Claim

本地27B模型在V100集群（TP=4）上，受限于长上下文（>8k）导致的KV Cache显存压力，Batch Size受限，实际推理吞吐量预计显著低于短上下文场景，具体数值需实测确定，参考单卡INT4量化基准约为28 tokens/sec，多卡长上下文场景下可能进一步降低。

## Evidence

[质询]来源[1]描述的是单卡V100（32GB）使用INT4量化的场景，而待核验事实涉及TP=4（多卡）、NVFP4量化及长上下文（>8k）导致KV Cache受限的低Batch Size场景。来源未覆盖多卡并行、特定量化格式（NVFP4）以及长上下文对吞吐量的具体影响，且来源标题提到的28 token/s与事实中预期的10-20 tokens/sec存在数值差异，无法直接支持该特定配置下的吞吐量预测。 | 逻辑上，长上下文导致KV Cache占用显存增加，从而限制Batch Size，进而降低吞吐量，这一因果链条符合推理引擎的基本原理；但来源[1]仅提供了单卡INT4量化的参考数据（28 token/s），未提供TP=4、NVFP4及长上下文场景的直接证据，属于间接相关且无法排除其他变量影响，故降级。

## Search Query

vLLM Qwen2.5-32B or 27B V100 TP4 inference throughput tokens per second long context benchmark

## Retrieval Sources

- {'url': 'https://developer.baidu.com/article/detail.html?id=6868754&rut=92c28f706501cdcc69cdd961ccaed65aff331573f609b89e39704ecc9f32d9a0', 'type': 'ddg', 'title': 'AI大模型本地部署实战：V100服务器27B参数模型28token/s推理优化全解析-百度开发者中心'}
