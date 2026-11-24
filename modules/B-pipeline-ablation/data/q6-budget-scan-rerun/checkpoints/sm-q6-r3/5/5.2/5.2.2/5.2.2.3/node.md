# N313: 混合对象大小对 CHR 的加权影响：CHR_weighted = w_img × CHR(s_img) + w_vid × CHR(s_vid)，其中 w_im

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N100, N101, N102

## Claim

混合对象大小对 CHR 的加权影响：CHR_weighted = w_img × CHR(s_img) + w_vid × CHR(s_vid)，其中 w_img=0.7, s_img=500KB, w_vid=0.3, s_vid=5MB (N16)；需分别计算小对象和大对象的 N_capacity (C_eff/s)，代入 N134 公式后加权求和，以反映真实流量组合下的命中率

## Corrected Claim

混合对象大小对 CHR 的加权影响：CHR_weighted = w_img × CHR(s_img) + w_vid × CHR(s_vid)，其中 w_img=0.7, s_img=500KB, w_vid=0.3, s_vid=5MB (N16)；需分别计算小对象和大对象的 N_capacity (C_eff/s)，代入 N134 公式后加权求和，以反映真实流量组合下的命中率

## Evidence

先验知识/题面给定，逻辑校验通过：加权平均公式结构正确，量纲一致（权重无量纲，CHR为比率），参数引用自题面节点N16，符合混合流量命中率计算的基本逻辑。
