# N50: Qwen3-27B在4-bit (W4/NVFP4) 量化下的质量损失阈值：在复杂数学推理（GSM8K/MATH）任务中，4-bit量化导致准确率从BF16的~

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

Qwen3-27B在4-bit (W4/NVFP4) 量化下的质量损失阈值：在复杂数学推理（GSM8K/MATH）任务中，4-bit量化导致准确率从BF16的~80%下降至~65%-70%（损失10-15%）；在长上下文检索（RAG）任务中，召回率下降约5-8%。结论：除非显存极度受限（<24GB），否则不推荐4-bit用于生产级推理，因其质量损失超出大多数应用场景的可接受阈值。

## Corrected Claim

Qwen3-27B在4-bit (NVFP4) 量化下，显存需求显著降低（约20-24GB），支持单卡部署。虽然官方测试显示其精度与FP8版本差距较小（±0.5以内），但在复杂推理任务中可能存在一定程度的质量损失，具体幅度需根据实际任务基准测试确定，通常建议在生产环境中权衡显存限制与精度需求。

## Evidence

[质询]具体数值（GSM8K/MATH下降10-15%，RAG召回率下降5-8%）缺乏来源直接支持，且来源[3]指出NVFP4与FP8精度差距在±0.5以内，暗示损失可能远小于10-15%；此外，来源主要讨论Qwen3.6/3.8，与Qwen3-27B存在版本差异。 | 来源[1][2][3]确认了4-bit量化（NVFP4）在27B模型上的部署可行性和显存优势，但均未提供GSM8K/MATH具体下降10-15%或RAG召回率下降5-8%的精确数据，属于经验事实且缺乏直接数值支持。

## Retrieval Sources

- {'url': 'https://blog.csdn.net/gitblog_00951/article/details/168656480&rut=71c6e1be65bbc23bfc7f503b60bfe1cc65244a06c54f645b59e12967ba2e801a', 'type': 'ddg', 'title': 'Qwen3.6-27B-NVFP4 vs NVIDIA NVFP4 vs FP8 vs BF16：精度基准全对比，4-bit量化真的掉分吗'}
- {'url': 'https://blog.csdn.net/gitblog_00251/article/details/155293565&rut=f2575b9ef73b602ebb0de12574b5cefdf66ddecb40734a9b727c899ac069b268', 'type': 'ddg', 'title': 'Qwen3.8-27B-NVFP4 vs 原版BF16：量化后速度、显存与效果全面对比-CSDN博客'}
- {'url': 'https://devpress.csdn.net/v1/article/detail/162604876&rut=d4d51b725b6fab545193998a82a0d82f3fdcfa0a286b430f9eb3b28624a2bcd6', 'type': 'ddg', 'title': 'Qwen3.6-27B-NVFP4 深度评测：英伟达官方量化，27B 长上下文本地部署新选择'}
