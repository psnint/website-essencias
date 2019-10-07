<template>
  <section class="productList__base">
    <div v-if="loading">
      Loading...
    </div>
    <ul class="productList__list">
      <!-- <li v-for="(product, key) in products" :key="key"> -->
      <ProductEntry v-for="(product, key) in products" :key="key"
        :title="product.name" :imgSrc="product.imgUrl"/>
      <!-- </li> -->
    </ul>
  </section>
</template>

<script>

import ProductEntry from './ProductEntry.vue';
import API_URL from '../configs.js';

export default {
  name: 'ProductList',
  components: {
    ProductEntry,
  },
  data() {
    return {
      loading: false,
      error: null,
      products: null,
    };
  },
  created() {
    this.requestProducts();
  },
  methods: {
    requestProducts() {
      this.error = this.products = null;
      this.loading = true
      fetch(`${API_URL}/products`)
        .then( res => res.json())
        .then( res => {
          console.log(res['catalogue']);
          this.loading = false;
          this.products = res['catalogue'];
        });
    },
  },
};

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
@import "../css/default.scss";

  $moduleName: 'productList';

  .#{$moduleName} {
    &__base {

    }

    &__list {
      // display: flex;
      // flex-wrap: wrap;
      // justify-content: space-around;
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(50%, 1fr));
      grid-column-gap: 7px;
      max-width: 1024px;
      margin: 0 auto;
      padding: 0 7px;

      @include breakpoint-from(mq2) {
        grid-template-columns: repeat(auto-fit, minmax(40%, 1fr));
      }
      @include breakpoint-from(mq3) {
        grid-template-columns: repeat(auto-fit, minmax(30%, 1fr));
      }
      @include breakpoint-from(mq4) {
        grid-template-columns: repeat(auto-fit, minmax(20%, 1fr));
      }
    }
  }

</style>
