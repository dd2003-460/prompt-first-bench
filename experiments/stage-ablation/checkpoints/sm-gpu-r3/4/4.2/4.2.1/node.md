# N99: Qwen3-27B 在 32K 上下文下的 Prefill 阶段计算量（FLOPs）约为 2 * 27e9 * 32768 ≈ 1.77 TFLOPs，Pref

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N21

## Claim

Qwen3-27B 在 32K 上下文下的 Prefill 阶段计算量（FLOPs）约为 2 * 27e9 * 32768 ≈ 1.77 TFLOPs，Prefill 延迟 T_prefill = 1.77e12 / (GPU_FLOPS * MFU)，其中 MFU (Model FLOPs Utilization) 在主流推理引擎中通常为 30%-50%。

## Corrected Claim

Qwen3-27B 在 32K 上下文下的 Prefill 阶段计算量（FLOPs）约为 2 * 27e9 * 32768 ≈ 1.77 TFLOPs，Prefill 延迟 T_prefill = 1.77e12 / (GPU_FLOPS * MFU)，其中 MFU (Model FLOPs Utilization) 在主流推理引擎中通常为 30%-50%。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点逻辑清晰且正交：节点1修正了父节点中缺失Attention计算量的FLOPs公式错误；节点2提供了不同硬件下的MFU参数；节点3基于前两者进行具体的延迟推导。三者分别对应'计算量定义'、'硬件效率参数'、'最终结果推导'，无重复且覆盖了父节点隐含的延迟计算需求。）

## Search Query

Qwen3-27B prefill FLOPs calculation 32k context
