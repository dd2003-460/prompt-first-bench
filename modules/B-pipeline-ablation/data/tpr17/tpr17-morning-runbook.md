# T-PR-17 T4 pilot 晨检 runbook（pilot 完成后执行）

# origin: ai
# 触发: waiter 报告出现 "PILOT COMPLETE" 或 "PILOT ABORTED"
# 报告位置: modules/B-pipeline-ablation/data/tpr17/tpr17-pilot-report-*.md (最新一个)

## 0. 先看 waiter 报告结论
```
cat "$(ls -t modules/B-pipeline-ablation/data/tpr17/tpr17-pilot-report-*.md | head -1)"
```
- `PILOT COMPLETE — 9/9 cells` → 进 1
- `PILOT ABORTED` → 看中止原因（哪个 cell rc!=0 或 sanity=LOW/ERR），
  读该 cell 的 stdout（在报告里），判断是 LLM 故障 / budget 瞬耗 / 结构性 bug。
  **瞬时 LLM 故障（502/超时，已知模式见 q7-300-r2-dup-rootcause）→ 直接跑 resume 脚本补跑缺失 cell**：
  ```
  bash experiments/stage-ablation/tpr17-pilot-resume.sh
  ```
  它跳过已成功的 cell（n_nodes>=381 且 n_llm_calls>=50），只补跑缺失/退化的，
  单 cell 再失败不中止（继续跑下一个），跑完汇总 done/skip/fail。fail>0 时 rc=1 提示人工复查。
  **结构性 bug（runner 自身 crash / patch 错误）→ 先修 runner 再跑 resume**（resume 会重跑该 cell）。

## 1. 识别退化 cell（零进度伪装成成功）
sanity floor 只抓崩溃；零进度 run 会以 n_nodes=381 过 floor。逐个 cell 看：
```
python3 -c "
import json,glob
for f in sorted(glob.glob('modules/B-pipeline-ablation/data/tpr17/*_r3_r*.json')):
    d=json.load(open(f))
    flag='⚠️退化' if (d.get('n_llm_calls',0)<50 or d.get('tokens_total',0)<5000) else 'ok'
    print(f\"{flag} {d['arm']}/{d['rep']}: n={d['n_nodes']} llm={d.get('n_llm_calls')} tok={d.get('tokens_total')} depth={d.get('depth')}\")
"
```
正常 cell：n_nodes>381（应有 ~44 新节点）、n_llm_calls 数百、tokens 数万。
`⚠️退化` 的 cell 作废，不计入分析（在 runbook 记录作废原因）。

## 2. 一键分析
```
cd experiments/stage-ablation && python3 tpr17_analysis.py \
  --out ../modules/B-pipeline-ablation/data/tpr17 --checkpoints r3
```
产出 `tpr17_analysis.json`。

## 3. 解读（关键：power 注记优先）
- **主结论锚定 verified + parent_link**（n=5-10 高功效，见 power 决策表）。
- **depth 是 TOST 瓶颈**（n≤10 功效仅 20-42%）：
  - depth 判"不等效" → 先查 `power_note`，若 underpowered 则只能读作
    **"功效不足，无法排除序列影响"**，**不能**读作"序列有影响"。
  - depth 判"等效" → 同样受 power 限制，读作"在该功效下未检出 >Δ 的差异"。
- **operational_total_effect（verify-off vs canonical）是方向性的**（Welch/MWU+bootstrap，
  无 TOST）：显著 = verify 环节确有净效应；不显著 = 未检出，不等于"无效应"。
- **sequence_mechanism_effect（null-control vs canonical）用 TOST**：
  等效 = 乱序 state 块未产生 >Δ 的可测差异（序列位置本身无净效应）。

## 4. 落结论
把结论 + 作废 cell 清单 + power 注记写回
`modules/B-pipeline-ablation/data/tpr17/tpr17_design_notes.md`，commit。

## 已知判据（异常信号）
- 单 run >78min 无新落盘 = 可疑（正常 ~52min，相位感知）。
- 9 run 总 >10h 未完 = 查 vLLM 健康 + 首个 cell 日志。
- 任一臂 3 rep 全退化 = 该臂 patch 可能有结构性问题，回查 runner。
