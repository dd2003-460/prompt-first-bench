# N201: 工作点 C（偏远地区/高延迟）：用户位于三四线及以下或偏远省份，距离最近 PoP > 300km，RTT_access ≈ 80-150ms，链路跳数多且带宽受

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N78

## Claim

工作点 C（偏远地区/高延迟）：用户位于三四线及以下或偏远省份，距离最近 PoP > 300km，RTT_access ≈ 80-150ms，链路跳数多且带宽受限，传输延迟 T_network_pub ≈ 100-200ms，构成 P99 延迟的主要长尾来源

## Corrected Claim

工作点 C（偏远地区/高延迟）：用户位于三四线及以下或偏远省份，距离最近 PoP > 300km，RTT_access ≈ 80-150ms，链路跳数多且带宽受限，传输延迟 T_network_pub ≈ 100-200ms，构成 P99 延迟的主要长尾来源

## Evidence

先验知识/题面给定，逻辑校验通过：300km光纤传输延迟约1.5ms，加上路由跳数、设备处理及拥塞排队，80-150ms RTT及100-200ms单向传输延迟符合偏远地区高延迟网络特征，量级合理。
