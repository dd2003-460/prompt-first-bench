# N37: 推荐方案的条件性约束1 - 任务类型：若任务为代码生成/数学推理（对精度敏感），推荐 BF16/FP8 精度下的单卡 A100 80GB 或双卡 RTX 409

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

推荐方案的条件性约束1 - 任务类型：若任务为代码生成/数学推理（对精度敏感），推荐 BF16/FP8 精度下的单卡 A100 80GB 或双卡 RTX 4090 (NVLink/PCIe)；若任务为通用对话/摘要（对精度容忍度高），推荐 W4/INT8 精度下的单卡 RTX 4090 或 AMD RX 7900 XTX 以最大化性价比。

## Corrected Claim

若任务为代码生成/数学推理（对精度敏感），通常推荐较高精度（如BF16/FP8）及具备足够显存的GPU（如A100 80GB或双卡RTX 4090）；若任务为通用对话/摘要（对精度容忍度高），可采用量化精度（如W4/INT8）及性价比更高的消费级GPU（如单卡RTX 4090或AMD RX 7900 XTX）。

## Evidence

[质询]参考来源均与硬件选型、精度量化及具体GPU型号无关，无法提供外部证据支持该经验性推荐方案；且该陈述属于具体的工程经验事实（特定硬件+精度组合），非第一性原理可推导。 | 逻辑自洽（精度敏感任务需更高精度/显存，通用任务可量化以省资源），但参考来源[1][2][3]均讨论提示词工程，与硬件选型主题无关，无可用外部证据支持具体硬件推荐。

## Retrieval Sources

- {'url': 'https://blog.csdn.net/AIRoses/article/details/163412907&rut=a381fbe5f5ccb34cdb73be150fe771ad849dbd39a8d94212c3c154f1a1a357c3', 'type': 'ddg', 'title': '约束型提示词：用限制条件框定AI输出边界_android ai 项目开发提示语 约束条件 模板-CSDN博客'}
- {'url': 'https://raybyte.cn/post/2026/8/30/d031d0d8&rut=efe03d477322d8bd924ec70342b6641ed2e94c7d38ca0c2b64f46d372127d3d4', 'type': 'ddg', 'title': '代码生成任务中提示词过于抽象只会产出冗余实现，利用类型签名与测试用例约束生成逻辑使其更精准。 | RayByte'}
- {'url': 'https://jishuzhan.net/article/2040782114177159169&rut=64b10012b5fbeacc398fd5b9f71658ad258c1af17e061c360920e8633575e911', 'type': 'ddg', 'title': '保姆级提示词工程学习总结（含实操示例+工具推荐） - 技术栈'}
