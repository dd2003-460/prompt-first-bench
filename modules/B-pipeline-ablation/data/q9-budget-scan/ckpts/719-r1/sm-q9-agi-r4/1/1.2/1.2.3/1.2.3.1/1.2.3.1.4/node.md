# N393: FP16 KV Cache 在 L=128k 长度下的基线 Coherence Error Rate (CER_FP16_128k) 实测值：作为 L=128k

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N129

## Claim

FP16 KV Cache 在 L=128k 长度下的基线 Coherence Error Rate (CER_FP16_128k) 实测值：作为 L=128k 的对照组，用于计算该长度点的 ΔCER，预期值高于 L=64k 基线 [待核验]。

## Corrected Claim

FP16 KV Cache 在 L=128k 长度下的基线 Coherence Error Rate (CER_FP16_128k) 通常预期高于 L=64k 基线，具体实测值需参照特定实验报告。

## Evidence

[质询]该陈述包含具体的实验测量值（'实测值'）和特定条件下的性能指标（L=128k时的CER），属于经验事实。在没有提供具体论文、数据集或实验报告的情况下，无法验证该'实测值'的具体数值或其是否真的'高于L=64k基线'。此外，'预期值'与'实测值'混用，且缺乏具体的模型架构、硬件环境和评估协议，导致该事实无法从第一性原理推导，也无法通过现有信息确认其准确性。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源，且该事实非第一性原理可推导项）

## Search Query

FP16 KV cache baseline coherence error rate 128k context
