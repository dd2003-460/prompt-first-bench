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

## L2 01:57 — E14b 已落盘，r11 继续跑不用动

E14（resume 处 _as_int）+ E14b（pass_rate 计算防御式取 int）都已提交。当前 r11 进程内存里 dropped_redundant=[] 的问题：E14b 让 :657 不再炸，但 pass_rate 会按 n_new_dropped=0 算（偏乐观），不影响本轮跑完。如果 r11 崩到 FATAL handler，checkpoint 保存路径上 dropped_redundant 写 [] 是旧行为——下次 resume 时 E14 的 _as_int 会兜住。所以 r11 不用重启，让它跑完这轮；下一轮从新 ckpt resume 就是干净的 int。

## L3 02:15 — r12 verify-only 已启动，盯核验进度

r12 (pid 55594) 从 sm-gpu-r11-crash-303.json resume，--verify-only 模式：跳过 decompose，直接核验 192 个 L4 pending 节点。每批 3 个，每批落 checkpoint。关注：(a) verify_batch 是否正常返回（不再 TypeError）(b) verified/degraded/failed 比例 (c) 是否有新 FATAL。日志：runs-s5-sm-gpu-r12-console.log。

## L1 03:48 — 开工确认 + 第一条上下文
Teamer 你好，我是 Lead。你刚被 spawn，先读 NIGHT-PROTOCOL.md 和 T53-night-autonomy.md。
补充一条：r14 日志里已经看到 structural test 双向生效（N25/N26 quotient→cartesian 改判正确），所以 step 2 的判据重点看最终分布而不是中途现象。
另外 idea #47 消融刚收口（A带prior 2/3 vs B无prior 2/3 = 混合效应），数据在 research/l1-repro-probe{,-v2}.jsonl，如果你 bench 选题时碰到"不确定性维度"相关的设计问题可以参考。
开始吧。
