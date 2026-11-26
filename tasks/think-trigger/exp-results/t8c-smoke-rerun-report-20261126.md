# T8c smoke 重跑报告（2026-11-26 夜）

# origin: ai · 执行者 pid 97852 死于 A 臂后，supervisor 接力 B 臂（pid 1383），eval 由 Lead 验收
# 数据: raw_outputs_t8c.json（A 臂=重跑数据, B 臂=接力数据）· 备份: *.pre-rerun.json
# 判据: t8c-preregistration.md §4 Stage 0（commit 8c168c2a4 冻结，判据先于数据）

## 判决：停止，不扩样（无分离迹象）

| 臂 | 标签 | s（有效样本） | 截断 | d_mean | repeat5max |
|---|---|---|---|---|---|
| A' | A3, A3, A3 | 0/3 = 0.0 | 0 | 3.0 | 8 |
| B' | indeterminate, A3, indeterminate(截断) | 1/2 = 0.5 | 1/3 | 3.5（有效 2 个） | 13 |

机械检查：截断率 ≤50% ✓（B 臂 1/3），judge 全出标签 ✓。
分流：分离迹象要求 s_B'≥2/3 且 s_A'≤1/3。B 臂 1 个截断样本按 §1 单独计数不进 s 分母
→ 有效分母 2，s_B'=1/2 < 2/3 → **无分离 → 停止**。方向为正（B 0.5 > A 0.0）但未达
pre-commit 阈值。按预注册纪律如实报告，不扩 n=9（n=3 对弱效应无检验力，烧 27b 换
不可检出的检验 = 浪费）。

## 关键发现（负结果的三个出口）

**F1 A 臂标签整体翻转（indeterminate→A3）= n=3 测量噪声的定量证据**
pre-rerun（第一次跑）A 臂 3/3 indeterminate（d=4.0）；重跑后 A 臂 3/3 A3（d=3.0）。
同一 judge 版本（correctness_layer_v0），不同数据批次 → 标签全翻。两批都是 s=0
（都断点），方向不受影响，但说明 **A 臂基线在 n=3 下不稳定**——这正是预注册
"n=3 无检验力、n=9 前验 power 对弱效应 <0.3"设计的实证支持。排除的错误解释：
"B 臂优势来自 judge 对 B 臂拼接文本的偏袒"——A 臂自己都在两批间翻转，judge 不是
单向偏置源。

**F2 B 臂复读退化是生产实例（repeat5max=13，1/3 截断）**
B 臂 6 阶段里 5 个阶段触发复读警告（repeat5≥5），run3 的 04.5 阶段撞 12288 token
上限被截断（finish=length）。六阶段流程在 27b 下产生复读循环——**流程的价值正在被
退化侵蚀**：B 臂 41k token 里有多少是真推理、多少是复读，需要单独审计。
这恰好是 think-trigger T4（打转检测）的生产靶子：T4 检测的"同一试错重复"在
B 臂 stage 级已经出现。

**F3 执行者死亡模式确认（pid 97852 死于 A 臂后，无 traceback）**
第二次观察到"长跑进程无声死亡"（第一次见 11-15 教训：6 个 run 全死无 traceback）。
共同点：`&` 起的进程绑在当轮进程组，turn 切换时被回收。executor-protocol 已要求
setsid nohup + PID 写 goal state，但本次执行者用的是 Hermes 跟踪后台（收据 start_note
有记录）——**Hermes 跟踪后台 ≠ setsid 脱离**，这个等价假设被证伪。协议需修订：
长跑进程必须 setsid nohup，Hermes 跟踪只用于短任务。

## 对 T8c 主 claim 的影响

H1（多阶段赢）在 n=3 无分离信号 → 按预注册停止。claim 状态：
**"27b + 本题面 + 73728 预算下多阶段流程的 correctness 优势未检出（n=3 smoke，
方向弱正 0.5 vs 0.0，B 臂伴复读退化+1/3 截断）"**。
若要推进 H1，前置条件不是扩样，而是先修 F2（B 臂复读退化）——退化中的 B 臂
即使扩到 n=9，测的也是"退化流程 vs 直接求解"，不是"流程 vs 直接求解"。

## 下一步（按性价比）

1. B 臂复读退化审计（脚本可算：每 stage 的 unique n-gram 比例/复读段占比）→ 判退化
   是 prompt 问题还是 27b 能力问题
2. 若退化可修 → 修后重跑 smoke（B 臂）；不可修 → T8c 降级为负结果报告，转 T8c-JudgeFix
   队列项
3. executor-protocol 修订：长跑进程 setsid 硬性要求（F3）
