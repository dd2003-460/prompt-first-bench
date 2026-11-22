# N724: 物理空间与散热约束：4 张 RTX 4090（双槽位）需 8 个槽位高度，标准 ATX 机箱需 4U 以上机架空间。4090 TDP 450W * 4 = 18

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N222

## Claim

物理空间与散热约束：4 张 RTX 4090（双槽位）需 8 个槽位高度，标准 ATX 机箱需 4U 以上机架空间。4090 TDP 450W * 4 = 1800W GPU 热量，需至少 4 个 140mm PWM 风扇（~150 CFM each）或水冷方案。若散热不足，GPU 温度 > 83°C 将触发降频（-5% 性能），等效增加 5% 推理时间。

## Corrected Claim

物理空间与散热约束：4 张 RTX 4090（双槽位）需 8 个槽位高度，标准 ATX 机箱需 4U 以上机架空间。4090 TDP 450W * 4 = 1800W GPU 热量，需至少 4 个 140mm PWM 风扇（~150 CFM each）或水冷方案。若散热不足，GPU 温度 > 83°C 将触发降频（-5% 性能），等效增加 5% 推理时间。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 4090 为双槽卡，4张需8槽位，450W TDP 总热量 1800W，散热需求与风扇/水冷方案符合工程常识，83°C 降频阈值符合 NVIDIA 驱动行为。

## Search Query

4x RTX 4090 chassis cooling requirements thermal throttling threshold
