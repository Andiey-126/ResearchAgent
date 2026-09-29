# 05 · Research Agent(多 agent 研究系统)· 项目文档

> 建档:2026-09-28 · 最后修订:2026-09-28(源码复读 + 官方文档核对后定稿教学计划,修正第五、六、八节)
> 所属:Agent 学习项目
> 对应路线图:**模块五 · 任务分解(LeadResearcher + Subagent)**

---

## 一、项目定位

用 Claude Agent SDK 从零实现一个多 agent 研究系统:一个主 agent 把研究问题拆成若干子课题,并行派多个研究员子 agent 上网搜索,最后由写报告的子 agent 汇总成报告。

**为什么是这个项目**

- 这是 Anthropic 工程博客《How we built our multi-agent research system》的缩小版实现,而这篇博客正是路线图模块五指定的阅读资料
- 全程终端运行,除 SDK 内置的 WebSearch 外**零网络配置**,不涉及前后端,注意力可以全部放在 agent 机制上
- 有官方实现可以当参考答案

**学习要求**:自己设计、自己写,官方 demo 只作为写完之后对照的"参考答案"。

---

## 二、参考源

| 项 | 内容 |
|---|---|
| 仓库 | https://github.com/anthropics/claude-agent-sdk-demos |
| 子目录 | [`research-agent/`](https://github.com/anthropics/claude-agent-sdk-demos/tree/main/research-agent) |
| 下载版本 | commit `826b268506a5f3707623c9e6140b200befcbebae`(仓库 HEAD,2026-03-13;下载日期 2026-09-28)。**2026-09-28 已核对:本地副本与上游 HEAD 的 `research_agent/` 逐文件一致** |
| research-agent 最后改动 | commit `fe8ae13`,**2025-12-11**(美西时间,即悉尼 12-12)。距下载约 9.5 个月,部分写法已过时,见第六节 |
| 本地位置 | `./example_program/` |
| 许可证 | 仓库**未声明 license**(GitHub API 返回 none),默认保留版权。**本地学习可以,但 `example_program/` 不要推到公开仓库**。以后 `git init` 时记得加进 `.gitignore` |
| 本地环境 | `claude-agent-sdk` **0.2.148**(内置 Claude Code CLI **2.1.251**),conda 环境 `claude_agent_sdk`。第六、八节里所有版本门槛均已满足 |

### demo 的结构

```
example_program/
├── research_agent/
│   ├── agent.py                  # 入口:定义 3 个子 agent + hooks + ClaudeSDKClient 会话循环
│   ├── prompts/                  # 四个角色的系统 prompt(约 26KB,项目的真正"内容"在这里)
│   │   ├── lead_agent.txt
│   │   ├── researcher.txt
│   │   ├── data_analyst.txt
│   │   └── report_writer.txt
│   └── utils/
│       ├── subagent_tracker.py   # 用 hooks 把工具调用归属到具体子 agent(约 280 行,已过时)
│       ├── message_handler.py    # 从消息流里识别"派出子 agent"事件
│       └── transcript.py         # 控制台 + 文件双写日志
└── .claude/
    ├── skills/                   # pdf、executive-briefing 两个 skill
    └── commands/                 # /research 等斜杠命令
```

### demo 的工作流

| 角色 | 工具 | 职责 |
|---|---|---|
| 主 agent(lead) | prompt 声称"只有 `Task`",**实际并非如此**(见第五节 B) | 把问题拆成 2–4 个子课题,派子 agent,本身不做任何研究 |
| researcher | `WebSearch`, `Write` | 搜 5–10 次,把笔记写到 `files/research_notes/` |
| data-analyst | `Glob`, `Read`, `Bash`, `Write` | 读笔记,用 matplotlib 画图,输出到 `files/charts/` 和 `files/data/` |
| report-writer | `Skill`, `Write`, `Glob`, `Read`, `Bash` | 读以上全部产物,用 reportlab 生成 PDF,输出到 `files/reports/` |

**demo 里没有任何自定义工具**,全部是 SDK 内置工具。这个项目练的不是"写工具",而是**编排**。

---

## 三、学习方式

**用 `structured-coding-tutor` skill,demo 当参考答案,不跟着敲。**

每个知识点先判断走哪条路径:

| 路径 | 用于 | 做法 |
|---|---|---|
| 辅助 | 脚手架、日志写入、prompt 文件加载 | 原理 → 示范代码 → 代码讲解 → 任务,一次输出完成;也可以 vibe coding |
| 核心·无设计空间 | 固定写法的配置(字段名、环境变量名) | 原理 → 代码思路 → 任务。不给示范代码,但**精确的 API / 字段名直接给**,组装逻辑自己想 |
| 核心·有设计空间 | 背后有"有人面对问题想出解法"的机制 | **两轮**。第一轮:只讲约束事实 → 抛一个问题 → 停,等我先给出自己的方案;之后反馈 → 引出真正机制 → 具体场景走一遍 → 我用自己的话复述。复述过关才进第二轮:代码思路 → 任务 |

**所有路径通用**

- 批改单独一轮,**只基于真实运行结果**
- 一次只讲一个知识点
- 代码全英文、必须有注释
- 技术细节先查当前官方文档,给链接,分清"必须这样"和"建议这样"
- 调试靠证据
- 设计选择由老师给出有依据的推荐
- **从最底层出发**:新概念先讲清前因后果,再给用法;不甩出没见过、没交代来历的东西(文件、配置、工具)
- **架构按需生长**:默认一切从零开始。目录、配置文件、ignore 规则等结构,只在某个知识点第一次真正需要它时才加,不因为"看过 demo 知道以后会用到"就提前搭好
- **每个知识点写完、跑通之后**,再去翻 demo 对应部分,对比差异:哪里不一样、为什么、谁的更好、demo 哪里已经过时
- 技术细节以当前官方文档为准,不以 demo 为准
- 每个阶段结束做一次测验,题目取自这个阶段真实发生过的决策和 bug,干扰项长度与正确答案对齐

**为什么不跟着 demo 敲**

- demo 有多处过时写法,照抄会写出"不报错但悄悄失效"的代码
- demo 开着 `bypassPermissions`,掩盖了权限层面的真实问题(见第五节 B),照抄等于跳过这一课
- 项目的分量在 prompt 和设计判断上(Python 仅约 500 行),抄一遍学不到"为什么这样设计"

**目录约定**

- `example_program/`:只读参考,不修改
- 我自己的代码:写在本目录(`05_ResearchAgent/`)下,结构自己设计

---

## 四、第一版范围、教学阶段与知识点

**核心(所有知识点都从这一条派生)**:主 agent 只能通过派单工具委派任务;子 agent 唯一能看到的,是派单时写的那段话(加上它自己的系统 prompt)。它看不到主 agent 的对话历史,干完活也只有最后一条消息会回到主 agent。
> 官方原话:"The only content you pass from parent to subagent is the Agent tool's prompt string";"only its final message returns to the parent"。

**第一版范围**:主 agent → 2–3 个研究员并行搜索 → 写报告的子 agent 汇总成一份 **markdown 报告**,写入 `files/reports/`。

**砍掉的部分**:data-analyst(画图)、PDF 生成、skills、斜杠命令、CitationAgent、Prompt Injection 防护代码(只讨论风险)、评估(留到模块七)、LeadResearcher 把方案存入 Memory(原因见第七节)。

### 阶段 0 · 准备(辅助,不计入知识点)

- SDK 版本确认 ✅(0.2.148 / CLI 2.1.251)
- 0.1 密钥与版本控制:`.env` + `.gitignore`(只忽略此刻已经存在、必须忽略的东西)+ git init
- 0.2 第一个能跑的最小程序:单文件,一个 agent,**从第一次运行起就设 `max_budget_usd`,开发阶段一律 haiku**(完整讲解在知识点 7)。**走核心·有设计空间路径(两轮)**:设计题是"agent 循环跑在 CLI 子进程里,Python 怎么知道里面发生了什么"(2026-09-29 从辅助路径改过来,见 issue.md 第 4 条)
- 其余结构(包目录、prompt 文件夹、运行产物目录及对应 ignore 规则等)一律等到对应知识点真正需要时再加

### 阶段一 · 两层结构与交接

| # | 知识点 | 路径 | 完成标志 | 对照 demo 看什么 |
|---|---|---|---|---|
| 1 | 最小两层结构:主 agent + 1 个研究员。包括两个必须知道的事实:`AgentDefinition.tools` 只管"看得见哪些工具",不管"要不要批准";批准是整个会话共享的 `allowed_tools`,所以子 agent 要用的工具也得放进去 | 有设计空间 | 亲眼看到 `Agent` 工具被调用、消息上带着 `parent_tool_use_id`,**不开 bypass 也能跑通** | `agent.py` 的 `allowed_tools=["Task"]` + `bypassPermissions` 为什么在 demo 里"能跑" |
| 2 | 派单契约:目标、输出格式、该用的工具和信息源、任务边界;`description` 本身就是路由 prompt | 有设计空间 | 子 agent 只凭派单那段话就能正确完成任务 | lead prompt 的 `<task_tool_usage>`:只写了"subtopic",缺了哪几要素 |
| 3 | 用文件交接,而不是层层转述 | 有设计空间 | 研究员把笔记写到约定路径,主 agent 只收到简短回执 | researcher prompt 的 `<file_workflow>` STEP 4 |

→ 阶段一测验

### 阶段二 · 并行与可观测

| # | 知识点 | 路径 | 完成标志 | 对照 demo 看什么 |
|---|---|---|---|---|
| 4 | 并行派 2–4 个研究员:怎么拆、派几个、后台运行时主 agent 怎么等 | 有设计空间 + 实测 | **实测**主 agent 能拿到所有研究员的结果(第八节盲区 2) | lead prompt "STEP 3: WAIT" 在后台默认下是否还成立 |
| 5 | 记录谁干了什么:hook 自带 `agent_id` + `SubagentStart/Stop`,写 JSONL(日志写入部分走辅助路径) | 机制有设计空间 | 每次工具调用都正确归到对应子 agent;**并能看出主 agent 有没有偷偷用 WebSearch** | `subagent_tracker.py` 用全局变量推算归属,并行时为什么可能记错 |

→ 阶段二测验

### 阶段三 · 护栏与汇总

| # | 知识点 | 路径 | 完成标志 | 对照 demo 看什么 |
|---|---|---|---|---|
| 6 | 按角色强制分工:主 agent 看得见也被批准了 WebSearch/Write(知识点 1 留下的口子),怎么让它真的用不了,而研究员照常能用 | 有设计空间 | 主 agent 调 WebSearch 被拒,研究员不受影响 | demo 只靠 prompt 里的 "You NEVER research" |
| 7 | 三个上限:花费、嵌套深度、并发数 | 核心·无设计空间 | 三个上限全部生效,能说出各自默认值和触发后的表现 | demo 一个都没设 |
| 8 | 写报告的子 agent:串行、只读笔记、不能上网,输出带来源链接的 markdown | 有设计空间 | 输出报告,**第一版完成标准达成** | `report_writer.txt`;博客里单独的 CitationAgent |

→ 阶段三测验

### 阶段四 · 复盘

| # | 内容 | 完成标志 |
|---|---|---|
| 9 | 与 demo 整体对比 | 写一份差异记录,更新第十一节踩坑记录 |

**完成标准**:在终端输入一个研究问题,能自动产出一份带来源链接的 markdown 报告;tool_calls 日志能看清每个子 agent 做了什么;设了花费上限。做到这一步就收尾,不再打磨。

---

## 五、能学到的 agent 理念与知识点

### A. 多 agent 编排(核心,模块五)

| 知识点 | demo 里的位置 | 要点 |
|---|---|---|
| 主 agent 加子 agent 的分工模式(orchestrator-workers) | lead prompt 写着 "You NEVER research" / "Your ONLY tool is Task" | 主 agent 只拆解和协调,不亲自干活。**更正**:demo 里这个分工**只靠 prompt 维持,不是工具权限强制的**(见 B);真正的强制是知识点 6 |
| 上下文隔离 | `AgentDefinition.prompt` + 派单时的那段话 | 子 agent 看不到主 agent 的历史和系统 prompt;子 agent 中间的搜索过程不会回流,只有最后一条消息会回去。子 agent 本质是**上下文压缩器** |
| 派单契约 | lead prompt 的 `<task_tool_usage>` | 博客四要素:目标、输出格式、该用哪些工具和信息源、任务边界。缺了会重复干活、留下空白、找不到该找的东西。demo 给研究员的派单只要求写"detailed instructions on what specific angle",四要素没有显式要求 |
| 任务分解,按复杂度调整规模 | demo 写死 2–4 个研究员 | 博客:简单事实查询 1 个 agent、3–10 次调用;直接对比类 2–4 个子 agent、每个 10–15 次调用;复杂研究 10 个以上且分工清晰。早期的坑:简单问题也派一大堆 |
| 并行与串行 | 研究员并行;分析 → 写报告串行 | 有依赖的步骤只能串行。博客的两层并行:主 agent 同时起 3–5 个子 agent,子 agent 同时发 3 个以上工具调用,研究耗时最多降 90%。博客也承认主 agent 同步等待一批子 agent 是信息流瓶颈 |
| 用文件交接,而不是层层转述 | `files/research_notes/` → `data/` → `reports/` | 博客:子 agent 产出可以绕过协调者直接落地,避免"传话游戏"式失真,也省掉在对话历史里搬运全文的 token |
| 搜索策略 | researcher prompt 的 `<search_strategy>` | 博客:先用短而宽的查询摸清全貌,再逐步收窄。demo 反而一上来就要求"data-focused queries",并附带数量指标(见第八节 4) |

**workflow 还是 agent?** demo 的执行顺序被 prompt 写死了(研究 → 分析 → 写报告),真正由模型决定的只有:主 agent 拆成哪几个子课题、研究员搜什么以及什么时候停。这是"**固定流程骨架加上有自主性的 agent 节点**"的混合体。自己的版本要把多少控制权交给模型,是一个设计决定。

### B. 多 agent 场景下的权限(2026-09-28 按官方文档重写)

- **两个维度要分开**(和 Obsidian 项目里 `tools` vs `allowed_tools` 是同一类问题):
  - **看得见**:`AgentDefinition.tools` 决定子 agent 看得见哪些工具。子 agent 的工具从主会话继承,再按 `tools` 收窄;**主会话层面对工具的限制(`--tools` / deny 规则)会传递给子 agent**。所以不能靠"主 agent 只看得见 `Agent`"来强制分工,那样研究员也就看不见 WebSearch 了
  - **要不要批准**:`allowed_tools` 是**整个会话共享**的批准名单。子 agent 要用的 WebSearch / Write 如果不在里面,又没开 bypass,调用就走到权限模式和 `canUseTool`,headless 下跑不下去。**demo 的 `allowed_tools=["Task"]` 能跑,完全是因为开了 `bypassPermissions`**
- **推论**:把 WebSearch 放进 `allowed_tools` 之后,主 agent 在技术上也能搜。要按角色强制分工,得在更早的一层拦:PreToolUse hook 在权限流程**最先**运行,而 hook 输入里的 `agent_id` **只在子 agent 内部触发时才有值**,主 agent 的调用没有。这是知识点 6 的设计题
- **子 agent 权限模式继承**:子 agent 默认跑在主会话的权限模式里。主会话开 `bypassPermissions`,所有子 agent 一起 bypass。demo 用 `bypassPermissions` + 两个子 agent 开着 Bash,是**反面教材**
- **模型分层**:demo 全部用 haiku;博客用 Opus 当主 agent + Sonnet 当子 agent,是能力和成本之间的取舍

### C. 多 agent 场景下的可观测性

多个 agent 并行时会冒出新问题:**这次工具调用是谁发起的?** 涉及 hooks、`parent_tool_use_id`、结构化 JSONL 日志。demo 的解法已过时,但问题本身真实存在。

### D. 成本意识

- 普通 agent 消耗的 token 约为普通对话的 **4 倍**,多 agent 约为 **15 倍**
- 博客评测中,**光 token 用量就解释了 80% 的效果差异**
- 多 agent 的本质是"花更多 token 换更好的结果",只有任务价值撑得起才值得用
- 实操:`max_budget_usd`,以及嵌套深度、并发数上限。**默认值:深度 3 层、并发 20 个、花费不设上限**,所以必须自己设

### E. 给 agent 写 prompt

- `description` 字段本身就是一段路由 prompt,主 agent 靠它判断派谁
- 系统 prompt 的分块结构:角色 / 流程 / 规则 / 正反例子
- 防止凭记忆作答:研究员被要求"只用搜索结果"
- **few-shot 例子本身会带偏**:researcher prompt 的 "GOOD" 示例里全是编造的数字,还混进了一条和主题无关的 "Mobile booking share: 63% of all reservations"。示例在教模型"数字多就是好",没在教"数字要真"
- 可以批判地看:demo 大量使用 CRITICAL / NEVER 这类强硬措辞,较新模型的 prompt 指南据说建议少用(**未重新查证**,到时查当前版本)
- 博客的两条 prompt 经验:"像你的 agent 一样思考"(逐步看它怎么干活)、"让 agent 帮你改 prompt"(把失败案例交给模型诊断)

### F. Prompt Injection 在 agent 之间传播(demo 没处理)

研究员读的网页是不可信输入 → 藏在里面的指令会被写进研究笔记 → 被写报告的子 agent 读到,**一层层往下传**。当前 SDK(CLI v2.1.210 起)会扫描子 agent 最终回复里像指令的内容,但只是加标记、中和掉伪造的控制标签,不删改内容,只能算一层防线。而且它只扫子 agent 的**最终回复**,不扫写进文件的笔记;我们用文件交接,笔记这条路不在扫描范围内。

### G. Skills 与斜杠命令(可选)

`.claude/skills/`、`.claude/commands/`,通过 `setting_sources=["project"]` 加载,体现"能力按需加载"的思路。不在第一版范围内。

---

## 六、demo 过时点与问题清单(已对照 2026-09 官方文档)

| 位置 | 问题 | 后果 |
|---|---|---|
| `message_handler.py`:`if block.name == 'Task'` | 派单工具在 `tool_use` 块里已改名为 `"Agent"`(Claude Code v2.1.63 起);`system:init` 工具列表里仍叫 `"Task"`。文档建议两个名字都匹配 | 不报错但悄悄失效:识别不到子 agent 被派出,所有子 agent 的调用都被记到 MAIN AGENT 名下 |
| `subagent_tracker.py` 第 219 行:`elif tool_name != 'Task'` | 同上,主 agent 的派单调用现在叫 `Agent`,这个过滤条件失效 | 主 agent 的每次派单都会被额外记成一条 MAIN AGENT 工具调用 |
| `agent.py`:`allowed_tools=["Task"]` | 当前文档示例写的是 `"Agent"`;旧名还能不能用**需实测** | 被 bypass 掩盖,见下一行 |
| `agent.py`:`permission_mode="bypassPermissions"` | ① 两个子 agent 开着 Bash 且无需确认;② 掩盖了"子 agent 的 WebSearch/Write 也需要被批准"这件事;③ `allowed_tools` 在 bypass 下不起限制作用 | 安全反面教材;去掉 bypass 后 demo 原样很可能跑不通 |
| lead prompt:"Your ONLY tool is Task" | 主 agent 没设任何工具限制,实际看得见全部内置工具,bypass 下也全部可用 | 分工只靠 prompt 维持 |
| `subagent_tracker.py`:用全局变量 `_current_parent_id` 推断是谁在调用 | 现在 hook 输入里直接带 `agent_id` / `agent_type`(Python 里是 PreToolUse、PostToolUse 等的可选字段),还有 `SubagentStart` / `SubagentStop` 事件 | 整套间接推算没必要了;并行时可能记错人(这一点是推断,知识点 5 实测) |
| lead prompt:"等所有研究员完成" | 子 agent 现在**默认后台运行**(CLI v2.1.198 起);后台子 agent 的结果以"完成通知"的形式在**之后的某一轮**才到达主 agent | 主 agent 能否正确等待,**需实测** |
| 各 prompt | 写死"优先 2024–2025 数据",示例文件名是 20251110 | 搜索结果的时效会偏旧 |
| data_analyst prompt:`python3 << 'EOF'` | Windows 上不一定有 `python3` 命令,PowerShell 也不支持 heredoc | 画图步骤可能失败(第一版已砍掉这部分) |

---

## 七、涉及与未涉及的知识点

**涉及**

| 知识点 | 覆盖程度 |
|---|---|
| 任务分解(LeadResearcher + Subagent) | ✅ 完整覆盖,这是主菜 |
| Just-in-time retrieval(概念层面) | ✅ 运行时按需搜索,而不是事先建索引 |
| 多 agent 的权限划分 | ✅ 可见性 vs 批准、会话共享批准、hook 按角色强制 |
| 多 agent 的可观测性 | ✅ 调用归属、结构化日志 |
| 成本控制 | ✅ 花费、深度、并发上限 |
| Prompt Injection 防御 | 🟡 问题真实存在,但只有自己加防护才算学到,demo 没有 |
| Context Window 管理 | 🟡 部分覆盖:学到用子 agent 隔离、用文件交接;学不到压缩、清理这类手段 |
| Agent 评估 | 🟡 可作为延伸(博客做法:约 20 个典型问题 + 模型当评委打 0–1 分 + 人工检查),但路线图规定先学完模块七的方法论,**不提前做** |

**未涉及**:经典 RAG / Contextual Retrieval、Memory Tool、Context Editing、执行规划(初始化 + 增量执行)、独立 stdio MCP server、ReAct / Reflexion 的显式实现、agent 循环本身(被 SDK 封装)。

**关于路线图模块五写的"主 agent 先想方案存入 Memory"**:博客里 LeadResearcher 这么做的原因是"上下文超过 200,000 token 会被截断",存下方案是为了不丢方向。我们的主 agent 只收到几条简短回执,上下文远到不了这个量级,硬加就是编一个假需求。而且这件事的机制本身属于模块四(工作记忆)。**第一版不做**,留给以后真撞上长任务时再加。

---

## 八、盲区与风险

1. ~~**SDK 版本未确认**~~ **已确认(2026-09-28)**:`claude-agent-sdk` 0.2.148,内置 CLI 2.1.251。`Agent` 改名(2.1.63)、后台默认(2.1.198)、输出扫描(2.1.210)、三个上限(SDK 0.2.127 / CLI 2.1.219)、hook 里的 `agent_id`(SDK 0.1.46)全部可用
2. **后台运行下的等待行为**:文档说后台子 agent 的结果以完成通知的形式在之后某一轮到达,主 agent 需要结果时会自己设 `run_in_background: false`。但这是模型的判断,不是保证;`client.receive_response()` 结束时研究员是否还在跑、结果怎么回到主 agent,**必须实测**(知识点 4)
3. **成本**:WebSearch 按次额外计费,加上多 agent 约 15 倍的 token 消耗,且研究员是并行的。**从第一次运行起就设 `max_budget_usd`**,开发阶段用 haiku
4. **研究质量可能是"凑出来的"**:demo 要求每份笔记"至少 10–15 个数字",few-shot 示例里的数字本身也是编的(见第五节 E)。这种数量指标可能诱导模型凑数甚至编造。自己的版本要考虑:数量要求会不会伤害真实性?来源链接要不要抽查?
5. **没有评估就没法判断"好不好"**:第一版只能人工看报告。要意识到这是主观判断,真正的评估留到模块七
6. **跨 agent 的注入传播**:见第五节 F。网页内容 → 笔记 → 报告,每经过一层,来源就更难追溯;SDK 的扫描覆盖不到文件
7. **相对路径依赖运行目录**:`files/...` 路径和 `setting_sources=["project"]` 都相对于 cwd 解析,从别的目录启动会出错
8. **范围蔓延**:画图、PDF、skills、斜杠命令都很诱人,但都是辅助功能。第一版不做
9. **用研究代替行动**:参考资料就是这篇博客、官方 subagents / hooks / permissions 文档和 demo 本身,够了,不再扩展比较别的仓库
10. **许可证**:`example_program/` 没有 license,不要公开发布
11. **(新增)第一次运行就会撞上权限**:不开 bypass,`allowed_tools` 里又只放 `Agent`,研究员的 WebSearch / Write 会卡在权限上。知识点 1 必须先处理

---

## 九、参考资料

- [Anthropic · How we built our multi-agent research system](https://www.anthropic.com/engineering/multi-agent-research-system):设计理念与数据来源
- [Agent SDK · Subagents](https://code.claude.com/docs/en/agent-sdk/subagents):`AgentDefinition`、派单工具名、上下文继承、三个上限
- [Claude Code · Subagents](https://code.claude.com/docs/en/sub-agents):子 agent 的可用工具、前台 / 后台运行与结果送达
- [Agent SDK · Hooks](https://code.claude.com/docs/en/agent-sdk/hooks):`agent_id` / `agent_type`、`SubagentStart` / `SubagentStop`、`permissionDecision`
- [Agent SDK · Permissions](https://code.claude.com/docs/en/agent-sdk/permissions):权限评估顺序、`allowed_tools` 语义、子 agent 权限模式继承
- [claude-agent-sdk-python CHANGELOG](https://github.com/anthropics/claude-agent-sdk-python/blob/main/CHANGELOG.md):各功能对应的 SDK 版本

---

## 十、进度记录

| 日期 | 进度 | 备注 |
|---|---|---|
| 2026-09-28 | 选定项目,下载 demo,读完源码,建立本文档 | — |
| 2026-09-28 | 确认 SDK 版本 0.2.148 / CLI 2.1.251;复读 demo 全部源码并与上游核对一致;对照官方 subagents / hooks / permissions 文档定稿教学计划(第四节),修正第五、六、八节 | 下一步:阶段 0(脚手架)→ 知识点 1 |
| 2026-09-29 | 阶段 0 第一版被推翻重来:一上来给了完整骨架和 `pyproject.toml`,违反"从最底层出发"和"架构按需生长";两条原则已写进第三节 | 重新从 0.1 开始 |
| 2026-09-29 | 0.1 完成(首次 commit);0.2 改为两轮教学 | 0.2 第一轮原理进行中 |

---

## 十一、踩坑记录

(做的过程中追加)
