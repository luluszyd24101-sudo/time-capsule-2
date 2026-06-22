# -*- coding: utf-8 -*-
import re

with open('time-capsule.html', 'r', encoding='utf-8') as f:
    content = f.read()

# =================== 1. CSS 添加 ===================
nav_css = '''
/* ============================================================
   === 导航栏 ===================================================
   ============================================================ */
.nav-bar {
  position: fixed;
  top: 0; left: 0; right: 0;
  z-index: 9997;
  background: rgba(255, 248, 240, 0.92);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  box-shadow: 0 2px 20px rgba(200, 100, 120, 0.1);
  display: none;
  padding: 0 12px;
  height: 50px;
  overflow-x: auto;
  overflow-y: hidden;
  white-space: nowrap;
  -webkit-overflow-scrolling: touch;
  scrollbar-width: none;
  align-items: center;
  gap: 2px;
  border-bottom: 1px solid var(--pink-lighter);
}
.nav-bar::-webkit-scrollbar { display: none; }
.nav-bar.show { display: flex; }

.nav-link {
  display: inline-flex;
  align-items: center;
  gap: 3px;
  padding: 6px 12px;
  font-size: 13px;
  font-weight: 500;
  color: var(--warm-text-light);
  text-decoration: none;
  border-radius: 20px;
  transition: all 0.25s ease;
  white-space: nowrap;
  font-family: var(--font-body);
  flex-shrink: 0;
  cursor: pointer;
  background: transparent;
  border: none;
}
.nav-link:hover {
  background: var(--pink-lighter);
  color: var(--pink-dark);
}
.nav-link.active {
  background: linear-gradient(135deg, var(--pink-light), var(--pink));
  color: var(--pink-dark);
  font-weight: 600;
}
.nav-link .nav-emoji { font-size: 15px; }

body.nav-visible { padding-top: 50px; }

/* ============================================================
   === 倒计时模块 ===============================================
   ============================================================ */
.countdown-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(160px, 1fr));
  gap: 14px;
  margin-top: 10px;
}
.countdown-card {
  background: linear-gradient(145deg, #FFF5F7, #FFE8EE);
  border-radius: var(--radius-md);
  padding: 20px 16px;
  text-align: center;
  box-shadow: var(--shadow-soft);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  position: relative;
  overflow: hidden;
}
.countdown-card:hover {
  transform: translateY(-3px);
  box-shadow: var(--shadow-medium);
}
.countdown-card::before {
  content: '';
  position: absolute;
  top: 0; left: 0; right: 0;
  height: 3px;
  background: linear-gradient(90deg, var(--pink-light), var(--pink-strong));
  opacity: 0.5;
}
.countdown-icon {
  font-size: 28px;
  display: block;
  margin-bottom: 6px;
}
.countdown-label {
  font-size: 14px;
  font-weight: 600;
  color: var(--warm-text);
  margin-bottom: 8px;
  font-family: var(--font-deco);
}
.countdown-number {
  font-family: var(--font-deco);
  font-size: 36px;
  font-weight: 700;
  color: var(--pink-strong);
  display: block;
  line-height: 1.2;
  font-variant-numeric: tabular-nums;
}
.countdown-unit {
  font-size: 12px;
  color: var(--warm-text-light);
  margin-top: 2px;
}
.countdown-desc {
  font-size: 12px;
  color: var(--warm-text-light);
  margin-top: 6px;
  opacity: 0.7;
}

/* ============================================================
   === 更新日志模块 ===============================================
   ============================================================ */
.changelog-list {
  max-height: 400px;
  overflow-y: auto;
  padding-right: 6px;
}
.changelog-list::-webkit-scrollbar { width: 4px; }
.changelog-list::-webkit-scrollbar-track { background: var(--pink-lightest); border-radius: 4px; }
.changelog-list::-webkit-scrollbar-thumb { background: var(--pink-light); border-radius: 4px; }

.changelog-item {
  display: flex;
  gap: 12px;
  padding: 12px 14px;
  border-radius: var(--radius-sm);
  margin-bottom: 8px;
  background: var(--pink-lightest);
  border: 1px solid var(--pink-lighter);
  transition: all 0.2s ease;
}
.changelog-item:hover {
  border-color: var(--pink-light);
  box-shadow: var(--shadow-soft);
}
.changelog-date {
  min-width: 85px;
  font-size: 12px;
  color: var(--pink-medium);
  font-weight: 600;
  padding-top: 2px;
}
.changelog-date .cl-time {
  font-weight: 400;
  opacity: 0.6;
  display: block;
  font-size: 11px;
}
.changelog-content {
  flex: 1;
  font-size: 14px;
  line-height: 1.6;
  color: var(--warm-text);
}
.changelog-tag {
  display: inline-block;
  font-size: 11px;
  padding: 2px 8px;
  border-radius: 10px;
  margin-right: 6px;
  font-weight: 600;
  vertical-align: middle;
}
.changelog-tag.tag-new { background: #E8F5E9; color: #2E7D32; }
.changelog-tag.tag-fix { background: #FFF3E0; color: #E65100; }
.changelog-tag.tag-enhance { background: #E3F2FD; color: #1565C0; }
.changelog-tag.tag-other { background: #F3E5F5; color: #6A1B9A; }

.changelog-empty {
  text-align: center;
  padding: 30px;
  color: var(--warm-text-light);
  opacity: 0.6;
  font-size: 14px;
}
.changelog-loading {
  text-align: center;
  padding: 30px;
  color: var(--warm-text-light);
  font-size: 14px;
}
'''

