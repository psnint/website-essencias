
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

import CountryButton from '@/components/CountryButton.vue';

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
      width: 100px;
      left: 60px;
      top: 50%;
      transform: translateY(-50%);
      height: 36px;
      color: white;
      text-transform: uppercase;
      border-radius: 15px;
      cursor: pointer;
      font-size: 14px;
      font-weight: bold;
    }

    &__logo {
      height: 80%;
      position: absolute;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%);
    }

    &__countryLanguage {
      width: 120px;
      position: absolute;
      right: 60px;
      display: flex;
      justify-content: space-evenly;
      top: 50%;
      transform: translateY(-50%);
    }
  }

</style>
