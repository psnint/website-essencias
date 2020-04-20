<template>
  <div class="collection__base">
    <ProductList :isCollection="true" :collectionId="$route.params.id"></ProductList>
  </div>
</template>

<script>
// @ is an alias to /src
import ProductList from '@/components/ProductList.vue';

export default {
  name: 'collection',
  components: {
    ProductList,
  },
};
</script>

<style lang="scss">
  $moduleName: 'collection';

  .#{$moduleName} {
    &__base {
    }
  }
</style>
