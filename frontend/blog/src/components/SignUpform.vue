<template>
  <div>
    <p>username</p>
    <input type="text" v-model="username" />
    <p>password</p>
    <input type="password" v-model="password" />

    <button @click="signupUser">sign-up</button>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "signup-form",
  data() {
    return {
      username: "",
      password: ""
    };
  },
  methods: {
    signupUser: function() {
      axios
        .request({
          method: "POST",
          url: "http://jayblogpost.ml/api/signup",
          headers: {
            "Content-Type": "application/json"
          },
          data: {
            password: this.password,
            username: this.username
          }
        })
        .then(response => {
          console.log(response);
        })
        .catch(error => {
          console.log(error);
        });
    }
  }
};
</script>

<style lang="sass" scoped>
</style>