// vue.config.js
module.exports = {
  pwa: {
    name: 'Essencias Catalogue',
    themeColor: '#ced2d3',
    msTileColor: '#000000',
    appleMobileWebAppCapable: 'yes',
    appleMobileWebAppStatusBarStyle: 'black',

    // configure the workbox plugin
    workboxPluginMode: 'GenerateSW',
    workboxOptions: {
      // swSrc: 'src/registerServiceWorker.js',
      runtimeCaching: [{
        urlPattern: new RegExp('^http://127.0.0.1:8000'),
        handler: 'networkFirst',
        // options: {
        //   networkTimeoutSeconds: 20,
        //   cacheName: 'api-cache',
        //   cacheableResponse: {
        //     statuses: [0, 200],
        //   },
        // },
      }],
    },
  },
};
