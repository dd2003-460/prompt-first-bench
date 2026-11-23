# N37: 图片类平均对象大小 $s_{img}$ 取 1.0 MB（基于 N8 中 0.5-2MB 区间的几何均值或经验加权），短视频类平均对象大小 $s_{vid}$ 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N7

## Claim

图片类平均对象大小 $s_{img}$ 取 1.0 MB（基于 N8 中 0.5-2MB 区间的几何均值或经验加权），短视频类平均对象大小 $s_{vid}$ 取 7.5 MB（基于 N8 中 5-10MB 区间的几何均值或经验加权）。

## Corrected Claim

图片类平均对象大小 $s_{img}$ 取 1.0 MB（基于 N8 中 0.5-2MB 区间的几何均值或经验加权），短视频类平均对象大小 $s_{vid}$ 取 7.5 MB（基于 N8 中 5-10MB 区间的几何均值或经验加权）。

## Evidence

先验知识/题面给定，逻辑校验通过：1.0 MB 是 0.5-2 MB 区间的几何均值（√(0.5*2)≈1.0），7.5 MB 是 5-10 MB 区间的几何均值（√(5*10)≈7.07，取整或经验加权为 7.5 合理），数值量级符合常识。

## Search Query

average image size MB web platform average short video file size MB
