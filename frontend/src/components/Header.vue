
<template>
  <header v-if="!['home'].includes($route.name)" class="header__base">
    <button @click="$router.go(-1)" class="header__back">← Voltar</button>
    <img class="header__logo" alt="Essencias Logo" src="../assets/logo-essencia.png">
  </header>
</template>

<script>
export default {
  name: 'Header',
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
  }

</style>
