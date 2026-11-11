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

## T2 02:24 — r14 进程已死（日志停在 r3 中途，无 DONE/FATAL），structural test 方向验证通过；建议从 sm-gpu-r2.json resume
状态快照（来源：本轮工具输出，非记忆）：
- r14 console.log 最后更新 02:17:07，此后无写入、无新 checkpoint（checkpoints/ 最新仍是 02:14 的 sm-gpu-r2.json）、无 runs-s5-sm-gpu-checkpoint.json FATAL dump、无 r14 pid 文件。launch.sh 会追加 EXIT 行——r14 log 没有 → 进程被 SIGKILL（OOM/外部杀），不是代码崩溃。
- 进度：L1(5) → r1(+17=22) → r2(+37=59) → r3 拆到 N57+ 后中断。r2 checkpoint 完整落盘：59 nodes, state=rework。
- **edge_types 分布（r2 ckpt，关键判据）**：cartesian 45 / quotient 14 = **quotient 23.7%**。对比 r13 终态 63/70=90%。structural test 双向生效确认：N25/N26 quotient→cartesian（TCO 加和项改判正确）+ N8/N10/N23/N24 cartesian→quotient（BW=通信量/带宽、成本=功率×时间×单价 等显式运算结构判对）。方向对了，但离 ≤20% 目标还差一点。
- status（r2 ckpt）：verified 20 / degraded 33 / pending 5 / failed 1 → degraded 56%，与 r13 的 54% 持平（ego-browser 慢导致的检索降级，属已知降级非故障）。
- levels：L1=5, L2=17, L3=37（max_depth=4 未到，r3 还在拆 L3/L4）。
- 本地 LLM (127.0.0.1:8787 qwen3.8-27b) 存活正常。

判断与建议（供 Lead 决策，我没动核心代码）：
1. **resume 路径**：`--resume checkpoints/sm-gpu-r2.json --max-nodes 150`（skip_l1=True 跳过 L1，从 59 节点续拆 r3+）。E14/E14b 类型防御已提交，sm-gpu-r2.json 是干净 int 字段，resume 安全。
2. **quotient 23.7% vs 目标 ≤20%**：略超线。两个选项——(a) 先 resume 跑完看终态分布（r3/r4 深层节点可能进一步稀释或推高）；(b) 若坚持 ≤20% 再修 prompt 跑 r15。我倾向 (a)：先拿完整数据点，避免为 3.7pp 反复重跑整树。
3. **degraded 56% 偏高**：r13/r14 都卡在 ~55%，根因是 ego-browser 通道慢/超时（r13 有 WEBLLM-SKIP PageNavigationTimeoutError）。如果 bench 泛化阶段要真实 evidence，需要先把 ego-browser 稳定性解决，否则 verified 率上不去。
