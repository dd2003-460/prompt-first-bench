# T53b 验证与收口 Goal
# origin: ai, 2026-11-20

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
