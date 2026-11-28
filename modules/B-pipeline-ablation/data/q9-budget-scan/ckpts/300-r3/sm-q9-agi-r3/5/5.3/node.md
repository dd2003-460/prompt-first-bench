# N26: 死锁与无限循环检测的触发阈值：基于 vLLM 的 max-model-len 和超时机制，设定单步生成 Token 数超过 1024 且熵值低于 0.1 [待核

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N5

## Claim

死锁与无限循环检测的触发阈值：基于 vLLM 的 max-model-len 和超时机制，设定单步生成 Token 数超过 1024 且熵值低于 0.1 [待核验] 时判定为陷入局部循环，触发中断重试。量化该阈值在正常科研推理中的误报率（False Positive Rate），目标控制在 1% 以内

## Corrected Claim

基于 vLLM 的 max-model-len 和超时机制，可设定单步生成 Token 数与熵值作为死锁与无限循环的检测指标（具体阈值需根据实际负载调优，例如 Token > 1024 且熵 < 0.1），并监控误报率以优化中断重试策略。

## Evidence

[质询]该陈述包含具体的经验性阈值（Token数>1024，熵<0.1）及特定的误报率目标（<1%），这些并非vLLM内置的标准参数或通用物理/数学定律，而是特定应用场景下的工程调优经验值。参考来源仅讨论了max_model_len的基础配置和OOM问题，完全未涉及死锁检测的具体阈值设定或误报率量化数据，因此缺乏直接的外部证据支持其具体数值的合理性。 | 逻辑上利用Token长度和熵值检测循环是合理的启发式方法，但具体阈值（1024/0.1）及误报率目标属于经验事实，参考来源[1][2][3]仅涵盖vLLM基础参数配置，未提供相关支持证据。

## Search Query

LLM infinite loop detection entropy threshold vLLM timeout mechanism

## Retrieval Sources

- {'url': 'https://blog.csdn.net/weixin_28487725/article/details/156805403&rut=391a48415f67adead4e98f229bbc4cc58a13a9b29b1a441e05c92c7008a185d8', 'type': 'ddg', 'title': 'vLLM-v0.11.0参数详解：max_model_len配置实战 - CSDN博客'}
- {'url': 'https://blog.csdn.net/weixin_29062671/article/details/158328734&rut=1fc829652835dbe3dfed957d16c51d0be1a60b07f870512054780301e7a30104', 'type': 'ddg', 'title': 'Vllm推理引擎崩溃？3个参数调优让你的a800 80g稳定运行glm4-9b大模型-csdn博客'}
- {'url': 'https://ask.csdn.net/questions/9093530&rut=e26e54a460ca79748257e255f0c05ec6ae5f4fba279bba87650f100b656eb041', 'type': 'ddg', 'title': '部署vLLM时如何确定最优的max_model_len参数？ - CSDN问答'}
