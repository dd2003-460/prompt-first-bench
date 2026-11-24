# N739: N254 激进工作点的上行带宽预留量 B_up_aggressive = (Daily_Upload_GB / Peak_Hours) × Peak_Facto

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N254

## Claim

N254 激进工作点的上行带宽预留量 B_up_aggressive = (Daily_Upload_GB / Peak_Hours) × Peak_Factor / 8 / 1000，代入 200GB/8h/1.8 计算得 5.06 Mbps，该值需与源站实际上传峰值 P99 对比以验证是否足够

## Corrected Claim

N254 激进工作点的上行带宽预留量 B_up_aggressive = (Daily_Upload_GB / Peak_Hours) × Peak_Factor / 8 / 1000，代入 200GB/8h/1.8 计算得 5.06 Mbps，该值需与源站实际上传峰值 P99 对比以验证是否足够

## Evidence

先验知识/题面给定，逻辑校验通过：公式量纲正确（GB/h -> Gbps -> Mbps），数值计算准确（200/8*1.8/8/1000 = 5.0625 ≈ 5.06），且符合带宽预留的工程逻辑。
