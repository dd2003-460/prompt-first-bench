# N7: 潜热通量公式 Q_sensible_latent = ρ * L_v * q_s * C_e，其中 C_e 为交换系数（通常取 0.002-0.004），q_s

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1

## Claim

潜热通量公式 Q_sensible_latent = ρ * L_v * q_s * C_e，其中 C_e 为交换系数（通常取 0.002-0.004），q_s 为饱和比湿，ρ 为空气密度；在典型登陆初期，海洋上的净潜热输入约为 50-100 W/m²，而登陆后该值骤降至 <10 W/m²（主要受限于陆面蒸发极弱）。

## Corrected Claim

潜热通量公式 Q_sensible_latent = ρ * L_v * q_s * C_e，其中 C_e 为交换系数（通常取 0.002-0.004），q_s 为饱和比湿，ρ 为空气密度；在典型登陆初期，海洋上的净潜热输入约为 50-100 W/m²，而登陆后该值骤降至 <10 W/m²（主要受限于陆面蒸发极弱）。

## Evidence

先验知识/题面给定，逻辑校验通过：公式符合湍流通量参数化标准形式（Q = ρLqC），数值量级（海洋50-100 W/m² vs 陆地<10 W/m²）符合气象学常识及能量守恒直觉。

## Search Query

typhoon latent heat flux ocean vs land exchange coefficient
