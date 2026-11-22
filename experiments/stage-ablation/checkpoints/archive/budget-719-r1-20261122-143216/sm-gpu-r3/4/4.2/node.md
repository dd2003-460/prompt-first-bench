# N22: 模型量化基准数据缺口：Qwen3-27B在BF16/FP8/INT8/NVFP4/W4精度下的MMLU/GSM8K基准分数及参数量化误差分布（如KL散度<0.0

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N4, N5

## Claim

模型量化基准数据缺口：Qwen3-27B在BF16/FP8/INT8/NVFP4/W4精度下的MMLU/GSM8K基准分数及参数量化误差分布（如KL散度<0.05阈值），需确认是否存在官方或社区一手机测数据，若无则标记[待核验]并给出预估误差区间。

## Corrected Claim

Qwen3-27B在BF16/FP8/NVFP4等精度下存在性能与显存的权衡，FP8精度损失较小而NVFP4显存占用低但精度损失较大；具体MMLU/GSM8K分数及KL散度误差分布需查阅官方技术报告或社区一手机测数据，当前来源未提供具体数值。

## Evidence

[质询]陈述中提到的具体量化误差阈值（如KL散度<0.05）及特定基准分数（MMLU/GSM8K）属于经验事实，参考来源仅提供了定性描述（如'精度损失小/大'）和部署指南，未提供具体的数值基准或误差分布数据，无法直接验证该具体阈值的有效性。 | 来源[1][2][3]确认了Qwen3-27B存在BF16/FP8/NVFP4等量化版本及性能差异的定性对比，但均未提供MMLU/GSM8K具体分数或KL散度数值，属于经验事实缺来源直接支持。

## Search Query

Qwen3-27B quantization benchmark MMLU GSM8K BF16 FP8 INT8 NVFP4 W4 accuracy loss

## Retrieval Sources

- {'url': 'https://www.shengyayun.com/blog/tech-implementation-2026-08-16/&rut=470f989aac0cbbbc50a02e9a7edb469f2acff9af9df425613db20efa88036c80', 'type': 'ddg', 'title': '技术热点落地：Qwen3.8-27B 本地部署实战——FP8/GGUF/NVFP4 选型与消费级显卡避坑清单（2026-08-16）'}
- {'url': 'https://aishare.jizhiku.net/archives/52380&rut=5039db391448ca89fc9e31a91fe1db6f2c987fedc9054ae8edd6c7dfbe5b8319', 'type': 'ddg', 'title': 'Qwen3.8-27B 实测：BF16/FP8/NVFP4 精度对比与部署优化指南 - AI技能智慧站'}
- {'url': 'https://blog.csdn.net/weixin_29056781/article/details/166022297&rut=acf49add5f46f2eaea65895c9fafae22a87eef3a627f68bc88459aef389fbcbb', 'type': 'ddg', 'title': 'Qwen3.8-27B FP8量化部署实战：从显存计算到性能调优-CSDN博客'}
