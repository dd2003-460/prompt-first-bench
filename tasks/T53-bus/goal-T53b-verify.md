# T53b 验证与收口 Goal
# origin: ai, 2026-11-20

## 进度（2026-11-20 13:48）
- [x] verify_checkpoints.py PASS（P0 全过 + P1 100%）—— 修了 T12/T13/T14 指向多路 watchdog 的 bug（旧脚本 pgrep 匹配不到 -multi.sh → T14 假 FAIL）。commit 已落。
- [x] 回滚 4 个空 run 重跑（gpu_formula_r09/r10, gpu_text_r01, soc_formula_r02）—— 根因=旧 watchdog 180s 误杀 + E18 5xx 无限重试致 SM 挂住。现 1800s+活性检查已修。
- [x] py-spy 已装（13:33），后续卡死可抓栈诊断
- [ ] 62 run 全部 done（当前 13/62 有数据，4 回滚重跑 + 45 排队，估 6-7h）
- [ ] ablation-results.json 完整 + commit
- [ ] watchdog 日志无连续 SM stale kill（监控中）
- [x] **py-spy 抓栈工具链在 macOS 上失效（2026-11-20 14:12 验证）**：`py-spy dump --pid <活SM>` 返回 "This program requires root on OSX"。watchdog 13:34 加的抓栈逻辑会静默失败（错误写进 dump 文件，无"已抓栈"日志）。后台进程不能加 sudo（密码提示会挂住）。
- [x] **替代方案：系统自带 `sample` 免 root，已验证可用（2026-11-20 14:16）；但 14:32 对照组推翻"递归栈=卡死"解读**：`sample <pid> 2 -file out.txt` 对同用户进程直接可用。watchdog 已把 py-spy 换成 sample 并重启（pid 47871，14:17），kill 前自动抓栈留现场。但 14:32 抓对照组发现：① 14:16 标"nat_r05"的 26 层递归栈其实是 soc_r03（pid 21010 启动时间 13:24:30 对应 soc，标错）；② 同一 soc_r03 两次采样递归深度 26→14 波动；③ gpu_text_r02 也是 14 层。**深层递归栈是 SM 正常计算态，非卡死专属**——sample 栈区分不了健康 vs 冻结（Python 3.9 无符号 + 深度波动），只能当 kill 现场的存档证据，不能当诊断依据。真正的卡死判别器仍是日志 mtime（watchdog 原有逻辑）。
- [x] **死因诊断修正（2026-11-20 14:08，推翻 13:50 的"残余风险"判断）**：13:50 记的"E18 退避 sleep 被 1800s 误杀"是误诊。实证：① retry 行确实写进 sm.log（502 重试日志），若卡退避 sleep 日志 mtime 会新鲜，stale 不会触发；② 被 kill 的 run（soc_formula_r02/gpu_formula_r09）死前日志尾部是 CACHE-HIT / verify 输出，不是 retry 行；③ watchdog 报"无子进程无连接"= CPU 采样也没涨。真实死因：SM 在纯 Python 处理阶段（cache/verify）CPU 冻结 30min+ = 真挂死，watchdog kill 是**正确行为非误杀**。根因在 SM 代码纯 Python 路径（死循环/死锁候选）。
- [x] **coverage=0.0 是真实信号，非 judge bug（2026-11-20 14:20 一锤定音，推翻 14:15 的"judge 静默失败"假设）**：14:15 曾怀疑 s8b_pilot.judge() JSON 解析失败→scores 空→coverage 记 0。但当前批次 synth json 被 driver 拷到 `ablation-runs/{RUN}.json`，judge 原始返回就在里面——**无 parse_error，scores 是真实 0/1 评分**：gpu 各 run 的 15 个 GOLD 要点几乎全 0（r08 全 0→cov=0.0），nat 的 6 个要点覆盖 5/6（cov=0.833）。结论：judge 工作正常，**gpu arm 低 coverage 是真信号**（gpu prompt 的分解/答案确实没覆盖 GOLD 要点），04-verify 统计时直接计入，不需单独标记。注意：gpu scores 长度 15、nat 长度 6（GOLD 要点数按 qid 不同），非 bug。
- [x] **跨 arm coverage 不可直接比——GOLD 要点数混杂（2026-11-20 14:22 确认）**：GOLD 定义 nat=6 点、soc=7 点、gpu=15 点（s8b_pilot.GOLD）。coverage=covered/n_pts，15 点的题天然比 6 点的难覆盖满。所以 gpu 的 cov 低有一部分是**题目更难**（分母大），不全是 prompt 质量差。04-verify 跨 arm 对比时必须处理：① 用 depth（同口径，judge_v2_depth.overall）做主对比，coverage 只做同 qid 内对比；② 或 coverage 按要点难度归一化。否则会把"题难"误判成"gpu prompt 差"。
- [x] **depth 同口径也确认 gpu 系统性偏低（2026-11-20 14:24，n 尚小）**：depth 按节点树评、不依赖 GOLD 要点数，是跨 arm 同口径。已出数据：gpu mean=0.396(n=6)、nat 0.647(n=4)、soc 0.633(n=1)。depth 也低 → gpu 低**不是 GOLD 混杂的假象**，是真信号（gpu prompt 分解质量确实差）。但 n 太小无统计意义，等 62 run 跑完才下结论。注：ablation-runs/*.json 里 arm 字段=None（driver 写 results 用环境变量 ARM，synth json 没存 arm），靠 qid 区分 arm。
- [x] **维度纠正（2026-11-20 14:28，推翻 14:24 的"gpu prompt 差"结论）**：14:24 把 qid（题目）当成了 arm（prompt 格式）。run 名格式 `{qid}_{arm}_{rep}`：qid∈{nat,soc,gpu} 是 3 道不同的题，arm∈{formula,text} 才是 2 种 prompt 格式。"gpu vs nat vs soc" 是比 3 道不同的题，不是比 2 种 prompt——**对消融假设无效**。真正的消融：同题内 formula vs text 谁好。当前已出数据只有 formula arm（text 还没跑到），同题内对比做不了。gpu 题 depth 低（0.34）是**题目难度**（15 个 GOLD 要点 + 复杂计算），不是 prompt 格式问题。04-verify 必须按 (qid, arm) 二维分组，同 qid 内比 formula vs text。

## 目标
T53b 62 个消融 run 全部跑完并收口；验证 SSL 卡死修复（_probe_network）+ watchdog SM stale 检测在实际运行中有效，无复发。

## 阶段
1. 独立验证：跑 verify_checkpoints.py，确认 P0 全过 + P1 ≥80%
2. 代码落盘确认：grep 确认 _probe_network + 5 guard + SM_STALE 逻辑在文件里
3. 监控 batch：跟踪 62 run 推进，记录成功/失败/耗时
4. 收口：全部 done 后汇总 ablation-results.json，commit

## SOP 索引
- tasks/T53-bus/checkpoints-and-tests.md（卡点清单 + 测试矩阵）
- experiments/stage-ablation/verify_checkpoints.py（验证脚本）
- experiments/stage-ablation/t53b-watchdog.sh（watchdog + SM stale 检测）

## 验收标准
- verify_checkpoints.py 判定 PASS（P0 全过 + P1 ≥80%）
- 代码落盘确认（_probe_network + 5 guard + SM_STALE 都在文件里）
- 62 run 全部 done（或标记 done 跳过）
- ablation-results.json 有完整 runs 记录
- watchdog 日志无连续 SM stale kill（SSL 修复有效，无卡死复发）

## 失败降级
- 某 run 反复失败 → 标记 done 跳过，记录原因
- batch 死亡 → watchdog 自动重启（已验证）
- watchdog 死亡 → nohup bash t53b-watchdog.sh 重启
- SSL 卡死复发 → 检查 _probe_network 是否生效，必要时调阈值
