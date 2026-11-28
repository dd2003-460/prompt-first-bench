# N283: 短序列高并发工作点（BS=8, L=4k）的实际可持续吞吐量 T_sustained：理论峰值 4500 tok/s 受 TP=4 的 AllReduce 通信

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N113

## Claim

短序列高并发工作点（BS=8, L=4k）的实际可持续吞吐量 T_sustained：理论峰值 4500 tok/s 受 TP=4 的 AllReduce 通信开销（约 10-15% 时间）及 vLLM 调度间隙影响，实际可达值约为 3500-4000 tok/s；需通过 1 小时持续负载压测确定 P50/P95 延迟下的稳态吞吐。

## Corrected Claim

短序列高并发工作点（BS=8, L=4k）的实际可持续吞吐量通常低于理论峰值，受TP=4的AllReduce通信开销及vLLM调度间隙影响，具体数值需根据特定硬件配置通过持续负载压测确定。

## Evidence

[质询]该陈述包含具体的经验性能指标（如4500 tok/s峰值、3500-4000 tok/s实际值、10-15%通信开销），这些数值高度依赖于具体的硬件型号（GPU类型、互联带宽）、vLLM版本及系统配置，无法从第一性原理推导，且参考来源完全无关，缺乏直接证据支持。 | 参考来源[1][2][3]均为生物信息学内容，与LLM推理性能无关，属「无可用外部证据」；该事实为经验性能数据，逻辑上自洽（实际吞吐低于理论峰值符合常识），但缺乏来源支持，依据经验事实排除条款降级。

## Search Query

vLLM Qwen3-27B batch 8 sequence 4k throughput benchmark V100 TP4

## Retrieval Sources

- {'url': 'https://blog.csdn.net/LogicNest/article/details/155440474&rut=7fcf39745eac4362c2d40e825934fc7f114c0fcf3b597e72a2536792cf063e6a', 'type': 'ddg', 'title': '揭秘生物信息学中的并行计算瓶颈：如何将序列比对速度提升10倍以上-csdn博客'}
- {'url': 'https://blog.csdn.net/LearnFlow/article/details/155440781&rut=24403d4b6876e662f3afd608cbc8e1d69ca4817073cd43d88ebfe0987d0096c4', 'type': 'ddg', 'title': '为什么你的blast任务总是超时？解析生物信息学作业调度中的并行优化盲区-csdn博客'}
- {'url': 'https://www.biocloudservice.com/server-calculator/articles/bioinformatics-config-cheatsheet.html&rut=dd7d405290e3de84b451e4e83b2bce4752d84efd97da7c1273836ed814cafc2e', 'type': 'ddg', 'title': '生信服务器配置速查表（2026 完整版） | 云生信'}
