# T49: 新题 Gold Tree 构建（Q6 网络架构 + Q7 存储系统）

## 强制段
你是 LMArena agent，本任务只涉及 prompt-first-bench/main。先 git pull 获取最新代码。严格按仓库内 `loop/prompt-first/` 阶段执行（01→02→02.5→03→04→04.5）。产出落盘路径见【交付物】。通道故障报告 Lead 不得静默跳过。

## 【目标】
为 PFB-APPLY D 面（gold 复现门禁）构建 2 棵新题 gold tree：
- **Q6**: CDN vs 自建边缘节点 — 决定"每千请求的 P99 延迟成本"的所有因素
- **Q7**: SSD RAID vs NVMe vs 分布式对象存储 — 决定"每 TB 年有效容量成本"的所有因素

这两道题与现有 Q1-Q5（全部 AI/ML 领域）完全不同域，用于验证 pfb 流程的真实泛化能力。

## 【背景】
- 现有 gold tree: `bench/rubric-v3/ablation/gold-tree.md`（31 节点，Q1 域）
- 现有题目定义: `experiments/stage-ablation/ablation_harness.py` 中 QUESTIONS dict
- 新题需要：① 题面文件 ② gold tree ③ 加入 QUESTIONS 注册
- PFB-APPLY 计划: `tasks/PFB-APPLY-midterm-plan.md` §D

## 【SOP 索引】
- `loop/prompt-first/01-goal-decomposition.md`
- `loop/prompt-first/02-information-research.md`
- `bench/rubric-v3/ablation/gold-tree.md`（参考格式，内容必须独立推导）
- `experiments/stage-ablation/ablation_harness.py`（QUESTIONS 注册格式）

## 【实验设计】

### Q6: 网络架构选型
**题面**（写入 `bench/questions/Q6-network-arch.txt`）：
```
你是一个逻辑严密的拆解者。面对一个复杂问题，不要凭直觉直接列清单，要像整理文件夹一样，一层一层往下分，最后交出一棵树。

把整个问题先定成一个要算清楚的「根节点」——通常是一个数（比如「哪种方案最划算」，就拆成「每个方案的单任务成本」）。然后一层层往下切，每一层都把这个节点切成几个子文件夹。一直切到每一片「叶子」都是一个你要么能查到规格、要么能套公式、要么能实测出来的具体数字或区间为止。

下面这个任务，请按上面的方式拆（你手头没有现成规格，请自行调研或推理补齐缺口，并把你发现的关键因素都拆出来）：

我们运营一个面向 C 端用户的图片+短视频平台（日活 500 万，日均上传 200GB，日均下载 2TB）。我在纠结三种 CDN 策略：全用公有云 CDN（阿里云/Cloudflare）、自建边缘节点（10 个 POP 点）、或者混合（核心区域自建+长尾走公有云）。
请帮我拆解：决定「每千请求的 P99 延迟成本（含基础设施+带宽+运维）」的所有因素都有哪些，并判断哪个策略最划算。
```

### Q7: 存储系统选型
**题面**（写入 `bench/questions/Q7-storage-arch.txt`）：
```
你是一个逻辑严密的拆解者。面对一个复杂问题，不要凭直觉直接列清单，要像整理文件夹一样，一层一层往下分，最后交出一棵树。

把整个问题先定成一个要算清楚的「根节点」——通常是一个数（比如「哪种方案最划算」，就拆成「每个方案的单任务成本」）。然后一层层往下切，每一层都把这个节点切成几个子文件夹。一直切到每一片「叶子」都是一个你要么能查到规格、要么能套公式、要么能实测出来的具体数字或区间为止。

下面这个任务，请按上面的方式拆（你手头没有现成规格，请自行调研或推理补齐缺口，并把你发现的关键因素都拆出来）：

我们有一个内部数据湖，总数据量约 500TB（其中 80% 是冷数据，极少访问；20% 是温数据，每天扫描 1-2 次）。我在纠结三种存储方案：本地 NVMe SSD 阵列、HDD+SSD 分层（热数据 SSD 冷数据 HDD）、或者云上对象存储（S3/OSS 生命周期策略）。
请帮我拆解：决定「每 TB 年有效可用容量成本（含硬件/云服务费+电力+运维+数据恢复 RTO 代价）」的所有因素都有哪些，并判断哪个方案最划算。
```

### Gold Tree 构建
对每道新题：
1. 独立调研（搜索预算不设上限，直到每个分支都有带来源的证据或显式黑盒声明）
2. 按 gold-tree.md 相同格式输出树形结构（根→子→叶，每节点标 SHARE + 可查/可调/黑盒 + 量法）
3. 所有数值和判断必须来自你自己的调研，不得引用既有 gold-tree.md 中的任何数值
4. 产出：
   - `bench/questions/Q6-network-arch.txt`（题面）
   - `bench/questions/Q7-storage-arch.txt`（题面）
   - `bench/rubric-v3/ablation/gold-Q6.md`（gold tree，≥50 行，≥3 层深度，≥8 叶子）
   - `bench/rubric-v3/ablation/gold-Q7.md`（gold tree，≥50 行，≥3 层深度，≥8 叶子）

### QUESTIONS 注册
在 `experiments/stage-ablation/ablation_harness.py` 的 QUESTIONS dict 中追加：
```python
"Q6": {"prompt_file": "bench/questions/Q6-network-arch.txt", "domain": "networking"},
"Q7": {"prompt_file": "bench/questions/Q7-storage-arch.txt", "domain": "storage"},
```

## 【验收标准】
- [ ] Q6/Q7 题面文件存在且非空（≥20 行）
- [ ] gold-Q6.md / gold-Q7.md 存在且 ≥50 行
- [ ] 树结构完整：有根节点、≥3 层深度、≥8 个叶子
- [ ] 每个叶子节点标注了证据来源（URL/文档名）或显式"黑盒"声明
- [ ] QUESTIONS dict 已更新（grep Q6/Q7 可找到）
- [ ] 两棵 gold tree 的域名与 Q1-Q5 无重叠（networking/storage vs AI/ML）

## 【禁止】
- 不得引用 gold-tree.md（Q1）中的任何数值
- 不得编造 URL 或数据源——查不到就标"黑盒"
- 不得修改 Q1-Q5 的任何文件