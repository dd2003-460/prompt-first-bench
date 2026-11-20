# T53b 验证与收口 Goal
# origin: ai, 2026-11-20

## 进度（2026-11-20 13:48）
- [x] verify_checkpoints.py PASS（P0 全过 + P1 100%）—— 修了 T12/T13/T14 指向多路 watchdog 的 bug（旧脚本 pgrep 匹配不到 -multi.sh → T14 假 FAIL）。commit 已落。
- [x] 回滚 4 个空 run 重跑（gpu_formula_r09/r10, gpu_text_r01, soc_formula_r02）—— 根因=旧 watchdog 180s 误杀 + E18 5xx 无限重试致 SM 挂住。现 1800s+活性检查已修。
- [x] py-spy 已装（13:33），后续卡死可抓栈诊断
- [ ] 62 run 全部 done（当前 13/62 有数据，4 回滚重跑 + 45 排队，估 6-7h）
- [ ] ablation-results.json 完整 + commit
- [ ] watchdog 日志无连续 SM stale kill（监控中）
- [ ] **残余风险（2026-11-20 13:50 发现）**：1800s 阈值在 E18 无限重试 + curl 600s 超时组合下仍可能误杀。模式：8787 proxy 在上游 5xx 时可能挂住不立即返回 → curl 600s 超时 + 300s 退避 = 900s/周期 → 2 周期 = 1800s = kill。日志实证：7 次 kill 前都有多次"跳过 kill"（活性检查说有子进程），60s 内突然"无子进程无连接"（curl 子进程刚退出，SM 进入退避 sleep）。修复方向（收口时做）：① curl 超时 600→120s（缩短周期）；② watchdog 活性检查加"最近 5min 内有 curl 子进程启动过"判断（区分退避 sleep 和真卡死）。不影响正在跑的 62 run。

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
