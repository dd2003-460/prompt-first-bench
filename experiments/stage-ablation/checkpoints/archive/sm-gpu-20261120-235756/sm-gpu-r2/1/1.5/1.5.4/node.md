# N50: INT8 vs FP8的性价比对比：INT8在缺乏FP8硬件加速的旧卡（如RTX 3090）上可能更快（因INT8 Tensor Core更成熟），但在新卡（R

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N11

## Claim

INT8 vs FP8的性价比对比：INT8在缺乏FP8硬件加速的旧卡（如RTX 3090）上可能更快（因INT8 Tensor Core更成熟），但在新卡（RTX 4090/5090）上FP8通常更优，需对比具体硬件的INT8/FP8吞吐差异。

## Corrected Claim

INT8与FP8的性价比取决于具体硬件架构与量化策略。在缺乏FP8硬件加速的旧卡上，INT8因Tensor Core成熟度可能更具优势；在新卡上，FP8通常因原生支持而表现良好，但根据来源[1]，在细粒度量化场景下INT8仍可能优于FP8，需结合具体硬件吞吐与精度需求综合评估。

## Evidence

[质询]来源[1]引用的论文结论指出在细粒度量化下INT8可能优于FP8，这与陈述中“新卡上FP8通常更优”的绝对化倾向存在潜在冲突；且来源[3]指出同等算力下能耗INT8略高，但未直接提供RTX 3090/4090/5090的具体吞吐对比数据，陈述中的具体硬件表现属于经验事实，缺乏直接来源支持。 | 逻辑自洽（硬件架构演进符合直觉），但来源[1]暗示INT8在特定条件下可能更优，来源[2][3]仅讨论硬件差异和能耗，未直接证实“新卡FP8通常更优”这一具体经验结论，属于经验事实缺直接来源支持。

## Search Query

INT8 vs FP8 inference speed RTX 3090 vs 4090 benchmark

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/1998468976825619938&rut=69219826e792411e92033db7cdeccd0ccb54256e339a2bc41bb09ee8ab6e63a2', 'type': 'ddg', 'title': 'INT8 vs FP8：低比特量化下谁更胜一筹？ - 知乎'}
- {'url': 'https://zhuanlan.zhihu.com/p/1910047780782707993&rut=40d2a91775683bdb677f11e5ece8156b4e53ebe675e28a5405699eef53230a90', 'type': 'ddg', 'title': 'Int8 与 Fp8 硬件支持差异 - 知乎专栏'}
- {'url': 'https://zhuanlan.zhihu.com/p/1951762437838737709&rut=8fb261c9e98feb19f9a04174f6f6970f092298a796effbfbb1441e90dde47e5f', 'type': 'ddg', 'title': 'Gpu 推理能耗（Int8、Fp8、Fp16）精炼版 - 知乎'}
