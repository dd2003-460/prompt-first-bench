# N425: WebP q=80 压缩下的单张图片平均字节数 s_webp_q80 需满足 s_webp_q80 ≈ 300 KB；若实际大小偏离 ±20%（即 240-36

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N138

## Claim

WebP q=80 压缩下的单张图片平均字节数 s_webp_q80 需满足 s_webp_q80 ≈ 300 KB；若实际大小偏离 ±20%（即 240-360 KB 之外），则 N138 的 '平衡工作点' 定义失效，需重新校准质量-带宽权衡曲线。

## Corrected Claim

WebP q=80 压缩下的单张图片平均字节数 s_webp_q80 通常处于数百KB量级（具体数值取决于源图分辨率与内容），若实际大小显著偏离预期基准（如±20%），则需重新校准质量-带宽权衡曲线。

## Evidence

[质询]该陈述将特定经验参数（q=80时平均300KB）作为通用事实，但WebP文件大小高度依赖于源图像分辨率、内容复杂度及编码设置（如-m参数），不同来源推荐的平衡点质量参数（如75或80）及对应文件大小并无统一标准，且参考来源未提供q=80对应300KB的具体数据支持。 | 经验事实，逻辑自洽但缺来源支持；来源[1]推荐q=75，来源[3]提及q=80效果优但未给出具体字节数，无法直接验证300KB这一具体数值。

## Search Query

WebP quality 80 average file size 1080p image KB

## Retrieval Sources

- {'url': 'https://www.cnblogs.com/yuexiaosheng/p/12389867.html&rut=d79a4eedeb534483590b48b1d2056e8fe771661f4e888f4b883413f35b51712f', 'type': 'ddg', 'title': 'Webp 用哪个压缩比优化好 - 月小升 - 博客园'}
- {'url': 'https://developers.google.com/speed/webp/docs/webp_study?hl=zh-cn&rut=f12071822aa36fa4f371f21f7527dfe86ea6e88d5b6d6d0e853edb87e1a5664a', 'type': 'ddg', 'title': 'WebP 压缩研究 | Google for Developers'}
- {'url': 'https://blog.csdn.net/jemenchen/article/details/98208417&rut=8a18c56bda7dd82aca303a900ce0e78794b376628f16d9725829d39bf1f71a62', 'type': 'ddg', 'title': '尺寸压缩与质量压缩的文件大小及效果对比，webp格式_图片质量压缩和尺寸压缩区别-CSDN博客'}
