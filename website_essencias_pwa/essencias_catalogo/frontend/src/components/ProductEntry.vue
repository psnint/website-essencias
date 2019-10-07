<template>
  <router-link to="/productDetail" class="productEntry__link">
    <li class="productEntry__base">
        <img class="productEntry__image" :src="`http://localhost:8000/${imgSrc}`" alt="title">
        <div class="productEntry__selected">
          <p class="productEntry__collection">Coleção</p>
          <p class="productEntry__collectionName">{{title}}</p>
        </div>
    </li>
  </router-link>
</template>


<script>

import API_URL from '../configs.js';

export default {
  name: 'ProductEntry',
  props: {
    title: String,
    imgSrc: String,
  },
  methods: {
    API_URL: () => {API_URL},
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">

  $moduleName: 'productEntry';

  .#{$moduleName} {
    &__base {
      margin: 7px;
      overflow: hidden;
      position: relative;
      cursor: pointer;

      &:after {
        content: "";
        background-color: white;
        opacity: 0;
        top: 0;
        left: 0;
        bottom: 0;
        right: 0;
        position: absolute;
        transition: opacity 300ms ease-in;
      }

      &:hover {
        &:after {
          opacity: 0.5;
        }

        .#{$moduleName}__selected {
          opacity: 1;
          transition: opacity 300ms ease-in;
          animation: scale-up-center 0.4s ease-in both;

          @keyframes scale-up-center{
            0%{transform:translateY(-50%) scale(.5)}
            100%{transform:translateY(-50%) scale(1)}
          }
        }
      }
    }

    &__image {
      display: block;
      width: 100%;
      position: relative;
    }

    &__selected {
      position: absolute;
      top: 50%;
      width: 100%;
      transform: translateY(-50%);
      opacity: 0;
      z-index: 1;
      text-transform: uppercase;
    }

    &__collection {
      font-size: 16px;
      margin: 2px 0;
    }

    &__collectionName {
      font-weight: bold;
      font-size: 24px;
      margin: 2px 0;
    }

    &__link {
      text-decoration: none;
      display: block;
      color: black;
    }
  }

</style>
