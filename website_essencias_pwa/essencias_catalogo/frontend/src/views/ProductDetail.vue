<template>
  <div>
    <h1></h1>
    <Gallery :id="$route.params.id"></Gallery>
  </div>
</template>

<script>
import Gallery from '../components/Gallery.vue';

export default {
  name: 'productDetail',
  components: {
    Gallery,
  },
};
</script>

<style lang="scss">
@import "../css/default.scss";

$moduleName: "productDetail";

.#{$moduleName} {
  &__base {
    position: relative;
    max-width: 768px;
    width: 100%;
    margin: auto;
  }

  &__title,
  &__image {
    display: inline-block;
    text-align: center;
    width: 80%;
    margin: auto;
  }

  &__title {
    color: #000;
    font-weight: 300;
    margin: 20px 0;
    text-transform: uppercase;
    font-size: 1rem;

    @include breakpoint-from(mq3) {
      font-size: 1.4rem;
    }
  }

  &__image {
    width: 90%;
  }
}
</style>
