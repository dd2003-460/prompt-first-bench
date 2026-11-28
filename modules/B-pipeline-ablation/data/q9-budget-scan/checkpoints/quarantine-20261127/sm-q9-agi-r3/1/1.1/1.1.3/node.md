# N32: 基于阿梅德定律（Amdahl's Law），TP=4 的理论加速比上限受限于串行部分占比，若通信开销占比为 C%，则最大加速比 S_max = 1/(C + (

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N6

## Claim

基于阿梅德定律（Amdahl's Law），TP=4 的理论加速比上限受限于串行部分占比，若通信开销占比为 C%，则最大加速比 S_max = 1/(C + (1-C)/4)，需实测校准 C 值。

## Corrected Claim

基于阿梅德定律（Amdahl's Law），TP=4 的理论加速比上限受限于串行部分占比，若通信开销占比为 C%，则最大加速比 S_max = 1/(C + (1-C)/4)，需实测校准 C 值。

## Evidence

先验知识/题面给定，逻辑校验通过：阿梅德定律公式 S = 1/(1 - p + p/N) 中，若串行部分占比为 C，则 S_max = 1/(C + (1-C)/N)，代入 N=4 即得 S_max = 1/(C + (1-C)/4)，公式推导正确且符合物理直觉。
