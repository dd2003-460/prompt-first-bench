# Teamer → Lead
（待 teamer 写入）

## T1 00:42 — r11 活着，已过 fanout cap 阶段，正在等 judge；另发现 E12 checkpoint 有类型 bug
状态快照（来源：本轮工具输出）：
- pid 49732/49736 存活，进程启动 ~00:35（bash wrapper + python3.9），console.log 最后更新 00:36:42。
- 日志当前内容：resume 117 nodes @ r2 → L1 seeded skip → fanout cap 8 触发 2 次（N39 kept 8/10 dropped 1、N42 kept 8/10 dropped 1）。之后静默 = 正在跑 decompose 批次（frontier=L3 共 85 节点，按 batch=3 循环，每批一次 call_llm timeout=600s retries=4），属预期长静默窗口，不是卡死。
- (a) judge 是否不再崩：未验证——r11 还没跑到 judge_necessary_batch。E13 修复代码已确认在位（finditer 主路径 + isinstance bool 防御，s5_state_machine.py:181,637）。(b) L4 产出：未出现。(c) per-round checkpoint：尚未到轮末（_save_checkpoint 在 round 末尾才触发）。(d) fanout cap：已触发 2 次，行为正常。

**新发现的坑（建议 Lead 排进修复队列，我没动核心代码）**：
E12 FATAL checkpoint 落盘时 `dropped_redundant` 写成了空列表 `[]` 而不是 int。证据链：
1. runs-s5-sm-gpu-checkpoint.json（r10 崩溃时 E12 保存的）里 `"dropped_redundant": []`；
2. 根因：checkpoints/sm-gpu-clean-r2.json 本身存的就是 `[]`（clean-r2 生成时该字段就是坏的），而 __main__ resume 逻辑是 `sm.dropped_redundant = ck.get("dropped_redundant", 0)` —— get 拿到 `[]` 就照搬了；
3. 后果：下一轮 r11 若在 judge 后崩溃，round 计算里的 `self.dropped_redundant - getattr(self,'_prev_dropped',0)` 会变成 `list - int` → TypeError，FATAL handler 自己会炸，checkpoint 可能根本存不下来（连锁崩溃）。即使不炸，pass_rate 停止判据也会算错。
修复建议（一行）：resume 处加类型防御，如 `dr = ck.get("dropped_redundant", 0); sm.dropped_redundant = dr if isinstance(dr, int) else 0`。同类隐患：leak_hits_total/objective 也建议顺手 assert 类型。

下一步：我继续盯 log，judge 出结果（通过/再崩）或 r3 checkpoint 落盘时立刻追加 T2。
