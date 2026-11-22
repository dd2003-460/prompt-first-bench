# N304: Android 端‘新降价’推送触达率 R_Android 的计算：R_Android = (1 - 权限关闭率 p_off_Android) * 推送到达成功

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N102

## Claim

Android 端‘新降价’推送触达率 R_Android 的计算：R_Android = (1 - 权限关闭率 p_off_Android) * 推送到达成功率 r_arr_Android；Android 端权限关闭率较低（p_off_Android ≈ 0.2-0.3），但存在厂商通道拦截（如华为/小米后台查杀），导致 r_arr_Android ≈ 0.8-0.9，综合 R_Android ≈ 0.56-0.72，处于父节点区间的中上部。

## Corrected Claim

Android 端‘新降价’推送触达率 R_Android 的计算：R_Android = (1 - 权限关闭率 p_off_Android) * 推送到达成功率 r_arr_Android；Android 端权限关闭率较低（p_off_Android ≈ 0.2-0.3），但存在厂商通道拦截（如华为/小米后台查杀），导致 r_arr_Android ≈ 0.8-0.9，综合 R_Android ≈ 0.56-0.72，处于父节点区间的中上部。

## Evidence

先验知识/题面给定，逻辑校验通过：公式推导正确（0.7*0.8=0.56, 0.8*0.9=0.72），参数取值符合Android生态常识（权限关闭率低于iOS，厂商通道拦截导致到达率低于100%），数值量级合理。

## Search Query

Android push notification delivery rate manufacturer channel blocking stats
