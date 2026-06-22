const CACHE_NAME = 'time-capsule-v20260622';

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

// 拦截请求：网络优先，缓存兜底（手机总能拿到最新版）
self.addEventListener('fetch', function(event) {
  // 只缓存 GET 请求
  if (event.request.method !== 'GET') return;

  event.respondWith(
    fetch(event.request).then(function(response) {
      // 缓存成功的响应
      if (response && response.status === 200) {
        var responseToCache = response.clone();
        caches.open(CACHE_NAME).then(function(cache) {
          cache.put(event.request, responseToCache);
        });
      }
      return response;
    }).catch(function() {
      // 离线时使用缓存
      return caches.match(event.request).then(function(cached) {
        return cached || caches.match('./time-capsule.html');
      });
    })
  );
});
