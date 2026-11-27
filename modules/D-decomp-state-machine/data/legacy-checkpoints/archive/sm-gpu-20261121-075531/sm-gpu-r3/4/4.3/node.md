# N21: Qwen3-27B 在 INT8 精度下的量化后困惑度及基准得分，计算相对于 BF16 的绝对值下降幅度，并区分权重量化（W8A16）与权值激活双量化（W8A8

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N4, N5

## Claim

Qwen3-27B 在 INT8 精度下的量化后困惑度及基准得分，计算相对于 BF16 的绝对值下降幅度，并区分权重量化（W8A16）与权值激活双量化（W8A8）的差异。

## Corrected Claim

Qwen3-27B 在 INT8 精度下（特别是 W8A8 模式）相比 BF16 会有轻微的困惑度上升（精度损失），具体数值取决于校准数据和任务，但通常 W8A8 的精度损失小于 W8A16 或更低比特量化。

## Evidence

[质询]参考来源中未提供具体的量化后困惑度（Perplexity）数值或相对于BF16的绝对下降幅度数据，仅定性描述了精度保持情况，无法验证具体的数值量级。 | 来源[1]和[3]确认了Qwen3.8-27B存在INT8量化版本及W8A8/W8A16等量化模式，并定性指出INT8 W8A8在A100上适配性好，但缺乏具体的困惑度数值支持，属于经验事实且缺具体数据支持。

## Search Query

Qwen3-27B INT8 W8A16 W8A8 quantization quality loss evaluation

## Retrieval Sources

- {'url': 'https://blog.csdn.net/student_upupgpu/article/details/166246073&rut=aa9cd260f6083109421d10da626cf8e35468718ee875d8897eb1b2d94d06853e', 'type': 'ddg', 'title': 'A100 跑 Qwen3.8-27B，FP8 还是 INT8？显存、速度、精度与微调兼容性怎么选_qwen3.8 27b'}
- {'url': 'https://blog.csdn.net/weixin_29038345/article/details/167519710&rut=8e36aeba880a5345f615cc5f8d2c40bdc2b432fc1954e2556cc04a1ee0736901', 'type': 'ddg', 'title': 'Qwen3.8-27B本地部署实战：量化档位、终端配置与推理优化全解析-CSDN博客'}
- {'url': 'https://www.datalearner.com/blog/qwen3-8-27b-local-deployment-quantization-guide&rut=019b4b04a134444a435411c99925256a4f452d07ffd1b48e7fa68ba2d2a1e932', 'type': 'ddg', 'title': 'Qwen3.8-27B 本地部署完全指南：量化版本怎么选，效果差多少，速度有多快？ | DataLearnerAI'}
