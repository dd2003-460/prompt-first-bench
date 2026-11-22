# N46: FP8 精度质量损失阈值：Qwen3 系列模型原生支持 FP8 训练/推理，FP8 E4M3 格式下的输出质量损失接近 BF16 (MMLU 差异 < 0.5%

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

FP8 精度质量损失阈值：Qwen3 系列模型原生支持 FP8 训练/推理，FP8 E4M3 格式下的输出质量损失接近 BF16 (MMLU 差异 < 0.5%)，且推理速度提升约 1.5-2x，是 27B 模型在 24-48GB 显存卡上的首选精度，无需额外校准数据。

## Corrected Claim

Qwen3 系列模型支持 FP8 推理，相比 BF16 推理速度提升约 1.5-2 倍，且精度损失较小，是 27B 模型在 24-48GB 显存卡上的优选精度方案。

## Evidence

[质询]陈述中关于“MMLU 差异 < 0.5%”的具体数值缺乏来源支持，且“无需额外校准数据”这一绝对化表述在量化领域通常不成立（FP8 通常仍需校准或特定训练策略），属于经验事实且存在过度概括风险。 | 来源[1]直接支持了“推理速度提升约 1.5-2x”这一关键性能指标，但所有来源均未提供“MMLU 差异 < 0.5%”的具体基准测试数据，也未明确证实“无需校准”这一条件，故降级为定性表述。

## Retrieval Sources

- {'url': 'https://blog.csdn.net/gitblog_00942/article/details/151020764&rut=ac7b1d33ce4820a83760854de84ef08e28867defa947be00c2fd6c27a1bd9537', 'type': 'ddg', 'title': 'FP8量化革命Qwen3-1.7B-FP8：性能与精度平衡之道 - CSDN博客'}
- {'url': 'https://blog.csdn.net/gitblog_00016/article/details/156715038&rut=b0c48be16b9b19b40e3e89e577d853f6369b46d0439781167f18965906d26737', 'type': 'ddg', 'title': 'FP8量化技术深度解析：Qwen3-235B推理效率革命性突破-CSDN博客'}
- {'url': 'https://devpress.csdn.net/v1/article/detail/159254526&rut=0bda6daa974a691f2d6e7e475af0f68e6372865034f467725669a9bbd0c170d2', 'type': 'ddg', 'title': 'Qwen3-0.6B-FP8开源大模型：FP8量化后模型精度损失实测与补偿策略_不卡不卡-CSDN-OPC开发者社区'}
