# N207: 1×A100 80GB 运行 Qwen3-27B BF16 的实际推理吞吐量基准值，需区分 Batch Size 1 和 8，预期 40-50 tokens/s

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N84

## Claim

1×A100 80GB 运行 Qwen3-27B BF16 的实际推理吞吐量基准值，需区分 Batch Size 1 和 8，预期 40-50 tokens/s，作为 TCO 计算的分母。

## Corrected Claim

1×A100 80GB 运行 Qwen3-27B BF16 时，显存占用接近上限，Batch Size 1 的吞吐量通常在 10-20 tokens/s 左右；Batch Size 8 可能因显存不足无法运行或吞吐量显著低于 40-50 tokens/s。若需达到 40-50 tokens/s 的吞吐量，通常建议采用双 A100 配置或量化方案。

## Evidence

[质询]数值量级与硬件配置不匹配：来源[2]和[3]均显示27B模型在BF16下通常需要双A100（160GB显存）才能稳定部署并达到较高吞吐，单卡80GB显存极度紧张（仅权重约54GB，剩余显存不足以支撑Batch 8的KV Cache），且单卡推理吞吐量通常远低于双卡并行或大Batch场景下的40-50 tokens/s（单卡Batch 1通常仅10-20 tokens/s，Batch 8受限于显存可能无法运行或吞吐更低）。 | 来源[2][3]证实27B BF16模型在A100上部署，但均使用双卡配置，未提供单卡80GB的具体吞吐量数据；单卡显存限制使得Batch 8的可行性及40-50 tokens/s的吞吐量存疑，属于经验事实且缺乏直接来源支持。

## Search Query

A100 80GB Qwen3-27B BF16 inference throughput tokens per second benchmark vLLM

## Retrieval Sources

- {'url': 'https://blog.csdn.net/student_upupgpu/article/details/166246073&rut=aa9cd260f6083109421d10da626cf8e35468718ee875d8897eb1b2d94d06853e', 'type': 'ddg', 'title': 'A100 跑 Qwen3.8-27B，FP8 还是 INT8？显存、速度、精度与微调兼容性怎么选_qwen3.8 27b'}
- {'url': 'https://juejin.cn/post/7641794682348601363&rut=acb672af9e3ba0f897ee3998f6c80bb440188caff6061dbb1bc9cf2c2cd51c55', 'type': 'ddg', 'title': '双A100部署Qwen3.6-27B：两轮vLLM调优，128K吞吐提升20%的完整记录从64K初始部署到128K生产配 - 掘金'}
- {'url': 'https://blog.csdn.net/weixin_31075273/article/details/162159501&rut=f2b1b10551a106b3a0b7beddc5d3a5094c53db91c53ebbf40bb30528ddfdde4b', 'type': 'ddg', 'title': '双A100部署Qwen 3.6-27B：128K长上下文推理实战优化 - CSDN博客'}
