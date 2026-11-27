# N119: 静态展示成本 γ_display 的量化：γ_display = $0.001 * (Pixel_Area / 1000)，假设提示区域面积为 5000 像素，

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N41

## Claim

静态展示成本 γ_display 的量化：γ_display = $0.001 * (Pixel_Area / 1000)，假设提示区域面积为 5000 像素，则 γ_display = $0.005，该成本随 UI 复杂度线性增加，但不随更新频率变化。

## Corrected Claim

静态展示成本 γ_display 的量化：γ_display = $0.001 * (Pixel_Area / 1000)，假设提示区域面积为 5000 像素，则 γ_display = $0.005，该成本随 UI 复杂度线性增加，但不随更新频率变化。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

UI display cost per pixel e-commerce platform
