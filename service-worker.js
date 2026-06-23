const CACHE_NAME = 'time-capsule-v20260623';

// 需要缓存的静态资源（已清空：每次都从网络获取最新文件）
const PRECACHE_URLS = [];

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

// 拦截请求：不做缓存拦截，始终从网络获取最新文件
self.addEventListener('fetch', function(event) {
  return;
});
