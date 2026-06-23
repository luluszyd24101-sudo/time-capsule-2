# 🖥️ Windows 性能诊断与清理报告

**生成时间**: 2026/06/22  
**系统**: Windows 10 专业版 (Build 18362)  
**设备**: Lenovo (Intel Core i5-8265U, 8GB RAM, Samsung 512GB NVMe SSD)

---

## 📊 一、硬件资源概况

| 组件 | 规格 | 当前状态 | 评估 |
|------|------|----------|------|
| **CPU** | i5-8265U (4核8线程, 1.60GHz) | 使用率 8%（空闲） | ✅ 正常 |
| **内存** | 7.8 GB | 已用 **5.3 GB (67.9%)**，剩余 **2.5 GB** | ⚠️ 紧张 |
| **系统盘(C:)** | 60 GB 分区 | 已用 **47.2 GB (78.6%)**，剩余 **12.8 GB** | 🔴 **明显不足** |
| **D:** | 137 GB | 已用 15 GB (11%) | ✅ 充足 |
| **E:** | 138 GB | 已用 **105.2 GB (76.2%)** | ⚠️ 较满 |
| **F:** | 142 GB | 已用 6 GB (4%) | ✅ 充足 |
| **运行时间** | — | 1 天 6 小时 | ✅ 正常 |
| **运行进程数** | — | **205 个** | 🔴 **过多** |
| **运行服务数** | — | **109 个** | ⚠️ 偏多 |
| **待安装更新** | — | **8 个** | ⚠️ 有积压 |

---

## 🔥 二、主要瓶颈分析

### 1️⃣ 内存不足（最严重的问题）

仅有 **7.8 GB 可用内存**，当前使用率 **67.9%**，这是电脑变慢的主要原因。以下进程消耗内存最多：

| 进程 | 内存占用 | 说明 |
|------|---------|------|
| QQ (×4个进程) | **~825 MB** | 腾讯QQ多实例 |
| Quark (夸克) (×4个进程) | **~740 MB** | 夸克浏览器多进程 |
| Claude Code | ~415 MB | 当前运行的AI工具 |
| Chrome | ~174 MB | 谷歌浏览器 |
| QQEX (腾讯) | ~166 MB | 相关组件 |
| QQPCTray | ~158 MB | QQ托盘 |
| explorer | ~202 MB | 资源管理器 |
| QQPCRTP (服务) | ~97 MB | QQ安全服务 |

> **结论**: QQ + 夸克浏览器 合计占用了 **>1.5 GB** 内存。8GB内存对于这些应用来说严重不足。

### 2️⃣ C 盘空间不足（严重问题）

C 盘仅 **60 GB**，已用 **78.6%**。Windows 系统盘低于 15% 剩余空间会显著影响性能。

**C 盘空间占用分布：**

| 目录 | 大小 | 说明 |
|------|------|------|
| `C:\Windows` | **17.98 GB** | 系统文件 |
| ├─ WinSxS | 6.46 GB | 系统组件存储（可通过DISM清理） |
| └─ DriverStore | 3.98 GB | 驱动程序存储 |
| `C:\Users` | **12.12 GB** | 用户数据 |
| ├─ AppData\Local\kingsoft | 2.68 GB | WPS Office 缓存/数据 |
| ├─ AppData\Local\Programs\Quark | 2.51 GB | 夸克浏览器（含旧版本） |
| ├─ npm-cache | 0.80 GB | npm 包缓存 |
| ├─ Roaming\kingsoft | 0.93 GB | WPS Office 配置 |
| ├─ Roaming\360se6 | 0.74 GB | 360浏览器数据 |
| ├─ Roaming\Tencent\QQ | 0.70 GB | QQ数据 |
| ├─ Roaming\QQEX | 0.38 GB | QQ扩展数据 |
| └─ Roaming\npm | 0.43 GB | npm 全局包 |
| `C:\Program Files (x86)` | **6.34 GB** | 32位程序 |
| `C:\Program Files` | **1.74 GB** | 64位程序 |

### 3️⃣ E 盘空间占用

| 目录 | 大小 | 说明 |
|------|------|------|
| `E:\WeGameApps\DeltaForce` | **104 GB** | 三角洲行动游戏 |

### 4️⃣ 自启动项目

| 启动项 | 来源 | 说明 |
|--------|------|------|
| WPS Office 应用中心 | Common Startup | WPS 后台进程 |
| RtkAudUService | HKLM-Run | 瑞昱音频后台 |
| ctfmon | HKCU-Run | 输入法 |

**后台驻留服务**（自动启动且高内存）：QQPCRTP (~97MB), AlibabaProtect (~48MB), WSearch (~41MB)

---

## 🗑️ 三、可清理空间建议

### 🟢 安全清理（不影响系统稳定性）

| 项目 | 预估可释放 | 方法 |
|------|-----------|------|
| npm-cache (`AppData\Local\npm-cache`) | **~800 MB** | 运行 `npm cache clean --force` |
| 临时文件 (`Temp`) | ~18 MB | 磁盘清理工具 |
| Windows 旧更新备份 | **~3-5 GB** | `dism /online /Cleanup-Image /StartComponentCleanup` |
| 旧 Quark 版本 (6.4.0.728) | **~1.2 GB** | 保留最新版，删除旧版文件夹 |
| 旧 WPS 版本 (12.1.0.24657) | **~1.3 GB** | 保留最新版，删除旧版文件夹 |
| 浏览器缓存 (INetCache) | ~1 MB | 浏览器内清理 |

