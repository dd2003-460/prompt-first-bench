# N21: 工作点 A（纯本地极限）：计算在 4×V100-16GB 配置下，Qwen3.8-27b NVFP4 量化模型的每秒 token 吞吐量 $Throughput

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N5

## Claim

工作点 A（纯本地极限）：计算在 4×V100-16GB 配置下，Qwen3.8-27b NVFP4 量化模型的每秒 token 吞吐量 $Throughput_{local}$（tokens/sec/GPU）及单请求延迟 $Latency_{local}$（ms/token）；基于 $Budget_{time}$ 约束，推导每日最大可处理研究任务数 $N_{tasks/day} = (H_{avail} \times 3600) / (T_{setup} + T_{inference} + T_{analysis})$，其中 $H_{avail}$ 为服务器可用小时数。

## Corrected Claim

工作点 A（纯本地极限）：计算在 4×V100-16GB 配置下，Qwen3.8-27b 采用低比特量化（如 Q4/Q8，来源未证实 NVFP4 可用性）模型的每秒 token 吞吐量及单请求延迟；基于时间预算约束，推导每日最大可处理研究任务数。

## Evidence

[质询]陈述中提到的 'NVFP4' 量化格式在提供的参考来源中未出现，来源主要讨论 Q4/Q8 或 FP8；此外，具体的吞吐量数值和延迟数据未在摘要中直接给出，属于需要具体实测数据的经验事实，仅凭逻辑公式无法验证具体性能指标。 | 来源 [1] 和 [2] 确认了 Qwen3.8-27B 在 V100 上的部署背景及量化需求（Q4/Q8），但未提供 NVFP4 的具体性能数据或吞吐量数值，属于经验事实且缺乏直接来源支持具体数值。

## Search Query

vLLM Qwen 27b V100 throughput tokens per second latency benchmark NVFP4

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/2072074634476909289&rut=e14e1b01b639a378ae8d7ef986fe88097d0f64a2bbbf119b0cbfae0037f1bd29', 'type': 'ddg', 'title': 'Qwen3.8-27B 实测：V100 上的部署要点与 Q4/Q8 全量基准'}
- {'url': 'https://zhuanlan.zhihu.com/p/2077790223518406650&rut=2b89b1ba33ff4199ff446f58300f7d439a224b24b2efdd0ed191c81a1d4f615d', 'type': 'ddg', 'title': '在 16G 显卡上部署 Qwen3.8 27B 最佳实践方案 - 知乎'}
