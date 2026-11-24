# N48: 云对象存储S3智能分层存储冗余系数R_cloud = 1.0，用户侧无冗余开销，自动在标准与低频间切换

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N9

## Claim

云对象存储S3智能分层存储冗余系数R_cloud = 1.0，用户侧无冗余开销，自动在标准与低频间切换

## Corrected Claim

云对象存储S3智能分层存储冗余系数R_cloud = 1.0，用户侧无冗余开销，自动在标准与低频间切换

## Evidence

先验知识/题面给定，逻辑校验通过：S3 Intelligent-Tiering 确实自动在标准与低频层间切换，且其冗余系数（相对于标准存储的额外冗余开销）通常视为 1.0（即无额外冗余开销，仅存储成本变化），符合云对象存储智能分层的定义。

## Search Query

S3 Intelligent-Tiering redundancy model
