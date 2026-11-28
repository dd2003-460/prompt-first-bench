# N72: Qwen3-27B 在 W4A8 量化下，MMLU 基准测试得分相对 BF16 下降幅度通常在 2-5% 之间，HumanEval 下降幅度可能在 5-10% 

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N14

## Claim

Qwen3-27B 在 W4A8 量化下，MMLU 基准测试得分相对 BF16 下降幅度通常在 2-5% 之间，HumanEval 下降幅度可能在 5-10% 之间 [待核验：4-bit 量化对代码生成任务影响较大]。

## Corrected Claim

Qwen3系列模型在4-bit量化下，MMLU得分通常保持较高水平（如84%+），HumanEval表现取决于具体量化算法和基线，部分优化版本（如OptiQ）可保持90%+的高分，下降幅度视具体实现而定，并非固定为5-10%。

## Evidence

[质询]模型名称不匹配（Qwen3-27B vs Qwen3.8-27B/Qwen3-30B-A3B）且量化方案不同（W4A8 vs GGUF/OptiQ-4bit），来源数据无法直接映射到特定声明的数值区间；此外，来源[3]显示4bit量化下HumanEval高达92.1%，若BF16基线接近满分，下降幅度可能远小于5-10%，甚至接近0，挑战了‘通常下降5-10%’的普遍性假设。 | 来源[2]和[3]涉及Qwen3系列模型的量化评测，但具体型号（30B-A3B, 3.8-27B）和量化方法（W4A8, OptiQ-4bit）与声明中的Qwen3-27B W4A8不完全一致，属于间接支持；逻辑上4bit量化对代码任务影响较大符合常识，但具体数值缺乏直接对应来源支持。

## Search Query

Qwen3-27B 4-bit quantization quality degradation MMLU HumanEval delta

## Retrieval Sources

- {'url': 'https://www.datalearner.com/blog/qwen3-8-27b-local-deployment-quantization-guide&rut=1fa99b1a298bb35659b089a8fb4cc56bec0cb2545060f406b39ee8a0274e36e1', 'type': 'ddg', 'title': 'Qwen3.8-27B 本地部署完全指南：量化版本怎么选，效果差多少，速度有多快？ | DataLearnerAI'}
- {'url': 'https://blog.csdn.net/gitblog_00696/article/details/168246507&rut=4a60aabd6fe7b1c4c1876aaf26daa04b2c0c7963a2aafc2af714d8c57c85afb8', 'type': 'ddg', 'title': '量化掉点多少？Qwen3-30B-A3B-quantized.w4a8 质量与性能实测（W4A8 vs W8A8 vs BF16）'}
- {'url': 'https://blog.csdn.net/gitblog_00194/article/details/171189400&rut=c075ba2cef96b5c74418b88f6a19d97ea5a2f7060eed2178e10c5e58a618233c', 'type': 'ddg', 'title': 'Qwen3.8-27B-pi-adapted-OptiQ-4bit基准测试报告解读：MMLU 84.1%与HumanEv'}
