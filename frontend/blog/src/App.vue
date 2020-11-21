<template>
  <div id="app">
    <login-form />
    <sign-upform />
    <blog-page />
  </div>
</template>

<script>
import LoginForm from "./components/LoginForm.vue";
import SignUpform from "./components/SignUpform";
import BlogPage from "./components/BlogPage.vue";

export default {
  data() {
    return { isloggedin: false };
  },
  name: "App",
  components: {
    LoginForm,
    SignUpform,
    BlogPage
  }
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
