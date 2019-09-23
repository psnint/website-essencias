<template>
  <router-link to="/catalogue" class="countryButton__base">
    <img class="countryButton__image"
        :src="require(`../assets/country_flags/${imgUrl}`)"
        :alt="`${local}`">
  </router-link>
</template>

<script>
export default {
  name: 'CountryButton',
  props: {
    local: String,
    imgUrl: String,
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">

  $moduleName: 'countryButton';

  .#{$moduleName} {
    &__base {
      width: 27%;
    }

    &__image {
      width: 100%;
      height: 100%;
    }
  }

</style>