content = content.replace('</style>', nav_css + '\n</style>')

# =================== 2. HTML 添加 ===================
nav_html = '\n  <!-- === 导航栏 ============================================== -->\n  <nav class="nav-bar" id="nav-bar"></nav>\n'
content = content.replace('<main id="main-content">', '<main id="main-content">' + nav_html)

countdown_html = '''
  <div class="section-divider"></div>

  <!-- === 倒计时模块 ============================================= -->
  <section id="countdown-section">
    <h2 class="section-title">⏰ 重要日子倒计时</h2>
    <p class="section-subtitle">每一个值得期待的日子，都在倒计时</p>
    <div class="content-card">
      <div class="countdown-grid" id="countdown-grid"></div>
    </div>
  </section>
'''
content = content.replace(
    '  </section>\n\n  <!-- === 小统计模块 ============================================ -->',
    '  </section>\n' + countdown_html + '\n  <!-- === 小统计模块 ============================================ -->'
)

changelog_html = '''
  <div class="section-divider"></div>

  <!-- === 更新日志 =============================================== -->
  <section id="changelog-section">
    <h2 class="section-title">\U0001f4cb 更新日志</h2>
    <p class="section-subtitle">网站每一次小小的变化，都记录下来啦</p>
    <div class="content-card">
      <div class="changelog-list" id="changelog-list">
        <div class="changelog-loading">⏳ 加载中…</div>
      </div>
    </div>
  </section>
'''
content = content.replace(
    '  <div style="text-align:center;padding:30px 0 10px;color:var(--warm-text-light);font-size:12px;opacity:0.5;">',
    changelog_html + '\n  <div style="text-align:center;padding:30px 0 10px;color:var(--warm-text-light);font-size:12px;opacity:0.5;">'
)

print("Step 1 done: CSS and HTML changes applied")

