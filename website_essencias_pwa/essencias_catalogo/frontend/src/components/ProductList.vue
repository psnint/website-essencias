<template>
  <section class="productList__base">
    <ul class="productList__list">
      <!-- <li v-for="(product, key) in products" :key="key"> -->
      <ProductEntry v-for="(product, key) in products" :key="key"
        :title="product.title" :imgSrc="product.imgSrc"/>
      <!-- </li> -->
    </ul>
  </section>
</template>

<script>

import ProductEntry from './ProductEntry.vue';

export default {
  name: 'ProductList',
  components: {
    ProductEntry,
  },
  data() {
    return {
      products: [],
    };
  },
  methods: {
    requestProducts() {
      this.products = [
        {
          title: 'Product1',
          imgSrc: 'Page-7-1.png',
        },
        { title: 'Product2', imgSrc: 'Page-3-1.png' },
        { title: 'Product3', imgSrc: 'Page-3-1.png' },
        { title: 'Product3', imgSrc: 'Page-3-1.png' },
        { title: 'Product3', imgSrc: 'Page-3-1.png' },
        { title: 'Product3', imgSrc: 'Page-3-1.png' },
        { title: 'Product3', imgSrc: 'Page-3-1.png' },
        { title: 'Product3', imgSrc: 'Page-3-1.png' },
      ];
    },
  },
  mounted() {
    this.requestProducts();
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
