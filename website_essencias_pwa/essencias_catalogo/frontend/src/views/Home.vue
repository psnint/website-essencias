<template>
  <div class="home__base">
    <img class="home__logo" alt="Essencias Logo" src="../assets/logo-essencia.png">
    <div class="home__countries">
      <CountryButton imgUrl="pt-flag.png" local="pt"/>
      <CountryButton imgUrl="uk-flag.png" local="en"/>
      <CountryButton imgUrl="fr-flag.png" local="fr"/>
    </div>
  </div>
</template>

<script>
import CountryButton from '@/components/CountryButton.vue';

export default {
  name: 'home',
  components: {
    CountryButton,
  },
};
</script>

<style lang="scss">
  $moduleName: 'home';

  .#{$moduleName} {
    &__logo {
      margin-top: 7vh;
    }

    &__countries {
      position: absolute;
      margin: auto;
      display: flex;
      justify-content: space-around;
      width: 60%;
      margin: auto;
      max-width: 612px;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%);
      padding: 40px;

      &::after {
        content: "";
        background: white;
        opacity: .5;
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        z-index: -1;
      }
    }
  }
</style>
