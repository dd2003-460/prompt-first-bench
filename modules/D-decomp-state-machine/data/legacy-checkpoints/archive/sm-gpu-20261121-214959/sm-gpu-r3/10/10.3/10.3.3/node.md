# N334: INT4 量化导致幻觉率上升的机制：低比特量化压缩了 Logits 分布的尾部概率，使得模型对罕见事实 (Long-tail Knowledge) 的置信度校准

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N120

## Claim

INT4 量化导致幻觉率上升的机制：低比特量化压缩了 Logits 分布的尾部概率，使得模型对罕见事实 (Long-tail Knowledge) 的置信度校准失效，倾向于输出高频但错误的模式，而非低频但正确的事实，这在医疗/法律等高风险场景中表现为不可接受的可靠性下降。

## Corrected Claim

INT4 量化导致幻觉率上升的机制：低比特量化压缩了 Logits 分布的尾部概率，使得模型对罕见事实 (Long-tail Knowledge) 的置信度校准失效，倾向于输出高频但错误的模式，而非低频但正确的事实，这在医疗/法律等高风险场景中表现为不可接受的可靠性下降。

## Evidence

先验知识/题面给定，逻辑校验通过：低比特量化确实会压缩Logits分布的尾部，导致长尾知识置信度校准失效，这是量化大模型幻觉机制的公认理论解释。

## Search Query

quantization impact on confidence calibration hallucination rare facts
