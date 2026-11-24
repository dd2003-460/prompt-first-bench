# N1229: 1080p 图片在 WebP q=60 压缩下的平均文件大小 s_webp_1080p_q60 的实测基准值，用于判断是否超过 150KB 阈值；若 s_web

- **status**: degraded
- **level**: L6
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N422

## Claim

1080p 图片在 WebP q=60 压缩下的平均文件大小 s_webp_1080p_q60 的实测基准值，用于判断是否超过 150KB 阈值；若 s_webp_1080p_q60 > 150 KB，则必须启用 Resize 或降低质量因子。

## Corrected Claim

1080p 图片在 WebP q=60 压缩下的大小因图像内容而异，通常需实测确定；若实测大小超过 150KB，则建议启用 Resize 或降低质量因子。

## Evidence

[质询]该陈述声称存在一个具体的“实测基准值”用于判断是否超过150KB，但WebP文件大小高度依赖于图像内容（熵、色彩复杂度），不存在通用的固定基准值；且参考来源中未提供1080p q=60的具体平均文件大小数据，仅提供了压缩参数建议或对比研究背景，无法直接支持该具体数值阈值或基准值的存在。 | 逻辑上，文件大小确实取决于质量和尺寸，但具体数值（如150KB阈值对应的基准值）属于经验事实，参考来源[1][2][3]均未提供1080p q=60的具体平均文件大小数据，无法直接支持该具体基准值，故降级。

## Search Query

average file size of 1080p image compressed to WebP quality 60

## Retrieval Sources

- {'url': 'https://www.cnblogs.com/yuexiaosheng/p/12389867.html&rut=d79a4eedeb534483590b48b1d2056e8fe771661f4e888f4b883413f35b51712f', 'type': 'ddg', 'title': 'Webp 用哪个压缩比优化好 - 月小升 - 博客园'}
- {'url': 'https://blog.csdn.net/jemenchen/article/details/98208417&rut=8a18c56bda7dd82aca303a900ce0e78794b376628f16d9725829d39bf1f71a62', 'type': 'ddg', 'title': '尺寸压缩与质量压缩的文件大小及效果对比，webp格式_图片质量压缩和尺寸压缩区别-CSDN博客'}
- {'url': 'https://developers.google.com/speed/webp/docs/webp_study?hl=zh-cn&rut=f12071822aa36fa4f371f21f7527dfe86ea6e88d5b6d6d0e853edb87e1a5664a', 'type': 'ddg', 'title': 'WebP 压缩研究 | Google for Developers'}
