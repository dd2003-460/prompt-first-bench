# N428: HEIC 格式兼容性约束：iOS 11+ 原生支持 HEIC，但 Android 需额外解码库；若目标用户中 Android 占比 > 60%，则需同时分发 J

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N139

## Claim

HEIC 格式兼容性约束：iOS 11+ 原生支持 HEIC，但 Android 需额外解码库；若目标用户中 Android 占比 > 60%，则需同时分发 JPEG q=95 版本，导致存储冗余和缓存复杂度增加，H_img 可能进一步降至 70-75%。

## Corrected Claim

HEIC 格式兼容性约束：iOS 11+ 原生支持 HEIC，但 Android 需额外解码库或存在版本碎片化问题；若目标用户中 Android 占比 > 60%，通常需同时分发 JPEG 版本以确保兼容性，这将导致存储冗余和缓存复杂度增加，可能对图像加载性能指标产生负面影响。

## Evidence

[质询]陈述中关于“H_img 可能进一步降至 70-75%”的具体数值预测缺乏来源支持，属于经验性估算，且未提供该指标的定义或计算依据，存在将定性影响量化为具体数值的风险。 | 来源[1]和[2]直接支持了iOS 11+原生支持HEIC以及Android存在兼容性/碎片化问题需额外处理的事实；但关于存储冗余导致H_img降至70-75%的具体数值结论在所有参考来源中均无直接证据支持，属于经验事实且缺乏多源一致或第一性原理推导，故降级。

## Search Query

HEIC format Android compatibility decoding overhead

## Retrieval Sources

- {'url': 'https://blog.csdn.net/weixin_29174141/article/details/163349662&rut=583a252c071bd1301c6940c5f8f89824c545030a60abb3468d9f070952aa276a', 'type': 'ddg', 'title': 'Android应用兼容HEIF/HEIC图片全攻略：从原理到实战解决方案'}
- {'url': 'https://support.apple.com/zh-cn/116944&rut=a878d82ba24a5e864cd96e44c3c5c5391556208533d0b81875f50795d44aa8bf', 'type': 'ddg', 'title': '在 Apple 设备上使用 HEIF 或 HEVC 媒体'}
- {'url': 'https://heictopng.net/en/heic-format-compatibility&rut=2145ea7d1a69a28e11011d58cbe1c1b389bb0e086acfed509bab6589d78366ce', 'type': 'ddg', 'title': 'HEIC Format Compatibility: Which Devices & Apps Support HEIC?'}
