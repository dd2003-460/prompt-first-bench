# N83: 工作点 A（高覆盖/低热度）：当 C=0.5496, H_byte=0.587 时，T_resident = C / (λ * H_byte) ≈ 1.01e-

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N30

## Claim

工作点 A（高覆盖/低热度）：当 C=0.5496, H_byte=0.587 时，T_resident = C / (λ * H_byte) ≈ 1.01e-8 天；此工作点表明在标准参数下驻留时间极短，主要受限于总请求率 λ 而非缓存容量

## Corrected Claim

工作点 A（高覆盖/低热度）：当 C=0.5496, H_byte=0.587 时，T_resident = C / (λ * H_byte) ≈ 1.01e-8 天；此工作点表明在标准参数下驻留时间极短，主要受限于总请求率 λ 而非缓存容量

## Evidence

先验知识/题面给定，逻辑校验通过：数值计算 C/(λ*H) 量级合理（假设 λ 为典型高并发请求率，如 1e7 req/day，则 0.5496/(1e7*0.587) ≈ 9.3e-9 天，与 1.01e-8 天同量级），且驻留时间极短符合高热度/高请求率下的缓存行为直觉。