with open('time-capsule.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("File saved. Now JS...")

# Now read the JS from a separate raw string file and append it
# Actually, let me just use a simpler approach - insert the JS at the right spot
with open('time-capsule.html', 'r', encoding='utf-8') as f:
    content = f.read()

js_code = r'''

  /* ----------------------------------------------------------
     === 导航栏自动生成 ============================================
     ---------------------------------------------------------- */
  function initNav() {
    var nav = document.getElementById('nav-bar');
    if (!nav) return;

    var NAV_ITEMS = [
      { id: 'timer-section', emoji: '\u{1F495}', label: '恋爱计时' },
      { id: 'countdown-section', emoji: '⏰', label: '倒计时' },
      { id: 'stats-section', emoji: '\u{1F4CA}', label: '小数据' },
      { id: 'timeline-section', emoji: '\u{1F4D6}', label: '回忆' },
      { id: 'quote-section', emoji: '\u{1F4AC}', label: '情话' },
      { id: 'quiz-section', emoji: '\u{1F9E1}', label: '测验' },
      { id: 'puzzle-section', emoji: '\u{1F9E9}', label: '拼图' },
      { id: 'wish-section', emoji: '⭐', label: '心愿' },
      { id: 'message-section', emoji: '\u{1F48C}', label: '留言' },
      { id: 'checkin-section', emoji: '\u{1F497}', label: '打卡' },
      { id: 'match-section', emoji: '\u{1F9E0}', label: '默契' },
      { id: 'confession-section', emoji: '\u{1F49D}', label: '告白' },
      { id: 'changelog-section', emoji: '\u{1F4CB}', label: '更新' },
    ];

    NAV_ITEMS.forEach(function(item) {
      var a = document.createElement('button');
      a.className = 'nav-link';
      a.innerHTML = '<span class="nav-emoji">' + item.emoji + '</span> ' + item.label;
      a.dataset.target = item.id;
      a.addEventListener('click', function() {
        var target = document.getElementById(item.id);
        if (target) {
          target.scrollIntoView({ behavior: 'smooth', block: 'start' });
          nav.querySelectorAll('.nav-link').forEach(function(l) { l.classList.remove('active'); });
          a.classList.add('active');
        }
      });
      nav.appendChild(a);
    });

    var navTimer = null;
    function updateActive() {
      var scrollY = window.scrollY + 80;
      var activeId = NAV_ITEMS[0].id;
      NAV_ITEMS.forEach(function(item) {
        var el = document.getElementById(item.id);
        if (el && el.offsetTop <= scrollY) activeId = item.id;
      });
      nav.querySelectorAll('.nav-link').forEach(function(l) {
        l.classList.remove('active');
        if (l.dataset.target === activeId) l.classList.add('active');
      });
    }
    window.addEventListener('scroll', function() {
      if (navTimer) clearTimeout(navTimer);
      navTimer = setTimeout(updateActive, 50);
    });
    setTimeout(updateActive, 500);

    var obs = new MutationObserver(function() {
      if (mainContent.classList.contains('show')) {
        nav.classList.add('show');
        document.body.classList.add('nav-visible');
        obs.disconnect();
      }
    });
    obs.observe(mainContent, { attributes: true, attributeFilter: ['class'] });
  }
  initNav();

  /* ----------------------------------------------------------
     === 倒计时模块（含农历生日）===================================
     ---------------------------------------------------------- */
  (function() {
    var lunarInfo = [
      0x095b0, 0x0a9b0, 0x0a4d0, 0x0a4e0, 0x0d4e0,
      0x0ea50, 0x0b540, 0x0b6a0, 0x095a0, 0x095b0,
      0x0a9b0
    ];
    var lunarYearStart = 2020;

    var springFestivals = {
      2020: { m: 1, d: 25 }, 2021: { m: 2, d: 12 },
      2022: { m: 2, d: 1 },  2023: { m: 1, d: 22 },
      2024: { m: 2, d: 10 }, 2025: { m: 1, d: 29 },
      2026: { m: 2, d: 17 }, 2027: { m: 2, d: 6 },
      2028: { m: 1, d: 26 }, 2029: { m: 2, d: 13 },
      2030: { m: 2, d: 3 }
    };

    function lunarToSolar(lunarY, lunarM, lunarD) {
      var idx = lunarY - lunarYearStart;
      if (idx < 0 || idx >= lunarInfo.length) return null;
      var data = lunarInfo[idx];
      var monthDays = [];
      for (var i = 0; i < 12; i++) {
        monthDays.push((data >> (4 + i)) & 1 ? 30 : 29);
      }
      var offset = 0;
      for (var m = 1; m < lunarM; m++) offset += monthDays[m - 1];
      offset += lunarD - 1;
      var sf = springFestivals[lunarY];
      if (!sf) return null;
      var start = new Date(lunarY, sf.m - 1, sf.d);
      start.setDate(start.getDate() + offset);
      return start;
    }

    function getBirthday() {
      var now = new Date();
      var y = now.getFullYear();
      var bd = lunarToSolar(y, 8, 29);
      if (bd && bd < now) bd = lunarToSolar(y + 1, 8, 29);
      return bd;
    }

    function getNextDate(m, d) {
      var now = new Date();
      var t = new Date(now.getFullYear(), m - 1, d);
      if (t < now) t = new Date(now.getFullYear() + 1, m - 1, d);
      return t;
    }

    function calcCD(target) {
      var diff = target - new Date();
      if (diff <= 0) return { d: 0, h: 0, m: 0, s: 0, passed: true };
      var ts = Math.floor(diff / 1000);
      return { d: Math.floor(ts / 86400), h: Math.floor((ts % 86400) / 3600), m: Math.floor((ts % 3600) / 60), s: ts % 60, passed: false };
    }

    function getQixi() {
      var now = new Date();
      var y = now.getFullYear();
      var d = lunarToSolar(y, 7, 7);
      if (d && d < now) d = lunarToSolar(y + 1, 7, 7);
      return d;
    }

    var container = document.getElementById('countdown-grid');
    if (!container) return;
    var timers = [];

    function render() {
      container.innerHTML = '';
      var items = [
        { label: '\u{1F382} 露露生日', emoji: '\u{1F382}', getT: getBirthday },
        { label: '\u{1F49C} 七弎节', emoji: '\u{1F49C}', getT: getQixi },
        { label: '❤️ 情人节', emoji: '❤️', getT: function() { return getNextDate(2, 14); } },
        { label: '\u{1F384} 圣诞节', emoji: '\u{1F384}', getT: function() { return getNextDate(12, 25); } },
        { label: '\u{1F389} 元旦', emoji: '\u{1F389}', getT: function() { return getNextDate(1, 1); } },
        { label: '\u{1F38A} 纪念日', emoji: '\u{1F38A}', getT: function() {
            var n = new Date();
            var t = new Date(n.getFullYear(), 9, 1);
            if (t < n) t = new Date(n.getFullYear() + 1, 9, 1);
            return t;
          }
        },
      ];
      items.forEach(function(item) {
        var target = item.getT();
        if (!target) return;
        var cd = calcCD(target);
        var card = document.createElement('div');
        card.className = 'countdown-card';
        card.dataset.target = target.getTime();
        card.innerHTML =
          '<span class="countdown-icon">' + item.emoji + '</span>' +
          '<div class="countdown-label">' + item.label + '</div>' +
          '<span class="countdown-number cd-num">' + cd.d + '</span>' +
          '<div class="countdown-unit">天</div>' +
          '<div class="countdown-desc cd-desc">' +
          (cd.passed ? '今天就是！\u{1F389}' : '距离还有 ' + cd.d + ' 天 ' + cd.h + ' 时 ' + cd.m + ' 分 ' + cd.s + ' 秒') +
          '</div>';
        container.appendChild(card);
      });

      timers.forEach(function(t) { clearInterval(t); });
      timers = [];
      timers.push(setInterval(function() {
        container.querySelectorAll('.countdown-card').forEach(function(card) {
          var t = parseFloat(card.dataset.target);
          if (!t) return;
          var cd = calcCD(new Date(t));
          var numEl = card.querySelector('.cd-num');
          var descEl = card.querySelector('.cd-desc');
          if (numEl) numEl.textContent = cd.d;
          if (descEl) {
            descEl.textContent = cd.passed
              ? '今天就是！\u{1F389}'
              : '距离还有 ' + cd.d + ' 天 ' + cd.h + ' 时 ' + cd.m + ' 分 ' + cd.s + ' 秒';
          }
        });
      }, 1000));
    }
    render();
  })();

  /* ----------------------------------------------------------
     === 更新日志加载 ==============================================
     ---------------------------------------------------------- */
  (function() {
    var list = document.getElementById('changelog-list');
    if (!list) return;
    if (typeof BASE_URL === 'undefined') {
      list.innerHTML = '<div class="changelog-empty">更新日志加载失败 \u{1F4DD}</div>';
      return;
    }
    fetch(BASE_URL + 'changelog.json')
      .then(function(r) {
        if (!r.ok) throw new Error('HTTP ' + r.status);
        return r.json();
      })
      .then(function(data) {
        if (!data || !data.length) {
          list.innerHTML = '<div class="changelog-empty">暂无更新记录 \u{1F4DD}</div>';
          return;
        }
        var html = '';
        var tags = { '新功能': 'new', '修复': 'fix', '优化': 'enhance' };
        for (var i = data.length - 1; i >= 0; i--) {
          var item = data[i];
          var tagClass = tags[item.tag] || 'other';
          var tagHtml = item.tag ? '<span class="changelog-tag tag-' + tagClass + '">' + item.tag + '</span>' : '';
          html +=
            '<div class="changelog-item">' +
            '<div class="changelog-date">' + item.date + '<span class="cl-time">' + (item.time || '') + '</span></div>' +
            '<div class="changelog-content">' + tagHtml + item.content + '</div>' +
            '</div>';
        }
        list.innerHTML = html;
      })
      .catch(function() {
        list.innerHTML = '<div class="changelog-empty">更新日志加载失败，请检查网络连接 \u{1F4DD}</div>';
      });
  })();
'''

# Insert JS before closing </script> tag
content = content.replace('</script>', js_code + '\n</script>')

# Check it worked
count_before = content.count('</script>')
if count_before != 1:
    print("WARNING: There are now", count_before, "</script> tags (expected 1)")

with open('time-capsule.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('OK - all modifications applied!')
