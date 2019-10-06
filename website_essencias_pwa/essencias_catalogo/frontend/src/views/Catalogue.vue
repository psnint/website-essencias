<template>
  <div class="catalogue__base">
    <ProductList></ProductList>
  </div>
</template>

<script>
// @ is an alias to /src
import ProductList from '@/components/ProductList.vue';

export default {
  name: 'catalogue',
  components: {
    ProductList,
  },
};
</script>

<style lang="scss">
  $moduleName: 'catalogue';

  .#{$moduleName} {
    &__base {
    }
  }
</style>
