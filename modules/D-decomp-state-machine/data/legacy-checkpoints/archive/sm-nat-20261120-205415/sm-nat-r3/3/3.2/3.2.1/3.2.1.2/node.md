# N136: 工作点 A（高频率/小对象）：假设 LFU 偏好小对象（ρ=-0.3），平均大小 E[S|H≥H_th] ≈ 0.5MB，则 K_LFU ≈ 131,072 M

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N50

## Claim

工作点 A（高频率/小对象）：假设 LFU 偏好小对象（ρ=-0.3），平均大小 E[S|H≥H_th] ≈ 0.5MB，则 K_LFU ≈ 131,072 MB / 0.5 MB ≈ 262,144。此工作点代表 LFU 在负相关下的最优性能边界，对应最大潜在对象覆盖数。

## Corrected Claim

工作点 A（高频率/小对象）：假设 LFU 偏好小对象（ρ=-0.3），平均大小 E[S|H≥H_th] ≈ 0.5MB，则 K_LFU ≈ 131,072 MB / 0.5 MB ≈ 262,144。此工作点代表 LFU 在负相关下的最优性能边界，对应最大潜在对象覆盖数。

## Evidence

先验知识/题面给定，逻辑校验通过：131,072 / 0.5 = 262,144，计算无误，量级合理。
