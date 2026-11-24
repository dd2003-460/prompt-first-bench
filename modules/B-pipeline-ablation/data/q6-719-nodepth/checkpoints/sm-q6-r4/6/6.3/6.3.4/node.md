# N361: 混合分布对缓存命中率的非线性影响：由于 w_img >> w_vid 且 α_img > α_vid，混合缓存命中率 Hit_Rate_mix 更接近图片命中率

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N125

## Claim

混合分布对缓存命中率的非线性影响：由于 w_img >> w_vid 且 α_img > α_vid，混合缓存命中率 Hit_Rate_mix 更接近图片命中率，但受视频长尾拖累，需分别计算 Hit_Rate_img 和 Hit_Rate_vid 后加权：Hit_Rate_mix = w_img × Hit_Rate_img + w_vid × Hit_Rate_vid。

## Corrected Claim

混合分布对缓存命中率的非线性影响：由于 w_img >> w_vid 且 α_img > α_vid，混合缓存命中率 Hit_Rate_mix 更接近图片命中率，但受视频长尾拖累，需分别计算 Hit_Rate_img 和 Hit_Rate_vid 后加权：Hit_Rate_mix = w_img × Hit_Rate_img + w_vid × Hit_Rate_vid。

## Evidence

先验知识/题面给定，逻辑校验通过：加权平均公式符合概率论全概率公式，且权重与命中率特征描述符合缓存系统常见经验规律。
