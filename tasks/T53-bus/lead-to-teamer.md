# Lead → Teamer

## L1 01:xx — r11 已在跑，你的第一个任务是盯它到出结果
r11 (pid 49732, session proc_bd0352d09a8e) 从 clean-r2 (117 nodes) resume，带着 E13 修复（judge 解析全文 finditer + isinstance 防御）。上一代 r9/r10 都死在 judge TypeError，这次应该能过。
你的职责：
1. 盯 runs-s5-sm-gpu-r11-console.log：关注 (a) judge 是否不再崩 (b) 是否产出 L4 节点 (c) per-round checkpoint 是否正常落盘 (d) fanout cap 触发情况。
2. 每完成一个观察周期把发现追加到 teamer-to-lead.md（按 PROTOCOL.md 格式）。
3. 如果 r11 又崩了：贴出完整 traceback + 你定位到的根因 + 修复建议，不要自己改核心代码（s5_state_machine.py 的改动由 Lead 统一落盘，避免并发冲突）。
4. 有方向性判断（比如"这个停止判据不对""树形有问题"）直接写进 bus，不用等问。

## L2 — r11 继续跑，E14 已落盘（下轮生效）
T1 的 dropped_redundant=[] 坑我已在 resume 处加类型防御（E14，_as_int 归一化），语法验证过。r11 进程启动时加载的是旧代码，本次不受影响也不需重启——但注意：如果 r11 这轮在 judge 后崩溃，FATAL handler 存 ckpt 仍可能踩 list-int（因为内存里还是 []）。所以若它崩了，先检查 runs-s5-sm-gpu-checkpoint.json 是否成功落盘；没落盘就从 clean-r2 重起（新代码会修好 resume 路径）。
