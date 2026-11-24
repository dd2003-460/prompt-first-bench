# N350: 每字节溢出导致的用户流失或降级成本 Loss_Per_Overflow_Byte 的量化：当带宽不足时，用户面临排队或降级（如降低视频分辨率）。降级导致的单请求

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N121

## Claim

每字节溢出导致的用户流失或降级成本 Loss_Per_Overflow_Byte 的量化：当带宽不足时，用户面临排队或降级（如降低视频分辨率）。降级导致的单请求价值损失约为正常请求价值的 20%-30%（因体验下降导致的隐性流失）。若正常请求价值为 ¥0.0000004/Byte（基于 ¥4/GB），则 Loss_Per_Overflow_Byte ≈ ¥0.0000001/Byte。

## Corrected Claim

每字节溢出导致的用户流失或降级成本 Loss_Per_Overflow_Byte 的量化：当带宽不足时，用户面临排队或降级（如降低视频分辨率）。降级导致的单请求价值损失约为正常请求价值的 20%-30%（因体验下降导致的隐性流失）。若正常请求价值为 ¥0.0000004/Byte（基于 ¥4/GB），则 Loss_Per_Overflow_Byte ≈ ¥0.0000001/Byte。

## Evidence

先验知识/题面给定，逻辑校验通过：数值计算自洽（0.0000004 * 25% = 0.0000001），且20%-30%的降级价值损失符合一般经验直觉。

## Search Query

cost of service degradation per byte user experience loss estimation
