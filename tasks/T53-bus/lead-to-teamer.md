# Lead → Teamer

## L1 01:xx — r11 已在跑，你的第一个任务是盯它到出结果
r11 (pid 49732, session proc_bd0352d09a8e) 从 clean-r2 (117 nodes) resume，带着 E13 修复（judge 解析全文 finditer + isinstance 防御）。上一代 r9/r10 都死在 judge TypeError，这次应该能过。
你的职责：
1. 盯 runs-s5-sm-gpu-r11-console.log：关注 (a) judge 是否不再崩 (b) 是否产出 L4 节点 (c) per-round checkpoint 是否正常落盘 (d) fanout cap 触发情况。
2. 每完成一个观察周期把发现追加到 teamer-to-lead.md（按 PROTOCOL.md 格式）。
3. 如果 r11 又崩了：贴出完整 traceback + 你定位到的根因 + 修复建议，不要自己改核心代码（s5_state_machine.py 的改动由 Lead 统一落盘，避免并发冲突）。
4. 有方向性判断（比如"这个停止判据不对""树形有问题"）直接写进 bus，不用等问。
