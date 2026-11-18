# Ralph Loop 夜间任务（2026-11-18 23:15 启动）

## 循环规则
- 每 5 分钟检查一次进程状态
- 进程挂了 → 诊断原因 → 修复 → 重启（最多重试 2 次）
- 进程正常 → 等
- 所有任务完成 → 写汇总报告 → 停

## Todolist（按顺序执行）

### T1: 监控 gptr 三题×3rep（进程 57218）
- 日志：`/tmp/gptr-official-3q.log`
- 输出：`runs-gptr-official/`
- 完成标志：日志出现 `=== ALL DONE (9 runs) ===`
- 验收：`runs-gptr-official/summary.json` 存在，9 条记录，elapsed_s > 0
- 如果挂了：检查 8787 是否健康（curl 127.0.0.1:8787/health），健康则重启：
  ```bash
  cd /Users/a1-6/Desktop/workspace/pfb/experiments/stage-ablation
  .venv-d1/bin/python -u gptr_official_3q.py > /tmp/gptr-official-3q.log 2>&1 &
  ```
- 预计完成：2-4 小时（depth=6 比 depth=2 慢很多）

### T2: 监控 langgraph nat（进程 42852）
- 日志：`/tmp/lg-pfb-full-nat.log`
- 完成标志：日志出现 `[LG:stop]` 或 `FINAL` 或进程退出
- 验收：日志末尾有 S_α 值 + verified 比例
- 如果挂了：检查 8787，健康则重启：
  ```bash
  cd /Users/a1-6/Desktop/workspace/pfb/experiments/stage-ablation
  rm -f /tmp/langgraph-pfb-full-nat.sqlite*
  /Library/Developer/CommandLineTools/usr/bin/python3 -u langgraph-pfb-full.py nat > /tmp/lg-pfb-full-nat.log 2>&1 &
  ```

### T3: langgraph gpu 题（T2 完成后启动）
- 命令：
  ```bash
  cd /Users/a1-6/Desktop/workspace/pfb/experiments/stage-ablation
  rm -f /tmp/langgraph-pfb-full-gpu.sqlite*
  /Library/Developer/CommandLineTools/usr/bin/python3 -u langgraph-pfb-full.py gpu > /tmp/lg-pfb-full-gpu.log 2>&1 &
  ```
- 日志：`/tmp/lg-pfb-full-gpu.log`
- 验收：日志末尾有 S_α 值 + verified 比例

### T4: 汇总报告（T1+T3 都完成后）
- 写 `runs-gptr-official/night-report.md`，包含：
  1. gptr 9 runs 的 elapsed/chars 表格
  2. langgraph nat + gpu 的 S_α / verified 率 / 节点数
  3. 与 S0 baseline 对比（nat cov≥0.634, gpu depth≥0.50）
  4. 异常记录（502、重试、失败）
- 格式：markdown 表格 + 结论

### T5: git commit（T4 完成后）
```bash
cd /Users/a1-6/Desktop/workspace/pfb
git add experiments/stage-ablation/runs-gptr-official/ experiments/stage-ablation/s5-pipeline-spec.md experiments/stage-ablation/gptr_official_3q.py experiments/stage-ablation/cc-tasks/
git commit -m "night-run: gptr 3q×3rep (depth6/breadth6) + langgraph nat/gpu + s5 spec"
```

### T6: A0-A13 完整消融 sweep（T4 汇总完成后启动，今晚跑不完，留白天）
- 前置：gptr + langgraph nat + gpu 全部完成（避免抢 8787 推理）
- 命令：
  ```bash
  cd /Users/a1-6/Desktop/workspace/pfb/experiments/stage-ablation
  /Library/Developer/CommandLineTools/usr/bin/python3 -u qc_ablation_sweep.py --arms all --qs nat,soc,gpu --reps 3 > /tmp/qc-ablation-14arms.log 2>&1 &
  ```
- 14 臂 × 3 题 × 3 rep = 126 runs，预计 10-17h
- 断点续跑：step-log/{arm}-{qid}.jsonl 每步落盘 + 每 run 完成写 {arm}-{qid}-r{rep}.json，重启跳过已完成
- 验收：runs-qc-ablation/summary.md 存在，126 行
- 完整矩阵定义：`ablation-matrix-full.md`（A0-A13，4 因子，补 A10-A13 二阶交互角点）
- 前人重合映射：`ablation-prior-work-mapping.md`（C1-C10 组件 × 前人工作，套磁优先级，复现 vs 创新清单）
- 注意：A10-A13 是 2026-11-18 补的（补全 D2×D4/D2×D5/D3×D4/D3×D5 二阶交互角点，缺了这 4 臂对应交互估不出来）

## 监控命令（每 5 分钟跑一次）
```bash
echo "=== $(date) ==="
echo "--- gptr ---"
ps aux | grep "gptr_official" | grep -v grep || echo "gptr: 已退出"
tail -3 /tmp/gptr-official-3q.log
echo "--- langgraph nat ---"
ps aux | grep "langgraph-pfb-full.*nat" | grep -v grep || echo "langgraph nat: 已退出"
tail -3 /tmp/lg-pfb-full-nat.log
echo "--- langgraph gpu ---"
ps aux | grep "langgraph-pfb-full.*gpu" | grep -v grep || echo "langgraph gpu: 未启动/已退出"
tail -3 /tmp/lg-pfb-full-gpu.log 2>/dev/null
echo "--- 8787 ---"
curl -s -o /dev/null -w "8787: %{http_code}\n" http://127.0.0.1:8787/health
```

## 停止条件
- T1-T5 全部完成 → 写 "ALL TASKS DONE" 到 `/tmp/ralph-night-done.txt` → 停
- 同一任务重试 2 次仍失败 → 记录原因到 night-report.md → 跳过继续下一个
- 8787 持续不健康 > 10 分钟 → 记录 → 等（不重启 vLLM，那是 watchdog 的活）

## 注意
- 不要同时跑两个 gptr（VRAM 不够）
- langgraph 和 gptr 可以并行（langgraph 用 python3.9，gptr 用 .venv-d1 python3.12，不冲突）
- 所有输出落盘到 pfb/experiments/stage-ablation/ 下，不要写到 /tmp 以外的地方（日志除外）
- 2026-11-18 修复：no_challenge 臂（A1/A3/A8/A10/A11）原来没真正去掉反方质询（两分支都调 verify_node，D2 主效应恒为 0 假阴性）。已加 P3_VERIFY_NC + verify_node_nc（s5_pipeline.py），qc_ablation_sweep.py 的 no_challenge 分支真正走它。跑 A0-A13 前确认修复已生效（grep verify_node_nc qc_ablation_sweep.py 应有匹配）。
- 2026-11-18: langgraph max_nodes 从 12 改回默认 150（日常完整 pipeline 水平；12 是早期快速验证值，太小，只跑了 12 个节点就停，不反映真实 pipeline 表现）。日常完整 pipeline 历史节点数：nat=278/soc=283（verified 率 65-79%）。
