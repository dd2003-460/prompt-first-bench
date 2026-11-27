# N166: LFU 热点集合的总请求字节量计算：Sum_{i=1}^{N_hot} S_i * P_i = Sum_{i=1}^{N_hot} E[S_i] * f_i *

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N59

## Claim

LFU 热点集合的总请求字节量计算：Sum_{i=1}^{N_hot} S_i * P_i = Sum_{i=1}^{N_hot} E[S_i] * f_i * R_total，其中 R_total 为总请求次数 50,000,000 次/天，f_i 为第 i 个对象的请求频率，E[S_i] 为第 i 个对象的期望大小。

## Corrected Claim

LFU 热点集合的总请求字节量计算：Sum_{i=1}^{N_hot} S_i * P_i = Sum_{i=1}^{N_hot} E[S_i] * f_i * R_total，其中 R_total 为总请求次数 50,000,000 次/天，f_i 为第 i 个对象的请求频率，E[S_i] 为第 i 个对象的期望大小。

## Evidence

先验知识/题面给定，逻辑校验通过：总请求字节量等于各对象期望大小乘以该对象总请求次数（频率×总次数）之和，公式推导符合定义。
