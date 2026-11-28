# N390: FP8 KV Cache 在 L=64k 长度下的 Coherence Error Rate (CER_FP8_64k) 实测值：定义为逻辑连贯性断裂事件数/总

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N129

## Claim

FP8 KV Cache 在 L=64k 长度下的 Coherence Error Rate (CER_FP8_64k) 实测值：定义为逻辑连贯性断裂事件数/总生成Token数，需通过 vLLM 日志解析获取，预期值范围 [0.005, 0.02] [待核验]。

## Corrected Claim

FP8 KV Cache 在 L=64k 长度下的 Coherence Error Rate (CER_FP8_64k) 定义为逻辑连贯性断裂事件数/总生成Token数，需通过 vLLM 日志解析获取，具体数值范围需根据实际实验数据确定。

## Evidence

[质询]该陈述包含具体的经验性数值范围 [0.005, 0.02] 和特定的测量方法（vLLM 日志解析），属于经验事实。由于缺乏任何外部来源支持，且 FP8 KV Cache 在长上下文下的具体连贯性错误率并非第一性原理可推导的数学或物理常数，而是依赖于具体模型、数据集和实现细节的经验观测值，因此无法验证其准确性。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源）。

## Search Query

vLLM FP8 KV cache coherence error rate benchmark 64k context
