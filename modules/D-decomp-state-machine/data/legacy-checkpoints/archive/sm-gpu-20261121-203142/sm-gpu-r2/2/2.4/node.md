# N14: NVFP4/W4精度下的质量损失评估：基于MMLU/GPQA基准测试，W4量化相比BF16的准确率下降通常在2.0-5.0%范围内 [待核验: 需查找Qwen3

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N2

## Claim

NVFP4/W4精度下的质量损失评估：基于MMLU/GPQA基准测试，W4量化相比BF16的准确率下降通常在2.0-5.0%范围内 [待核验: 需查找Qwen3-27B在NVFP4/W4下的具体基准测试数据]

## Corrected Claim

NVFP4/W4精度下的质量损失评估：基于现有公开基准测试（如DeepSeek-R1），NVFP4量化相比BF16在MMLU/GPQA等基准上的准确率下降通常控制在1%以内或统计不可区分；Qwen3-27B的具体数据需进一步核验。

## Evidence

[质询]参考来源显示NVFP4量化在MMLU/GPQA等基准上几乎无损（差异<1%或统计不可区分），与陈述中'2.0-5.0%下降'的量级存在显著偏差；且来源未覆盖Qwen3-27B具体数据，无法证实该特定模型在此精度下的损失范围。 | 来源[1]和[2]均表明NVFP4量化在MMLU/GPQA上精度损失极小（<1%或无显著差异），与陈述的2-5%范围不符，但逻辑上W4量化确实可能带来一定损失，故降级为定性表述。

## Search Query

Qwen3-27B NVFP4 W4 quantization MMLU GPQA benchmark accuracy drop

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/1944504541950248086&rut=869ea6519580eac34c7a6747ee1c49facef2ad98a05edbf6aa6d83776b758e44', 'type': 'ddg', 'title': 'Nvfp4量化技术深度解析：4位精度下实现2.3倍推理加速 - 知乎'}
- {'url': 'https://github.com/jiayiliu12/quantization_project/blob/main/mmlu_pro_nvfp4_vs_bf16.md&rut=cbae306adbc2e44f5759419f3908c1c49d721b683d519cc055cea28b92eab3db', 'type': 'ddg', 'title': 'quantization_project/mmlu_pro_nvfp4_vs_bf16.md at main - GitHub'}
