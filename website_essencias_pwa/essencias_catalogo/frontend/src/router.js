import Vue from 'vue';
import Router from 'vue-router';
import Home from './views/Home.vue';
import Catalogue from './views/Catalogue.vue';
import Collection from './views/Collection.vue';
import productDetail from './views/ProductDetail.vue';
import API_URL from './configs';

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
      path: '/collection/:id',
      name: 'collection',
      component: Collection,
    },
    {
      path: '/productDetail/:id',
      name: 'productDetail',
      component: productDetail,
    },
    {
      path: '/admin',
      name: 'admin',
      beforeEnter() { window.location.href = `${API_URL}/admin`; },
    },
  ],
});
