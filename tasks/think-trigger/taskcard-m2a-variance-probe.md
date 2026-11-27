# origin: ai (M 线 M2a 方差探针任务卡, 2026-11-28)
# 目的: 零 GPU 判定 M3 对照实验 3 reps 是否有统计功效。方差过大→先 pilot; 方差小→直接 3 reps。
# 唯一指令来源=本卡。不要读其他项目文件做判断。

## 背景(只读, 不据此做额外判断)
M3 要跑 V0/V1 × 域 × reps 对照实验。跑前先确认: 已有数据的 rep 间方差多大? 若单指标 rep 间波动 > 效应量预期, 3 reps 测不出差异, 需先 pilot 或加 reps。

## 数据源(checkpoint, 只读)
基目录: /Users/a1-6/Desktop/workspace/pfb-thinkmech/experiments/stage-ablation/checkpoints/
- cyclone s0: sm-oood-cyclone-r1, sm-oood-cyclone-r2  (2 reps)
- cyclone s1: sm-oood-s1-cyclone-r1, sm-oood-s1-cyclone-r2  (2 reps)
- hw s0: sm-k3-S0-r1, sm-k3-S0-r2  (2 reps)
- hw s1: sm-k3-S1-r1  (1 rep, 只算单点)
每个 checkpoint 下: <node_id>/node.md (含 ## Claim 段) + meta.json。
先 ls 确认实际存在的 rep, 缺的如实标 missing, 不伪造。

## 三个诊断指标(定义来自 m2-injection-design-20261128.md §2, 此处复述, 以本卡为准)
对每个 arm 的每个 rep, 遍历所有 node.md 的 ## Claim 段, 算:
1. **量化 claim 密度** = 含(阿拉伯数字 或 数学符号 ∈{=,≥,≤,÷,×,%,℃,km,hPa,knot,节} 或 区间表达式)的节点数 / 总节点数
2. **域偏移率** = 域外机制词命中次数 / max(域内机制词命中次数,1)。词表(预注册, 直接用):
   - cyclone 域内{衰减,风眼,眼壁,角动量,潜热,边界层摩擦,洋热通量} 域外{非凸,landscape,梯度下降,损失面,相变,李雅普诺夫}
   - hw 域内{功耗,延迟,带宽,缓存,流水线,时钟,总线} 域外{非凸,landscape,梯度下降,损失面,相变}
3. **机制覆盖率(正则初筛)** = 同时命中≥2 个"机制三要素"的节点数 / 总节点数。三要素正则:
   - 参数变化: 含(变化|改变|增大|减小|升高|降低|中断|切断|增强|减弱)
   - 因果说明: 含(导致|引起|使得|造成|因为|由于|从而|进而)
   - 影响量: 含(数量级|量级|约|典型|平均|速率|强度|占比|百分比)
   (这是初筛, 不含人工核; 人工核是 M4 正式记分才做, 本探针只用正则)

## 执行(脚本落盘, 不走模型输出流)
写一个 Python 脚本 m2a_variance_probe.py 到 oood-probe/ 目录, 逻辑:
- 解析每个 checkpoint 的所有 node.md, 提取 ## Claim 段文本
- 对每 (arm, rep) 算上面 3 指标
- 输出 JSON 到 oood-probe/m2a-variance-probe.json:
  {
    "arms": { "<arm>": { "reps": { "<rep>": {n_nodes, quant_density, domain_drift_rate, mech_coverage} } ,
                        "metric_stats": { <metric>: {values:[...], mean, sd, cv(=sd/mean)} } } },
    "verdict": { "cyclone_reps_per_arm": 2, "largest_cv": <metric+值>, "power_risk": "low|medium|high" }
  }
  power_risk 判据: 任一指标 cv>0.3 → high; cv 0.15-0.3 → medium; 全 <0.15 → low。
- 脚本跑完 print 一行: 每 arm 每指标的 mean±sd + power_risk 结论

## 验收
1. m2a-variance-probe.json 存在且可 json.load, 含全部实际存在的 (arm,rep)
2. 脚本可重跑(幂等, 覆盖写)
3. 最终汇报 1 行: cyclone s0/s1 三指标 rep 间 cv 各多少, power_risk=? , json 路径, commit hash
4. commit 只 add 脚本 + json 两个文件

## 边界
- 零 GPU, 不调 8787, 不跑任何 SM 实验
- 不改任何既有文件, 只新增脚本+json
- 数据缺失如实标 missing, 不补数
- 若某 checkpoint 无 node.md 或结构不符, 跳过并在 JSON 标 parse_error, 不崩溃
