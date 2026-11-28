# origin: ai (2026-11-28 sm-run3 任务卡 · G5 定案 · 载体=sub-27b)
# 本任务书是 sub 的唯一指令来源。不要读本任务书以外的任何规划/记忆文件。

## 任务
定案 G5：q9 v2 队列的幂等检查是否存在假阳性（json 文件缺失但队列日志标了 SKIP）。
给出 是/否 判决 + 根因（哪一行逻辑、为什么）+ 证据（文件:行号）。

## 背景事实（已核，直接用）
- 工作目录：/Users/a1-6/Desktop/workspace/pfb-thinkmech
- 队列日志 /tmp/q9-budget-scan-queue.log 里有 `budget=300 rep=3 SKIP (existing: ...)` 之类的行
- 数据目录 modules/B-pipeline-ablation/data/q9-budget-scan/ 里 q9-300-r3-*.json 曾经缺失（13:50 重启队列后可能已补跑，先 ls 确认现状）
- 13:50 队列重启后 300-r3 可能已正常补跑——若 json 已存在，假阳性已自愈，但你仍要解释当时为什么标 SKIP

## 步骤
1. ls 数据目录，记录 q9-300-r3 现状（存在/缺失/文件名+时间戳）
2. 读 experiments/stage-ablation/q9_budget_scan_queue_v2.sh 全文（<200 行），找到 SKIP 判定逻辑（already_done / existing 判定那段）
3. 静态分析：该判定在什么条件下会对「文件实际不存在」返回 SKIP？重点看：glob 匹配模式、通配符、文件名时间戳后缀、大小写、路径拼接
4. 隔离复现（不许跑队列本身！）：把判定逻辑抄成一个独立小脚本，用「不存在的文件名」喂它，看返回什么。复现脚本写到 /Users/a1-6/.hermes/cache/scratch/g5-repro.py
5. 结论写入 tasks/rsi-pilot/sm-run3-g5-verdict.md（<30 行）：判决(是/否) + 根因(文件:行号) + 复现输出 + 修复建议(一行，不实施)

## 边界（违反=任务失败）
- 禁止运行 q9_budget_scan_queue_v2.sh 或 launch_q9_detached_v2.sh（会启动数小时的实验）
- 禁止 kill 任何进程
- 禁止修改任何现有脚本（只报告修复建议）
- 只读 + scratch 目录写复现脚本 + 写 verdict 文件
- 无网络（本任务不需要）

## 验收
sm-run3-g5-verdict.md 存在，含：明确判决词(是/否) + 至少一个 文件:行号 引用 + 复现脚本输出摘录。
