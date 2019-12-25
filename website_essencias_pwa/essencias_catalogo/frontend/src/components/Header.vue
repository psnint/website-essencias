
<template>
  <header v-if="!['home'].includes($route.name)" class="header__base">
    <button @click="$router.go(-1)" class="header__back">← {{ back[$store.getters.lang] }}</button>
    <img class="header__logo" alt="Essencias Logo" src="../assets/logo-essencia.png">
    <div class="header__countryLanguage">
      <CountryButton imgUrl="pt-flag.png" local="pt"/>
      <CountryButton imgUrl="uk-flag.png" local="en"/>
      <CountryButton imgUrl="fr-flag.png" local="fr"/>
    </div>
  </header>
</template>

<script>

import CountryButton from './CountryButton.vue';

export default {
  name: 'Header',
  data: () => ({
    back: {
      pt: 'Voltar',
      en: 'Back',
      fr: 'Reviens',
    },
  }),
  components: {
    CountryButton,
  },
};
</script>

<style scoped lang="scss">
  @import "../css/default.scss";

  $moduleName: 'header';

  .#{$moduleName} {
    &__base {
      height: 110px;
      width: 100%;
      position: relative;
      max-width: 1024px;
      margin: auto;
    }

    &__back {
      background-color: #d9ab2b;
      position: absolute;
      left: 3%;
      width: 25%;
      top: 50%;
      transform: translateY(-50%);
      height: 30px;
      color: white;
      text-transform: uppercase;
      border-radius: 15px;
      cursor: pointer;
      font-size: 10px;
      font-weight: bold;

      @include breakpoint-from(mq2) {
          left: 60px;
          width: 100px;
          font-size: 14px;
          height: 36px;
      }
    }

    &__logo {
      height: 80%;
      position: absolute;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%);
      @include breakpoint-to(mq2) {
        width: 30%;
        max-height: 161px;
        height: auto;
        max-width: 98px;
      }
    }

    &__countryLanguage {
      width: 25%;
      position: absolute;
      right: 3%;
      display: flex;
      justify-content: space-evenly;
      top: 50%;
      transform: translateY(-50%);

      @include breakpoint-from(mq2) {
        width: 120px;
        right: 60px;;
      }
    }
  }

</style>
