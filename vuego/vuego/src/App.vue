<template>
  <div id="app">
    <!-- <img src="./assets/logo.png"> -->
    <Navbar/>
    <router-view/>
  </div>
</template>

<script>
import Navbar from "./components/navbar/Navbar.vue";
export default {
  name: "App",
  data() {
    return {
      message: "Hello world"
    };
  },
  components: {
    Navbar
  }
};
</script>

<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
</style>
