<template>
  <div id="app" class="app">
    <Header></Header>
    <!-- <div id="nav">
      <router-link to="/">Home</router-link> |
      <router-link to="/about">About</router-link>
    </div> -->
    <router-view/>
  </div>
</template>


<script>
import Header from '@/components/Header.vue';

export default {
  name: 'App',
  components: {
    Header,
  },
};
</script>

<style lang="scss">
@import 'normalize-scss';
@include normalize();
@import url('https://fonts.googleapis.com/css?family=Arimo:400,700&display=swap');
@import "./css/default.scss";

.app {
  position: absolute;
  height: 100%;
  width: 100%;

  &::after {
    content: "";
    background-image: url("./assets/background.jpg");
    background-position: center;
    background-repeat: no-repeat;
    background-size: cover;
    opacity: 0.5;
    top: 0;
    left: 0;
    bottom: 0;
    right: 0;
    position: fixed;
    z-index: -1;
  }
}

#app {
  font-family: Arimo, 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

</style>
