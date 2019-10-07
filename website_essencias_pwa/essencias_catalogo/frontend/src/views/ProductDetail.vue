<template>
  <div class="productDetail__base">
    <h2 class="productDetail__title">Sabonete de massagem de eucalipto (coleção pitonados)</h2>
    <img class="productDetail__image" src="../assets/catalogue/Page-9-2.png" alt="title">
  </div>
</template>

<script>
// @ is an alias to /src

export default {
  name: 'productDetail',
};
</script>

<style lang="scss">
@import "../css/default.scss";

  $moduleName: 'productDetail';

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
