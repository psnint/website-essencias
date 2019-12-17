import Vue from 'vue';
import Router from 'vue-router';
import Home from './views/Home.vue';
import Catalogue from './views/Catalogue.vue';
import productDetail from './views/ProductDetail.vue';

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home,
    },
    {
      path: '/catalogue',
      name: 'catalogue',
      component: Catalogue,
    },
    {
      path: '/productDetail/:id',
      name: 'productDetail',
      component: productDetail,
    },
  ],
});
