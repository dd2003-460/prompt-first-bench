# N79: Qwen3-27B FP8 量化在 MMLU 基准测试上的准确率与 BF16 基线的具体差值，需引用 Qwen 官方技术报告或 HuggingFace 社区评测

- **status**: pending
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N27

## Claim

Qwen3-27B FP8 量化在 MMLU 基准测试上的准确率与 BF16 基线的具体差值，需引用 Qwen 官方技术报告或 HuggingFace 社区评测数据，确认是否小于 0.5%

## Corrected Claim

Qwen3-27B（或Qwen3.8-27B）FP8量化在MMLU基准测试上的准确率与BF16基线基本持平，甚至略有提升，具体差值极小（来源未提供精确百分比，但定性描述为'完全打平'）。

## Evidence

[质询]来源[1]提到的模型版本为'Qwen3.8 27B'，而待核验事实指定为'Qwen3-27B'，存在版本标识不一致的风险；此外，来源仅给出'打平'和'MMLU涨4分'的定性/相对描述，未提供具体的绝对准确率数值或明确的差值百分比（如<0.5%），无法直接证实'差值小于0.5%'这一具体量化结论。 | 来源[1]间接支持FP8量化与BF16性能高度一致（'完全打平'、'MMLU还涨4分'），逻辑上支持差值极小甚至为负（即FP8更优），但缺乏具体数值证据直接证实'差值<0.5%'这一精确阈值，且模型版本号存在细微差异（Qwen3.8 vs Qwen3），故降级为定性表述。

## Search Query

Qwen3-27B FP8 quantization MMLU accuracy loss vs BF16

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/2090789049246266005&rut=487180e00b160a6ddc0ace847a28aad7ead071c4b7bd28e88dbb3ab86d610a60', 'type': 'ddg', 'title': 'Qwen3.8 27B 后训练完结篇，GPQA，MMLU和LCB都过90且大幅降低原版思考量的27B已发布'}
