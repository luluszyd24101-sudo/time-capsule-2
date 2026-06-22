const CACHE_NAME = 'time-capsule-v1';

// 需要缓存的静态资源
const PRECACHE_URLS = [
  './',
  './time-capsule.html',
  './manifest.json',
  './changelog.json'
];

// 安装阶段：预缓存核心文件
self.addEventListener('install', function(event) {
  event.waitUntil(
    caches.open(CACHE_NAME).then(function(cache) {
      return cache.addAll(PRECACHE_URLS);
    }).then(function() {
      return self.skipWaiting();
    })
  );
});

// 激活阶段：清理旧缓存
self.addEventListener('activate', function(event) {
  event.waitUntil(
    caches.keys().then(function(cacheNames) {
      return Promise.all(
        cacheNames.filter(function(name) {
          return name !== CACHE_NAME;
        }).map(function(name) {
          return caches.delete(name);
        })
      );
    }).then(function() {
      return self.clients.claim();
    })
  );
});

// 拦截请求：缓存优先（离线也能访问）
self.addEventListener('fetch', function(event) {
  // 只缓存 GET 请求
  if (event.request.method !== 'GET') return;

  event.respondWith(
    caches.match(event.request).then(function(cachedResponse) {
      if (cachedResponse) {
        // 有缓存 → 返回缓存（离线可用）
        return cachedResponse;
      }

      // 没缓存 → 发起网络请求
      return fetch(event.request).then(function(response) {
        // 只缓存有效响应
        if (!response || response.status !== 200 || response.type !== 'basic') {
          return response;
        }

        // 克隆响应（流只能消费一次）
        var responseToCache = response.clone();
        caches.open(CACHE_NAME).then(function(cache) {
          cache.put(event.request, responseToCache);
        });

        return response;
      }).catch(function() {
        // 网络失败时，尝试返回缓存的 fallback 页面
        return caches.match('./time-capsule.html');
      });
    })
  );
});
