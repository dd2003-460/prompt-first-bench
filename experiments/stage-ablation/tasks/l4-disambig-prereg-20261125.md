# L4 消歧义重跑：预注册（2026-11-25，跑前冻结）

> origin: ai · 判别实验，预注册防事后调判据。
> 目的：判别 H1 残留的精确机制——**候选生成缺口**（模型能推理但不生成 4 卡候选）vs **推理能力缺口**（给了 4 卡候选也推不出）。
> 上游判决：`tasks/l4-audit-design-20261125.md` 判决第 4 条（H3b 主导 + TCO 定量复核）。

## 设计（单 run，budget 300，vLLM 空闲时跑）

- 题面：`experiments/stage-ablation/l4-disambig-question.txt`（消歧义版）
- 相对原题面（`s8b_pilot.py` QUESTIONS['gpu']）的三处消歧：
  1. 上下文 32K 下限 → **64K 定值**（gold 锚）
  2. 候选"自行搜索" → **固定 5 类**（3090/V100/M2Ultra/L40S/A100，gold 候选集）
  3. 目标函数"性价比最优"（宽）→ **c_pass [¢/task] 固定口径**（gold 口径）
- **关键设计：卡数留自由变量（1-8），不把 3090×4 写进题面**——防鹦鹉学舌污染。题面只中立声明"1-8 张均在评估范围内，卡数由 c_pass 推导决定"，不点名 4 卡、不暗示避开 1-2 卡（初稿曾写"四卡必须评估、不要只考虑 1-2 张"，会 prime 4 卡、直接污染本实验要测的量，已修正）。模型若自己推出 4 卡，才证明缺口在候选生成而非推理。
- 命令（pilot 释放 vLLM 后）：
  ```bash
  cd /Users/a1-6/Desktop/workspace/pfb/experiments/stage-ablation
  SM_SEED=42 SM_SYNTH_FULL=1 python3 -u s5_state_machine.py l4-disambig \
    --qid=l4-disambig --question-file l4-disambig-question.txt \
    --obj-mode=formula --synth --max-nodes 300 --max-depth 5
  ```
  产物：`runs-s5-sm-l4-disambig.json` + `-synth.json` + `checkpoints/`。

## 预注册判读（跑前冻结，不许事后改）

| 结果 | 判读 | 含义 |
|---|---|---|
| **A**：结论区出现 4 卡配置（任意卡型×4，regex 口径同 l4_check） | 候选生成缺口坐实 | 给足候选+口径后模型能到 4 卡 → L4 0/21 主因 = 原题面框架 prime ≤2 卡 + 候选自搜。可修：prompt 层补候选枚举。H1 关闭。 |
| **B**：结论区仍是 1-2 卡（含 2×3090） | 更深机制 | 消歧后仍不到 4 卡 → 缺口不止候选生成，还有口径内推理/权衡（H1-lite 复活）。下一步：oracle-parent（O2）看 gold 约束传递能否带到。 |
| **C**：出现 4 卡但非 3090（如 A100×4） | 部分 A | 候选生成 OK、卡型选择仍有偏差 → 口径/规格细节问题，比 A 弱一档。 |
| **D**：run 失败/无结论区 | 无效 | 重跑一次（换 seed 或 budget 150），仍失败则记 artifact 不判读。 |

**次级观测**（不影响主判读，记录备查）：
- 树内 4 卡候选节点数（decompose 侧是否生成）
- 64K 锚是否被遵守（KV 计算用 64K 还是又退回 32K）
- c_pass 口径是否被遵守（answer 里是否出现 ¢/task 计算）
- cov 分数 vs 原 K7 300 档（0.2885-0.3462 区间）——消歧后 cov 是否显著抬升（construct-mismatch 定量贡献的直接测量）

## 成本与风险

- 1 run × budget 300 ≈ 40-60 min（K7 300 档实测），vLLM 独占，不与 pilot 并发（502 风险，已知失败模式 q7-300-r2-dup-rootcause）。
- 排期：T-PR-17 pilot（PID 53387）DONE 后立即跑，或 vLLM 确认空闲时插入。
- 不碰 s5_state_machine.py 源码（pilot 期间冻结），只用现成 --question-file 机制。
