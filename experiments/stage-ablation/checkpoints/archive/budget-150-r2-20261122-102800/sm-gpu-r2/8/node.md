# N49: Qwen3-27B在INT8量化下的具体质量损失基准：在MMLU基准测试中，BF16得分约为85.2%，INT8 (GPTQ/AWQ) 得分约为83.5%-84

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

Qwen3-27B在INT8量化下的具体质量损失基准：在MMLU基准测试中，BF16得分约为85.2%，INT8 (GPTQ/AWQ) 得分约为83.5%-84.8%（下降1.4-1.7%）；在HumanEval代码生成基准中，BF16 Pass@1约为72%，INT8约为68%-70%（下降2-4%）。判定标准：若任务为通用对话，<2%损失可接受；若为复杂推理/代码，>3%损失通常不可接受。

## Corrected Claim

Qwen3-27B在INT8量化下通常会有轻微的质量损失，具体数值因量化方法（GPTQ/AWQ）和基准测试而异，一般认为在MMLU等通用基准上损失在1-2%左右，在代码生成等复杂任务上损失可能稍大，但具体分数需以官方或权威第三方实测为准。

## Evidence

[质询]参考来源[1]讨论的是'Qwen3.8-27B'（版本号与N49中的Qwen3-27B不符，且Qwen3.8并非已知官方发布版本，疑似笔误或混淆），且其结论是不同量化路径间差异极小（0.70%），并未提供N49中声称的具体基准分数（如MMLU 85.2% vs 83.5%）或HumanEval的具体下降幅度，无法直接支持N49中的具体数值。 | 逻辑上INT8量化导致1-4%的性能损失符合一般大模型量化经验，但参考来源[1]主题相关（Qwen系列量化对比）却未提供N49中的具体基准数据，且模型版本号存在不一致（Qwen3.8 vs Qwen3），属于间接支持且存在细节矛盾，故降级。

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/2073832437491287186&rut=b4516df8992fdf7a3c7e8f94308cbb87f96dc4ab542bf2ddc1a5f6aa5bec2829', 'type': 'ddg', 'title': 'qwen3.8-27b量化模型实测对比情况 - 知乎'}
