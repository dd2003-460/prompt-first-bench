# N13: INT8 精度下 Qwen3-27B 质量损失量化：相对于 BF16 的困惑度增加和下游任务准确率下降，需区分 GPTQ/AWQ 等不同量化方法的影响 [待核验

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N2

## Claim

INT8 精度下 Qwen3-27B 质量损失量化：相对于 BF16 的困惑度增加和下游任务准确率下降，需区分 GPTQ/AWQ 等不同量化方法的影响 [待核验]

## Corrected Claim

INT8 精度下 Qwen3-27B 通常存在相对于 BF16 的质量损失，具体幅度取决于量化方法（如 GPTQ/AWQ）及校准数据，需通过任务级评测确定具体的困惑度增加和准确率下降数值。

## Evidence

[质询]陈述要求量化具体的困惑度增加和准确率下降数值，但参考来源主要讨论部署配置、显存占用及定性精度对比，缺乏针对 Qwen3-27B 在 INT8 下相对于 BF16 的具体量化损失数据（如具体的 PPL 增量或准确率百分比），且来源 [1] 甚至提到特定量化方法可能反超 BF16，与“质量损失”的普遍假设存在潜在冲突或需特定条件限定。 | 来源 [3] 确认了 INT8 与 BF16 在 Qwen3.8-27B 上的对比场景及精度关注点，但未提供具体的量化损失数值；来源 [2] 提供量化版本选择指南但侧重 GGUF 格式；整体逻辑自洽，但缺乏直接支持具体数值损失的证据，属于经验事实且缺具体数据支持。

## Search Query

Qwen3-27B INT8 GPTQ AWQ quantization quality impact

## Retrieval Sources

- {'url': 'https://blog.csdn.net/liangjinhu/article/details/164183862&rut=a6a509f8e74bff9b487998cd33b34a6a6d8d0784c2d7f4310f4e98041b75497e', 'type': 'ddg', 'title': 'Qwen3.8-27B GSQ-RCO 量化部署实测：9.3GB 跑出超 BF16 精度，消费级显卡落地 27B 多模态'}
- {'url': 'https://www.datalearner.com/blog/qwen3-8-27b-local-deployment-quantization-guide&rut=019b4b04a134444a435411c99925256a4f452d07ffd1b48e7fa68ba2d2a1e932', 'type': 'ddg', 'title': 'Qwen3.8-27B 本地部署完全指南：量化版本怎么选，效果差多少，速度有多快？ | DataLearnerAI'}
- {'url': 'https://blog.csdn.net/student_upupgpu/article/details/166246073&rut=aa9cd260f6083109421d10da626cf8e35468718ee875d8897eb1b2d94d06853e', 'type': 'ddg', 'title': 'A100 跑 Qwen3.8-27B，FP8 还是 INT8？显存、速度、精度与微调兼容性怎么选_qwen3.8 27b'}
