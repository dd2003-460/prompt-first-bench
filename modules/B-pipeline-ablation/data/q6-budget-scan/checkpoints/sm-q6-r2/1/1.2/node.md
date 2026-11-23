# N7: 基础往返时延RTT_base的地理分布模型：RTT_base ≈ 0.05ms/km × 2 × D_user_to_edge，D_user_to_edge为用

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1

## Claim

基础往返时延RTT_base的地理分布模型：RTT_base ≈ 0.05ms/km × 2 × D_user_to_edge，D_user_to_edge为用户到最近边缘节点的光纤距离，需结合用户地理分布加权计算

## Corrected Claim

基础往返时延RTT_base的地理分布模型：RTT_base ≈ 0.05ms/km × 2 × D_user_to_edge，D_user_to_edge为用户到最近边缘节点的光纤距离，需结合用户地理分布加权计算

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别处理了公式中的系数修正（物理常数层面）和变量定义（地理分布层面），两者维度不同且互不重叠，覆盖了父节点中提到的‘系数准确性’和‘加权计算’两个核心要素，无冗余。）

## Search Query

fiber optic speed of light propagation delay 0.2 ms/km
