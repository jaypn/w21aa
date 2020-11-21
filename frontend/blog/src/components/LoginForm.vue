<template>
  <div>
    <h1>Log in Jaypblog</h1>
    <p>username</p>
    <input type="text" v-model="username" />
    <p>password</p>
    <input type="password" v-model="password" />
    <button @click="loginUser">login</button>
  </div>
</template>

<script>
import axios from "axios";
import cookies from "vue-cookie";

export default {
  data() {
    return {
      username: "",
      password: ""
    };
  },
  methods: {
    loginUser: function() {
      axios
        .request({
          method: "POST",
          url: "http://127.0.0.1:5000/login",
          headers: {
            "Content-Type": "application/json"
          },
          data: {
            username: this.username,
            password: this.password
          }
        })
        .then(response => {
          console.log(response);

          cookies.set("blogger_id", response.data[0]);
        })
        .catch(error => {
          console.log(error);
          this.loginStatus = "error";
        });
    }
  }
};
</script>

<style lang="sass" scoped>
</style>