<template>
  <router-link :to=" $route.name === 'home' ? 'catalogue' : '' " class="countryButton__base">
    <img class="countryButton__image"
        @click="$store.commit('changeLanguage', local)"
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
    to: String,
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
  @import "../css/default.scss";

  $moduleName: 'countryButton';

  .#{$moduleName} {
    &__base {
      width: 27%;
      @include breakpoint-to(mq2) {
        margin: 0 2%;
        width: 100%;
      }
    }

    &__image {
      width: 100%;
      height: 100%;
    }
  }

</style>
