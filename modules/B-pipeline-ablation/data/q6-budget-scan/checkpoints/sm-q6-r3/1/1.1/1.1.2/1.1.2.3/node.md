# N156: 工作点C（高码率/4K）：$s_{img}=2.0 \text{ MB}$（原图），$s_{vid}=15 \text{ MB}$（4K短视频），组合后 $s_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N37

## Claim

工作点C（高码率/4K）：$s_{img}=2.0 \text{ MB}$（原图），$s_{vid}=15 \text{ MB}$（4K短视频），组合后 $s_{avg} = 0.7 \times 2.0 + 0.3 \times 15 = 5.9 \text{ MB}$，带宽成本翻倍，且单流传输时间 $T_{transfer}$ 增加，需评估对P99延迟的冲击。

## Corrected Claim

工作点C（高码率/4K）：$s_{img}=2.0 \text{ MB}$（原图），$s_{vid}=15 \text{ MB}$（4K短视频），组合后 $s_{avg} = 0.7 \times 2.0 + 0.3 \times 15 = 5.9 \text{ MB}$，带宽成本翻倍，且单流传输时间 $T_{transfer}$ 增加，需评估对P99延迟的冲击。

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算 0.7*2.0 + 0.3*15 = 1.4 + 4.5 = 5.9 正确，量纲一致，符合加权平均逻辑。