**小计**: 可安全释放约 **6.3-8.3 GB**

### 🟡 需确认后清理

| 项目 | 预估可释放 | 说明 |
|------|-----------|------|
| 360se6 浏览器数据 | **~740 MB** | 如果不再使用360浏览器 |
| 磁盘清理 → 回收站 | 需检查 | `cleanmgr /sageset` |

---

## ❌ 四、不必要的软件评估

### 建议卸载（理由）

| 软件 | 大小 | 理由 |
|------|------|------|
| **360安全浏览器** (360se6) | ~387 MB | 已有Chrome，功能重复 |
| **360文件夹大师** | ~N/A | 文件管理工具，Windows已有 |
| **Adobe Flash Player ×2** | ~23 MB | 2021年已停止支持，安全风险 |
| **搜索大师** (搜狗?) | ~N/A | 非必需 |
| **迅雷PDF转换器** | ~N/A | 如不常用PDF转换 |
| **WPS Office 旧版本缓存** | ~2.6 GB | 保留最新版数据即可 |
| **Quark 夸克浏览器** | ~2.5 GB | 如未使用 > 已有Chrome/Edge |
| **腾讯视频 (WeGame)** | 按需 | 如不玩 DeltaForce 游戏 |
| **UE4 Prerequisites** | ~174 MB | 如不玩虚幻4引擎游戏 |
| **Huawei Cloud** | ~696 MB | 如不使用华为云服务 |
| **Huawei HMS Core** | ~N/A | 华为移动服务 |
| **百度网盘** | ~920 MB | 如不常用 |

### 建议保留

- **Microsoft VC++ Redistributables**（全部）：系统运行库，很多程序依赖
- **Python 3.12.7**：开发工具
- **Node.js**：开发工具
- **Git**：版本控制工具
- **Clash Verge**：代理工具
- **Microsoft Edge / Chrome**：浏览器

---

## 📋 五、优化建议（按优先级排序）

### 优先级 🔴 高

1. **给 C 盘扩容**（最有效）
   - 当前 C 盘只有 60 GB，而 D/F 盘基本空置
   - 推荐用磁盘管理工具（如 DiskGenius / AOMEI）从 D 或 F 盘挪 50-80 GB 到 C 盘
   - 或重装系统时分配至少 100-120 GB 给 C 盘

2. **增加内存条到 16 GB**
   - 当前 8 GB 对于 QQ + 浏览器 + 开发工具的组合严重不足
   - 加装一条 8 GB DDR4 内存（约 ¥100-150）可大幅提升体验

### 优先级 🟡 中

3. **C 盘空间释放**
   ```bash
   # 清理临时文件
   cleanmgr /sagerun:1
   
   # 清理 WinSxS 旧版本
   dism /online /Cleanup-Image /StartComponentCleanup
   dism /online /Cleanup-Image /SPSuperseded
   
   # 清理 npm 缓存
   npm cache clean --force
   ```

4. **减少开机自启项**
   - 禁用 WPS Office 应用中心开机启动
   - 关闭 QQ 开机自启（可在 QQ 设置中关闭）
   - 禁用 AlibabaProtect 服务（如不使用阿里软件）

5. **更新 Windows**
   - 有 8 个待安装更新（含 2020 年累积更新 KB4592449）
   - 运行 Windows Update 完成安装

### 优先级 🟢 低

6. **卸载不常用软件**（见第四节）
7. **整理 E 盘**：DeltaForce 游戏 104 GB，如果不常玩可备份存档后卸载
8. **检查虚拟内存设置**：建议设为 8-16 GB (自动管理或手动 8GB+)

---

## ⚡ 六、快速修复命令（一键执行）

打开 **管理员 PowerShell**，逐条执行：

```powershell
# 1. 磁盘清理（回收站、临时文件、缩略图等）
cleanmgr /sageset:1   # 先勾选要清理的项目
cleanmgr /sagerun:1   # 执行清理

# 2. 清理 WinSxS 组件存储
dism /online /Cleanup-Image /StartComponentCleanup
dism /online /Cleanup-Image /AnalyzeComponentStore  # 查看可节省空间

# 3. 清理 npm 缓存
npm cache clean --force

# 4. 关闭不必要的自启服务
sc config "QQPCRTP" start=disabled    # QQ 安全服务
sc config "AlibabaProtect" start=disabled  # 阿里安全

# 5. 系统文件检查（修复系统文件）
sfc /scannow
```

---

## 📝 七、结论

电脑变慢的 **三大主要原因**：

1. **C 盘空间不足** (78.6%) → 系统盘太满，影响虚拟内存和系统缓存
2. **内存仅 8GB 且严重不足** (67.9% 占用) → QQ/夸克等后台程序吃掉大量内存
3. **后台进程过多** (205个) → 大量驻留服务消耗资源

**建议优先**：给 C 盘扩容 + 加内存条，这是提升性能最显著的两项投入。
**不花钱的方案**：清理 npm-cache + 旧版 Quark/WPS + 禁用不必要的自启服务，预计可释放 **6-8 GB** C盘空间，并减少约 500 MB 内存占用。

---

*本报告仅做分析建议，未删除任何文件。如需执行清理，请逐项确认后操作。*
